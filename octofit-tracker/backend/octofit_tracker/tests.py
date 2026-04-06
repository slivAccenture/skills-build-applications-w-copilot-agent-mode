from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        user = User.objects.create_user(username='testuser', email='test@user.com', password='testpass', team=marvel)
        Activity.objects.create(user=user, type='Run', duration=30, calories=300)
        Workout.objects.create(name='Test Workout', description='Test Desc', duration=20)
        Leaderboard.objects.create(user=user, score=100)

    def test_team(self):
        self.assertEqual(Team.objects.count(), 1)

    def test_user(self):
        self.assertEqual(User.objects.count(), 1)

    def test_activity(self):
        self.assertEqual(Activity.objects.count(), 1)

    def test_workout(self):
        self.assertEqual(Workout.objects.count(), 1)

    def test_leaderboard(self):
        self.assertEqual(Leaderboard.objects.count(), 1)
