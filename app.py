import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env

# The first part of set-ups is inspired by the course materials, mini project "Task Manager":
app = Flask(__name__)

app.config["MONGO_URI"]= "mongodb+srv://root:r00tUser@myfirstcluster-vdori.mongodb.net/speak?retryWrites=true&w=majority"
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "speak"
COLLECTION_NAME = "categories"

mongo = PyMongo(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/user.html')
def user():

    return render_template("user.html", categories=mongo.db.categories.find())

@app.route('/admin.html')
def admin():
    return render_template("admin.html")
    
@app.route('/all_words.html')
def all_words():    
    return render_template("all_words.html", words=mongo.db.words.find())

@app.route('/add_word.html')
def add_word():
    return render_template("add_word.html")

@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('all_words'))


@app.route('/edit_word.html/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({'_id': ObjectId(word_id)})
    
    return render_template("edit_word.html", word=the_word)

@app.route('/delete_word.html')
def delete_word():
    return render_template("delete_word.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)