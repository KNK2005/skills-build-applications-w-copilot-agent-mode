import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

# Users
def populate():
    user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
    user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
    user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

    # Teams
    team1 = Team.objects.create(name='Team Alpha')
    team2 = Team.objects.create(name='Team Beta')
    team1.members.add(user1, user2)
    team2.members.add(user3)

    # Activities
    Activity.objects.create(user=user1, activity_type='Running', duration=30, date='2025-06-01')
    Activity.objects.create(user=user2, activity_type='Cycling', duration=45, date='2025-06-01')
    Activity.objects.create(user=user3, activity_type='Swimming', duration=60, date='2025-06-01')

    # Leaderboard
    Leaderboard.objects.create(team=team1, score=75)
    Leaderboard.objects.create(team=team2, score=60)

    # Workouts
    Workout.objects.create(name='Pushups', description='Do 20 pushups')
    Workout.objects.create(name='Situps', description='Do 30 situps')
    Workout.objects.create(name='Jump Rope', description='Jump rope for 5 minutes')

    print('Test data populated successfully.')

if __name__ == '__main__':
    populate()
