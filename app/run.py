from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from pathlib import Path
from google.cloud import storage, pubsub_v1
import os, time, cv2, imutils, threading



app = Flask(__name__)
IMAGES_FOLDER = 'images'
ROTATED_IMAGES_FOLDER = 'rotatedImages'
BUCKET_NAME_ORIGINAL = 'cloud-systems'
BUCKET_NAME_ROTATED = 'cloud-systems-rotated'
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER
app.config['ROTATED_IMAGES_FOLDER'] = ROTATED_IMAGES_FOLDER
app.config['BUCKET_NAME_ORIGINAL'] = BUCKET_NAME_ORIGINAL
app.config['BUCKET_NAME_ROTATED'] = BUCKET_NAME_ROTATED
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/jakub/.gcp/serviceaccount.json"

if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

if not os.path.exists(ROTATED_IMAGES_FOLDER):
    os.makedirs(ROTATED_IMAGES_FOLDER)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return 'No file part', 400
    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400
    if file:
        rotation_degrees = int(request.form['rotation_degrees'])
        if rotation_degrees > 0 or rotation_degrees < 360:
            filepath = os.path.join(app.config['IMAGES_FOLDER'], file.filename)
            file.save(filepath)
            threading.Thread(target=upload_image, args=(app.config['BUCKET_NAME_ORIGINAL'], filepath, file.filename, {'angle-to-rotate': rotation_degrees})).start()
        return redirect(url_for('index'))
    

@app.route('/get/images/native', methods=['GET'])
def get_images():
    images = []
    objects = list_blobs(app.config['BUCKET_NAME_ORIGINAL'])
    for object in objects:
        images.append({
            'name': object.name,
            'url': f'/uploads/{object.name}'
        })
    return jsonify({'images': images})

@app.route('/get/images/rotated', methods=['GET'])
def get_images_rotated():
    images = []
    objects = list_blobs(app.config['BUCKET_NAME_ROTATED'])
    for object in objects:
        images.append({
            'name': object.name,
            'url': f'/uploads/{object.name}'
        })
    return jsonify({'images': images})


@app.route('/download/native/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory("../"+app.config['IMAGES_FOLDER'], filename, as_attachment=True)

@app.route('/download/rotated/<filename>', methods=['GET'])
def download_file_rotated(filename):
    return send_from_directory("../"+app.config['ROTATED_IMAGES_FOLDER'], filename, as_attachment=True)



def upload_image(bucket_name, source_file_name, destination_blob_name, metadata):

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.metadata = metadata

    #generation_match_precondition = 0

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )
    os.remove(source_file_name)

def list_blobs(bucket_name):
    storage_client = storage.Client()
    return storage_client.list_blobs(bucket_name)

def blob_metadata(bucket_name, blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.get_blob(blob_name)
    return blob.metadata

def download_blob(bucket_name, source_blob_name, destination_file_name):

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )



def rotate_image(filename):
    rotation_degrees = int(blob_metadata(app.config['BUCKET_NAME_ORIGINAL'],filename)["angle-to-rotate"])
    print("Rotating: "+ filename + " Degrees: " + str(rotation_degrees))
    image_to_rotate = os.path.join(os.getcwd(), app.config['IMAGES_FOLDER'], filename)
    download_blob(app.config['BUCKET_NAME_ORIGINAL'],filename,image_to_rotate)

    image_to_save = os.path.join(os.getcwd(), app.config['ROTATED_IMAGES_FOLDER'], construct_filename_for_rotated_image(filename))

    image = cv2.imread(image_to_rotate)
    rot = imutils.rotate(image, angle=rotation_degrees)   
    cv2.imwrite(image_to_save,rot)

    threading.Thread(target=upload_image, args=(app.config['BUCKET_NAME_ROTATED'], image_to_save, construct_filename_for_rotated_image(filename), {'rotated-angle': rotation_degrees})).start()
    os.remove(image_to_rotate)
    print("Rotated: "+ filename + "by " + str(rotation_degrees) + " degrees")

def construct_filename_for_rotated_image(filename):
    path = Path(filename)
    return str(path.with_stem(f"{path.stem}_{'rotated'}"))



def poll_notifications(project, subscription_name):
    subscription_path = 'projects/{project_id}/subscriptions/{sub}'.format(
        project_id=project,
        sub=subscription_name,
    )

    def callback(message):
        if message.attributes["eventType"] == "OBJECT_FINALIZE":
            print("Uploaded: "+ message.attributes["objectId"]+" Bucket: "+message.attributes["bucketId"]+" Date: "+message.attributes["eventTime"])
            threading.Thread(target=rotate_image, args=(message.attributes["objectId"],)).start()
        message.ack()

    subscriber = pubsub_v1.SubscriberClient()
    subscriber.subscribe(subscription_path, callback=callback)

    print(f"Listening for messages on {subscription_path}")
    while True:
        time.sleep(100)

if __name__ == '__main__':
    threading.Thread(target=poll_notifications, args=('cloud-systems-course', 'cloud-systems')).start()
    app.run()