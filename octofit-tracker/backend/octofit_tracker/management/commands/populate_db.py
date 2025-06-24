from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1, user2])
        team2 = Team.objects.create(name='Team Beta', members=[user3])

        # Activities
        Activity.objects.create(user=user1, activity_type='run', duration=30, date=datetime(2025, 6, 1))
        Activity.objects.create(user=user2, activity_type='walk', duration=45, date=datetime(2025, 6, 2))
        Activity.objects.create(user=user3, activity_type='cycle', duration=60, date=datetime(2025, 6, 3))

        # Leaderboard
        Leaderboard.objects.create(user=user1, score=120)
        Leaderboard.objects.create(user=user2, score=110)
        Leaderboard.objects.create(user=user3, score=130)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups')
        Workout.objects.create(name='Situps', description='Do 30 situps')
        Workout.objects.create(name='Squats', description='Do 40 squats')

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
