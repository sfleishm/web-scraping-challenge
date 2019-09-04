from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import Image 
import time
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrapingMars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mData")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    marsData = mongo.db.mData.find_one()

    # Return template and data
    # return render_template("index.html", mars=marsData)
    return render_template("index.html", marsData=marsData)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mData = mongo.db.mData
    # Run the scrape function
    marsData = scrapingMars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mData.update({}, marsData, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

