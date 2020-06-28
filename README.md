# *Pol_speak* 
# Quick and useful English to Polish translator

## The Milestone project 3 by _Stan Kaczorkiewicz_

The main purpose of this project, from my point of view, is to prove that I'm familiar and efficent while working with Python and databases, while still taking good care of the front-end design.
Also it's my small step towards the better world, where we as humans don't hate others just because we can't understand them.

From the users' perspective, this project is supposed to help in communication at work with Poles, or just any interaction with Polish- speaking people. It always helps to get positive reactions from foreigners, 
if they see you trying to communicate with them in their language.

It's worth to mention, that during the process of creating this app, there was a need for a very similar one, for the fandom of ["The Name of The Wind"](https://ademre.herokuapp.com/) by Patrick Rothfuss, one of the greatest books of all time.
I decided to use part of the code from this app, to create enviroment for our community to share the ideas for sign language, that will express emotions, while we are covering our faces due to the pandemy, which is based on the book.
I even considered using it as my Milestone Project, but then realised, that a lot of people would participate in creating it and I could not say that it's entirely my own project in the end, even though the code would have been mine.



# UX 
I identified a user as:
- a person who works with immigrants from Poland in a warehouse or an office,
- someone willing to learn few words in new language, without attention to grammar etc,
- A person who is attracted to a Polish-speaking man or woman.
- Firstly I thought about potential travellers to Poland, but then I realised that there's huge amount of websites that cover this subject, while no-one focused on Polish co-workers.

My first idea of the website can be found in assets/images/first_idea.jpg and assets/images/plan_how.jpg among with the first version of database underneath.

# UI
Users that will receive link to the full app, will start on index.html page, that gives them a choice of what actions they want to perform. I decided to create two 'base' files- called base and base_student.
The reason for that is to limit user's ability to edit records inside the database.
This also allows me to send a link for 'student' only, if I don't trust them too much.
The 'Admin', on the other hand, has access to full  spectrum of CRUD operations.
There are doors for the user to come back from 'Student' to 'Admin' page, through the 'Contact' page, that is linked in the footer.
Of course if potential users will recive link to the full app, they can just open it again or hit 'back' button enough times.
I just believe, that someone who would like to only damage my database will be too lazy to do so.

For the same reason there are two, almost identical pages called 'cat' and 'cat_admin'.
'cat_admin' allows user to edit any word and has an admin menu, while 'cat' only allows user to read them.

Due to the way my database is made, I do not allow users to create new categories. They can only choose one of four, but in my honest opinion that's enough for the current level of complicity.

# Features

As mentioned above, this website has two separates navigations, that depend on the user's decisions and purpose of their visit.

It also contains contact form and links to my social media, if they wish to contact me in any way.
All of the above are in the footer, that is the same on both 'base' pages.

Depending on user's choices, website can provide tools to perform all CRUD operations over the database, or only Read if choosen so.

# Features left to implement

As one of my main concerns was security of the app and protection against the acts of vandalism, I would like to enable user to log-in and then only pre-chosen users would be able to delete or edit words in the database. That will go instead of the current version, with two base templates.

Another, very important feature, is the audio file, with recording of right pronaunciation of every word in the database.
As my free MongoDB account has limited memory capacity, I decided to ignore that until I'll find other ways to do so.
Tests with my friends have shown, that my tips in 'pronounce' section do the job.



# Testing

Throughout the proccess of creation, I was constantly testing every new functionality of my app.
I learned during my previous projects and I was testing one change at a time.

The biggest issue was- how to connect all the words in one category and present them to the user in a right place.
In the beginning I was trying to use various "if" statements (as in commit at 29th May), but none of the versions I tried worked.
Googling it brought me many different ways, that weren't suitable for my needs.
Finally I managed to find my own way and that's the one I've got a pleasure to present here in a commit at 31st of May.
Although I believe there's an easier way, that will allow me to avoid repeating the "if" statement so many times.
I'm going to change it just after I'll work it out.

