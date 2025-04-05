from flask import Flask

app = Flask(__name__)  # Tworzymy instancję aplikacji

@app.route("/")         # Dekorator określa ścieżkę URL
def hello():
    return "To jest strona główna!"  # Zwracamy prostą odpowiedź

@app.route("/hello")
def say_hello():
    return "Witaj świecie!"

@app.route("/about")
def about():
    return "To jest podstrona 'O nas'."

@app.route("/user/<name>")
def greet_user(name):
    return f"Cześć, {name}!"

if __name__ == "__main__":
    app.run(debug=True)  # Uruchamiamy aplikację w trybie debug
