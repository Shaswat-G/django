Python manager.py startapp movies

This creates another folder called movies with a subfolder for migrations and a packgae with __init__.py with admin (how will the amdin area look like), apps (config.py), models (classes that represent the domain of the apps and functionality), tests (automated tests) and views (resource controller / exchangers).

views.py
Index is the main page of a service.


urls.py
This has to be created by convention with this name only. We have to make a list object called urlpatterns - we add objects and url endpoints.
This urlpatterns list is called the url configutration wchich every app should have. Basically, when you make and http request to the server, 
django will find (match) the correspoinding urlpattern and call the approriate view.

Then you include urls of these kinds by extending the urls.py in the main app called strefront. You have to additionally import the include function from path
{expand on what include does and how does django map a url endpoint to a view.


models.py
django.db encapsualte all the finctionality related to workgin with databases.
SO we derive (inherit) from this class and then we do not have to write any code to write say Genre (or derived class) object into the db.

the models module alllows us to store model objects, retrieve them and so on.
class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='movies')
    # rating = models.DecimalField(max_digits=3, decimal_places=1)
    # duration = models.IntegerField()  # in minutes
    # image_url = models.URLField()



django supoorts all types of db engines like MS sql serve, mongo db, pstgtessql, oracle, etc [expand on all the modern db engines used in modern apps]

sqlite is a serverless, security less no concurrency based light db for mobile and local applications used for tesing [expand on what are the main features and pros and cons of sqlite]

you can tables, indices, biews and triggers. [Expand on what each of them are and what do they do]


django comapares the model clases and db tables and creates a migration file [expand ont he details, terminologies and the process here]
that sync our db with model classes.

 python manage.py makemigrations -> genetates the migrations.py file with the operations needed for sync

  python manage.py migrate