# *Pol_speak* the quick and useful English to Polish translator
## The Milestone project 3 by Stan Kaczorkiewicz

The main purpose of this project from my point of view is to prove that I'm familiar and efficent while working with Python and databases, while still taking good care of the front-end design.
Also it's my small step towards the better world, where we as humans don't hate others just because we can't understand them.

From the user perspective, this project is supposed to help in a in-work communication with Poles, or just any interaction with Polish- speaking people. It always helps to get positive reactions from foreigners, 
if they see you trying to communicate with them in their language.
Here, hopefully, I can provide a tool, that will allow dear users to do so.

It's worth to mention, that during the process of creation this app, there was a need for very similar one, for the fandom of "The Name of The Wind" by Patrick Rothfuss, one of the greatest books of all time.
I decided to use part of the code from this app, to create enviroment for our community to share the ideas for sign language, that will express emotions, while we are covering our faces due to the pandemy.
I even consiedered to change it to my Milestone Project, but then realised that more people will participate in it and I could not say that it's my own project on the end, even though the code will be mine.


# UI 
I identified a user as:
- a person who works with immigrants from Poland in the warehouse or office,
- someone willing to learn few words in new language, without care for grammar etc,
- A person who is attracted in Polish-speaking man or woman.
- Firstly I thought about potentiall travelers to Poland, but then I realised that there's huge amount of websites that cover this subject, while no-one focused on Polish co-workers.

# UX
Users that will receive full link to aplication, will start on index.html page, that gives them a choice of what actions they want to perform. I decided to create two base files- called base and base_student.
The reason for that is to limit user's ability to edit records inside the database.
This also allows me to send a link for 'student' only, if I don't trust them too much.
The 'Admin', on the other hand, has access to full  spectrum of CRUD operations.
There are doors for the user to come back from 'Student' to 'Admin' page, through the 'Contact' page, that is linked in the footer.
Of course if potentiall users will recive link to the full app, they can just open it again or hit 'back' button enough times.
I just believe, that someone who would like to only damage my database will be too lazy to do so. f

# Testing

Throughout the proccess of creation, I was constantly testing every new functionality of my app.
As I learned during my previous projects, I was testing one change at a time.

The biggest issue, that took me three days of thinking and researching to solve, was how to connect all the words of one category and present them to the user in a right place.
On the beginning I was trying to use various "if" statements (as in commit at 29th May), but none of the versions I tried works.
Googling it brought me many different ways, that wasn't suitable for my needs.
Finally I managed to find my own way and that's the one I've got a pleasure to present here in a commit at 31st of May.
Although I believe there's easier way, that will allow me to avoid repeating the "if" statement so many times.
I'm going to change it just after I'll work it out.

Another interesting test was to send it to few of my English friends and ask them for their opinion.
Only one of them really had a look into the app, what makes me think that it could be a great failure, as English people generally don't like to learn languages.



# Deployment

As I had to create all records in my database by myself, I've decided to deploy this app first. It's much comfier to create new records via the app, than in the MongoDB website itself.
I decided to deploy it on Heroku, as it allows deploying python apps, that will not run on GitHub.
To do that I had to create Procfile to show their system how to start the app, and keep updated requirements.txt, so it knows what extensions in needs to install in order for app to run.
Then I needed to log in to Heroku through GitPod and push it there in the same way as we do with GitHub.
Of course after any update to the libraries, I need to update requirements.txt file, using my terminal.
The final steps to make it works was to declare Config Vars, such as IP and PORT.
With all this in place, I was able to use the app to create new records, what has significantly reduced my usage of GitPod, so my free 100 hours should be enough for this month as well.


# Credits

While creating this app, I used some external sources:
- coolors.co to choose the colors palette
- materialize.com to use some CSS and JavaScript. Also it's worth to mention, that it was my first project with     something else than bootstrap. Also the accordion offered by bootstrap is not as nice in my opinion, and I was unable to find side-nav in bootstrap. It is a feature that I really like. 
- I was inspired by the Code Institute course materials, espacially the last mini-project with databases.
