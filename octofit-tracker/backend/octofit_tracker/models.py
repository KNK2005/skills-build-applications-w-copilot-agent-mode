from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    score = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
