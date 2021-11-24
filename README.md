# twt
https://youtu.be/sm1mokevMWk

After the first half hour,
python manage.py shell
to play around and get a feel for the syntax

>>> from main.models import Item, ToDoList
>>> t = ToDoList(name="Tim\'s List") 
>>> t.save
<bound method Model.save of <ToDoList: Tim's List>>>>> ToDoList.objects.all
<bound method BaseManager.all of <django.db.models.manager.Manager object at 0x0000020C8DAEEE20>>     
>>>
instead of <QuerySet [<ToDoList: Tim's List..>]>

Seems to create an emtpy QuerySet on calling all objects
>>> ToDoList.objects.all()                 
<QuerySet []>

# Can't get past this point!

>>> ToDoList.objects.get(id=1)             
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Python38\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\Python38\lib\site-packages\django\db\models\query.py", line 435, in get
    raise self.model.DoesNotExist(
main.models.ToDoList.DoesNotExist: ToDoList matching query does not exist.

Maybe newer versions use new features?
What is causing the bug? (not gettin normal shell results (37min of video))

38min) New section of the video

42min) https://www.techwithtim.net/tutorials/django/sqlite3-database/
Shell commands weren't inputting data?
Not the data (names as strings) we need here
to demontrate renaming id to name
matching query does not exist.

55min mark) Realize I started with:
https://docs.djangoproject.com/en/3.2/intro/tutorial02/
in terms of understanding models.py

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

1u21) Simple Forms

Number of the day:
35/2 = 17.5 = 5.7%
Chance of making a typo and commiting fix

Used in tutorial:
https://getbootstrap.com/docs/4.3/getting-started/introduction/

Best practice (how/what/why differently?!)
https://getbootstrap.com/docs/5.1/getting-started/introduction/#starter-template

Lesson learned: Poorly indented divs are a nightmare and cause of many things not working (but seeming to work as before)

https://www.techwithtim.net/tutorials/django/login-logout/ does it first, but this is part of it
pip install django-crispy-forms