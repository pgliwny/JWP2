from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Przekazujemy do szablonu zmienną "message"
    return render_template('home.html', message="Witaj w naszym prostym projekcie Flask!")

if __name__ == '__main__':
    app.run(debug=True)