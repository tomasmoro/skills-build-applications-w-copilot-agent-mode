from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

# Define models for each collection
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'teams'

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'users'

class Activity(models.Model):
    user_email = models.EmailField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'workouts'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Team.objects.all().delete()
        User.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel'),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel'),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC'),
            User(name='Batman', email='batman@dc.com', team='DC'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user_email='spiderman@marvel.com', activity_type='Running', duration=30),
            Activity(user_email='ironman@marvel.com', activity_type='Cycling', duration=45),
            Activity(user_email='wonderwoman@dc.com', activity_type='Swimming', duration=60),
            Activity(user_email='batman@dc.com', activity_type='Yoga', duration=20),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Workouts
        workouts = [
            Workout(name='Full Body Blast', description='A full body workout for all levels.'),
            Workout(name='Cardio Burn', description='High intensity cardio session.'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
