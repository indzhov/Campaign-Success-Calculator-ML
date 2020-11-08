from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('persona.pkl', 'rb'))
app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():

    ### Variables ###
    
    wines = 0
    fruits = 0
    meat = 0
    sweets = 0
    gold = 0
    fish = 0
    web_p = 0
    catalog_p = 0
    store_p = 0
    child_Yes = 0


    prodcuts = request.form['a']
    if prodcuts == "wine":
        wines = 1
    elif prodcuts == "fruit":
        fruits = 1
    elif prodcuts == "meat":
        meat = 1
    elif prodcuts == "sweet": 
        sweet = 1
    elif prodcuts == "gold":
        gold = 1
    elif prodcuts == "fish":
        fish = 1
    
    channels = request.form['b'] 
    if channels == "web_p":
        web_p = 1
    elif channels == "catalog_p":
        catalog_p = 1 
    elif channels == "store_p":
        store_p = 1 
    child = request.form['c'] 
    if child == "child_yes":
        child_Yes = 1
    elif child == "child_no":
        child_Yes = 0

    arr = np.array([[wines, fruits, meat, sweets, gold, fish, web_p, catalog_p, store_p, child_Yes]])
    pred = model.predict(arr)
    return render_template('after.html', data=pred)

  




if __name__ == "__main__":
    app.run(debug=True)















