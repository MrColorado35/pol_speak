import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env

# The first part of set-ups is inspired by the course materials, mini project "Task Manager":
app = Flask(__name__)

# os.environ.get('MONGO_URI')
# os.getenv('MONGO_URI')
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@myfirstcluster-vdori.mongodb.net/speak?retryWrites=true&w=majority"
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "speak"
COLLECTION_NAME = "categories"

mongo = PyMongo(app)

categories = mongo.db.categories.find()
cat_list = [category for category in categories]
# desc_list = [description for description in categories]
words = mongo.db.words.find()


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/user.html')
def user():
    # description = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    return render_template("user.html", categories=cat_list)


@app.route('/cat.html/<cat_id>')
def cat(cat_id):
    category = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    words = mongo.db.words.find({'cat_name': "work"})
    romances = mongo.db.words.find({'cat_name': "romance"})
    nsfws = mongo.db.words.find({'cat_name': "NSFW"})
    others = mongo.db.words.find({'cat_name': "other"})
    # word = mongo.db.find_one()
    # cat_name = mongo.db.words.find({'cat_name': ObjectId(cat_name)})
    # words_choosen = mongo.db.words.find({'cat_name': ObjectId(cat_name)})
    return render_template('cat.html', category=category,
        words=words, romances=romances, nsfws=nsfws, others=others)


@app.route('/admin.html')
def admin():
    return render_template("admin.html")


@app.route('/all_words.html')
def all_words():
    words = mongo.db.words.find()
    return render_template("all_words.html", words=words)


@app.route('/add_word.html')
def add_word():
    return render_template("add_word.html", categories=cat_list, words=words)


@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('all_words'))


@app.route('/edit_word.html/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({'_id': ObjectId(word_id)})    
    return render_template("edit_word.html", word=the_word, categories=cat_list,)


@app.route('/update_word/<word_id>', methods=['POST'])
def update_word(word_id):
    words = mongo.db.words
    words.update({'_id': ObjectId(word_id)}, 
    {
        'eng': request.form.get('eng'),     
        'pol': request.form.get('pol'),
        'read': request.form.get('read'),
        'explaination': request.form.get('explaination'),
        'cat_name': request.form.get('cat_name')        
    })
    return redirect(url_for('all_words'))


@app.route('/delete_word.html/<word_id>')
def delete_word(word_id):
    the_word = mongo.db.words.find_one({'_id': ObjectId(word_id)})  
    return render_template("delete_word.html", word=the_word)


@app.route('/remove_word/<word_id>', methods=['POST', 'GET'])
def remove_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('all_words'))


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
