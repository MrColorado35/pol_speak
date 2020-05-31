# *Pol_speak* the quick and useful English to Polish translator
## The Milestone project 3 by Stan Kaczorkiewicz

The main purpose of this project from my point of view is to prove that I'm familiar and efficent while working with Python and databases, while still taking good care of the front-end design.

From the user perspective, this project is supposed to help in a in-work communication with Poles, or just any interaction with Polish- speaking people. It always helps to get positive reactions for your presence from foreigners, 
if they see you trying to communicate with them in their language.
Here, hopefully, I can provide a tool, that will allow dear users to do so.

# UI 
I identified a user as:
- a person who works with immigrants from Poland in the warehouse or office,
- someone willing to learn few words in new language, without care for grammar etc,
- English speaking person who want to travel to Poland
- A person who is attracted in Polish-speaking man or woman.

# Testing

Throughout the proccess of creation, I was constantly testing every new functionality of my app.
As I learned during my previous projects, I was testing one change at a time.
The biggest issue, that took me three days of thinking and researching to solve, was how to connect all the words of one category and present them to the user in a right place.
On the beginning I was trying to use "if" statement (as in commit at 29th May), but none of the versions I tried works.
Googling it brought me many different ways, that wasn't suitable for my needs.
Despite an advice given by my mentor, to create a "sub-collection" in my app.py file, I decided to find my own way and that's the one I've got a pleasure to present here.

# Deployment

As I had to create all records by myself, I've decided to deploy this app first. It's much comfier to create new records via the app, than in the MongoDB website itself.
I decided to deploy it on Heroku, as it allows deploying python apps, that will not run on GitHub.
To do that I had to create Procfile to show their system how to start the app, and keep updated requirements.txt, so it knows what extensions in needs to install in order for app to run.
Then I needed to log in to Heroku throu GitPod and push it there in the same way as we do with GitHub.
Of course after any update to the libraries, I need to update requirements.txt file, using my terminal.
The final steps to make it works was to declare Config Vars, such as IP and PORT.
With all this in place, I was able to use the app to create new records, what has significantly reduced my usage of GitPod, so my free 100 hours should be enough this month as well.


# Credits

While creating this app, I used some external sources:
- coolors.co to choose the colors palette
- materialize.com to use some CSS and JavaScript. Also it's worth to mention, that it was my first project with     something else than bootstrap. 
- I was inspired by the Code Institute course materials, espacially the last mini-project with databases.