Another interesting test was to send it to few of my English friends and ask them for their opinion.
Only three of them really had a look into the app, what makes me think that it could be a great failure, as English people generally don't like to learn languages.

The last tests after security breach at 27 of June, tought me how to use .gitignore file, and that I've got to set up MONGO_URI as a config variable in Heroku itself, if I don't want it to be visible on my GitHub repository. Otherwise the app doesn't work, which was the issue I fixed with a little help of Code Institute tutor, which I am really grateful for.


## Edit at 27/06/2020 

Today, after sending a link to a friend of mine, I found out that someone who had an access to my app has erased a whole database. It means, that someone spent 20 minutes oh their Saturday, just deleting all 50ish records one after another.
I've sent it to around 20 people and then requested code preview on Slack, Code Institute Team.
Finally I added it to my LinkedIn profile as my newest project, and this is my bet on where the intruder got the access from.
As I've got to recreate the whole database now, I commented parts of the code in app.py, that is responsible for removing and editing records in the database. Now, if user is trying to delete them, it will do nothing, just come back to the list of words again.
Please uncomment it in order to test functionality, this whole situation is a proof that it worked very well.
I just simply cannot believe, that someone was determined enough to just clear all data for no reason.


# Deployment

As I had to create all records in my database by myself, I've decided to deploy this app first. It's much more comfortable to create new records via the app, than in the MongoDB website itself.
I decided to deploy it on Heroku, as it allows deploying python apps, that will not run on GitHub.
To do that I had to create Procfile to show their system how to start the app, and keep updated requirements.txt, so it knows what extensions it needs to install in order for app to run.
I logged in Heroku and created new app, choosing app name and server.
Then I needed to log in to Heroku through GitPod and push it there in the same way as we do with GitHub.
Of course after any update to the libraries, I need to update requirements.txt file, using my terminal.
The final steps to make it works was to declare Config Vars, such as IP and PORT.
With all this in place, I was able to use the app to create new records, what has significantly reduced my usage of GitPod, so my free 100 hours should be enough for this month as well.


# Technologies used:

- HTML5 to structure the page;
- CSS3 for adding the style to it;
- Materialize for navigation and layout and to make every page responsive. It was my first project where I used something else than Bootstrap, which in my opinion was a good lesson and gave me valuable experience, that will benefit me in my professional career.
- JavaScript to add functionality to the contact form from EmailJS;
- Python3 and Jinja2 for functionality of the whole page and reduction of unnecessery, repeatable code;
- GitPod provides me an enviroment where I've been working, also providing version control;
- FontAwesome to provide icons for footer's social links, where Materialize has failed;
- Google Fonts for that fancy font I'm using in the Nav menu;
- W3C validator To validate HTML, Jinja2 and CSS;
- EmailJS to provide me with the functionality of my Contact Form;
- Heroku allowed me to deploy my page for free;
- GitHub to store my work online;
- MongoDB to store my database there
- Developer Tools (build-in feature of Google Chrome), that allowed me to instantly apply all the changes I intened to make and to see their effects (or lack of effects in many cases) immediately;

# Credits

While creating this app, I used some external sources:
- coolors.co to choose the colors palette
- materialize.com to use some CSS and JavaScript. It was my first project with something else than bootstrap. Also the accordion offered by bootstrap is not as nice in my opinion, and I was unable to find side-nav (that is a feature that I really like) in there. 
- I was inspired by the Code Institute course materials, espacially the last mini-project with databases;
- While creating the README file, I was inspired by my own README from a previous project. 

# Acknowledgement

I would like to say thank you to my fiancee for support and her valid opinions regarding to this project. I'm also gratefull for all the good advice from my mentor, Reuben Ferrante, including such small things like good practices about naming global variables with capital letters.
I would also like to mention Tony O'Brien, Nick Mortimer and Andrea Mason who were testing this app and left me some valuable feedback. 
