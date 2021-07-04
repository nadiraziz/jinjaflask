from flask import Flask, render_template
import requests

app = Flask(__name__)

AGE_API = "https://api.agify.io?name="
GENDER_API = "https://api.genderize.io?name="


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/guess/<name>')
def guess(name):
    guess_name = name
    get_gender = requests.get(f"{GENDER_API}{guess_name}").json()
    get_age = requests.get(f"{AGE_API}{guess_name}").json()
    guess_gender = get_gender['gender']
    guess_age = get_age['age']
    return render_template('guess.html', name=guess_name, age=guess_age, gender=guess_gender)


if __name__ == "__main__":
    app.run(debug=True)