from flask import Flask, request
from faker import Faker
import pandas as pd
import requests


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



@app.route("/mean/")
def mean():
    df = pd.read_csv(r'/home/kirtsun/Стільниця/hw.csv')
    weight = df[' "Weight(Pounds)"'].median()
    weight = weight / 2.2046
    average_weight = round(weight, 1)
    height = df[' "Height(Inches)"'].median()
    height = height * 2.54
    average_height = round(height, 1)
    return f"<p>Average_height = {average_height} centimeter.<br>Average_weight = {average_weight} kilograms. </p>"







