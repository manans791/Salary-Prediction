from flask import Flask, render_template , request
import pandas as pd
import numpy as np
import pickle

app = Flask('__name__')

model = pickle.load(open("model.pkl","rb"))
df = pd.read_csv("Cleaned_data_salary.csv")

@app.route('/')
def home():


    return render_template("index.html")

@app.route('/predict', methods=["get","post"])
def predict():
    Education = request.form.get('Education')
    Experience = request.form.get('Experience')
    Age = request.form.get('Age')
    Gender = request.form.get('Gender')
    Area = request.form.get('Area')
    if Area=='Rural':
        Rural =1
        Suburban=0
        Urban=0
    elif Area=='Suburban':
        Rural = 0
        Suburban = 1
        Urban = 0
    else:
        Rural = 0
        Suburban = 0
        Urban = 1

    Designation = request.form.get('Designation')
    if Designation=='Analyst':
        Analyst=1
        Director=0
        Engineer=0
        Manager=0
    elif Designation=='Director':
        Analyst = 0
        Director = 1
        Engineer = 0
        Manager = 0
    elif Designation=='Engineer':
        Analyst = 0
        Director = 0
        Engineer = 1
        Manager = 0
    else:
        Analyst = 0
        Director = 0
        Engineer = 0
        Manager = 1



    prediction = model.predict([[Education,Experience,Age,Gender,Rural,Suburban,Urban,
                                 Analyst,Director,Engineer,Manager]])

    print(prediction)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction="Your Annual Salary would be  {} $".format(output))

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)