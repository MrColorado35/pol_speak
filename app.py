import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import env

# The first part of set-ups is inspired by the course materials, mini project "Task Manager":
app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

CATEGORIES = mongo.db.categories.find()
cat_list = list(CATEGORIES)
ALL_WORDS = mongo.db.words.find()

# This decorator brings us the main page
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# If we choose that we want to learn Polish, here's where we go
@app.route('/user')
def user():
    # description = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    return render_template("user.html", categories=cat_list)

# Allows us to see all categories and then all the words in specific order.
@app.route('/cat/<cat_id>')
def cat(cat_id):
    # try:
    #     category = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    # except Exception:
    #     flash("There was an error getting the category")
    #     redirect(url_for('user.html'))

    category = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    words = mongo.db.words.find({'cat_name': "work"})
    romances = mongo.db.words.find({'cat_name': "romance"})
    nsfws = mongo.db.words.find({'cat_name': "NSFW"})
    others = mongo.db.words.find({'cat_name': "other"})

    # word = mongo.db.find_one()
    # cat_name = mongo.db.words.find({'cat_name': ObjectId(cat_name)})
    # words_choosen = mongo.db.words.find({'cat_name': ObjectId(cat_name)})
    return render_template('cat.html', category=category, categories=CATEGORIES,
        words=words,  romances=romances, nsfws=nsfws, others=others)

# Brings page for Admin, with a list of all options that admin is allowed to do.
@app.route('/admin')
def admin():
    return render_template("admin.html")

# Provide an access to all words without keeping them in order.
@app.route('/all_words')
def all_words():
    words = mongo.db.words.find()
    return render_template("all_words.html", words=words)

# That part of code allows Admin to add new words in a new page, dedicated to it.
@app.route('/add_word')
def add_word():
    return render_template("add_word.html", categories=cat_list, words=ALL_WORDS)


@app.route('/insert_word', methods=['POST'])
def insert_word():
    try:
        words = mongo.db.words
        words.insert_one(request.form.to_dict())
    except:
        flash("Unknown error. please try again.")
    return redirect(url_for('all_words'))

# This bit of code allows us to edit all aspects of any word in the database
@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({'_id': ObjectId(word_id)})    
    return render_template("edit_word.html", word=the_word, categories=cat_list,)


@app.route('/update_word/<word_id>', methods=['POST'])
def update_word(word_id):
    words = mongo.db.words
    try:
        words.update({'_id': ObjectId(word_id)}, 
        {
            'eng': request.form.get('eng'),
            'pol': request.form.get('pol'),
            'read': request.form.get('read'),
            'explaination': request.form.get('explaination'),
            'cat_name': request.form.get('cat_name')        
        })
    except Exception:
        flash("There was an error with your querry, please try again")
       
    return redirect(url_for('all_words'))

# These are allowing admin to permanently delete any word from the database. I'm still unsure if I should leave it while 
# letting people to use my app freely.

@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    the_word = mongo.db.words.find_one({'_id': ObjectId(word_id)})  
    return render_template("delete_word.html", word=the_word)


@app.route('/remove_word/<word_id>', methods=['POST', 'GET'])
def remove_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('all_words'))

# This one allows us to go to contact page. This is also a trick to help to come out from the "user's trap" that I 
# created earlier and that will not allow users to go back to admin page through the menu
@app.route('/contact')
def contact():
    return render_template("contact.html")

# Thats my newest idea, to allow an admin to see words divided by categories, not only as a pile of all words from 
# the websie together, kept without any order

@app.route('/admin_cat')
def admin_cat():
    return render_template("admin_cat.html", categories=cat_list)

@app.route('/cat_admin/<cat_id>')
def cat_admin(cat_id):
    category = mongo.db.categories.find_one({'_id': ObjectId(cat_id)})
    words = mongo.db.words.find({'cat_name': "work"})
    romances = mongo.db.words.find({'cat_name': "romance"})
    nsfws = mongo.db.words.find({'cat_name': "NSFW"})
    others = mongo.db.words.find({'cat_name': "other"})
    
    return render_template('cat_admin.html', category=category,
        words=words, romances=romances, nsfws=nsfws, others=others,)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
