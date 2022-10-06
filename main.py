from flask import Flask, request
from faker import Faker



app = Flask(__name__)
fake = Faker()


@app.route("/requirements/")
def requirements():
    with open('requirements.txt', 'r') as file_one:
        text = file_one.readlines()
    text = "<br>".join(text)
    return text

@app.route("/generate-users/", methods=['GET'])
def generate_users():
    count = request.args.get("count", "100", type=int)
    lst = []
    for _ in range(count):
        name = f'{fake.name()}: {fake.email()}'
        lst.append(name)
    lst = "<br>".join(lst)
    return f"<p>{lst}</p>"




