#module 10.5.1
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

#The first line says that we'll use Flask to render a template, redirecting to another url, and creating a URL.
#The second line says we'll use PyMongo to interact with our Mongo database.
#The third line says that to use the scraping code, we will convert from Jupyter notebook to Python.

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#uniform resource identifier uri is similar to url mar_app was made in module 10.4.1
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#app.config["MONGO_URI"] tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL. 
#"mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".

#html page route line 1 find mars collection after converting jupyter scraping code to python script
#Flask will return an html template using an indexhtml file 
#mars=mars thells python to use the mars collectin in MondDB
#this function is what links our visual representation of our work, our web app, to the the code that powers it

@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

   #scraping route the button of the web application that will scarpe udated data when we tell it to 

@app.route("/scrape")
def scrape():
   mars = mongo.db.mars #new variable that point to our mongo databse
   mars_data = scraping.scrape_all()  #new variable to hold the nwely scraped data from imports line 1
   mars.update_one({}, {"$set":mars_data}, upsert=True) #update the database after gathering new data
   return redirect('/', code=302)

if __name__ == "__main__":
    app.run()
