from django.test import TestCase
from .models import Game


# Create your tests here.
class TestGame_test_cases(TestCase):
    def test_game_creation(self):
        game = Game(title="Pokemon")
        game.save()
        self.assertEqual(Game.objects.count(), 1)

    def test_read_all_games(self):
        game = Game.objects.create(title="Pokemon")
        game.save()

        games = Game.objects.all()
        title = [Game.title for game in games]
        self.assertEqual(len(title), 1)

    def test_delete_game(self):
        D = Game(title="Pokemon")
        D.save()

        # title = [Game.title for game in games]

        D.delete()
        games = Game.objects.all()
        self.assertEqual(len(games), 0)

    def test_update_game(self):
        game = Game.objects.create(title="Pokemon")
        game.save()
        game.title = "Pokemon: Black"
        game.save()

        self.assertEqual(game.title, "Pokemon: Black")

    def test_read_by_title(self):
        game = Game.objects.create(title="Pokemon")
        game.save()
        game_return = Game.objects.get(title="Pokemon")
        self.assertEqual(game_return.title, "Pokemon")

    def test_filtered_search(self):
        game = Game.objects.create(title="Pokemon")
        game.save()
        game_return = Game.objects.filter(title="Pokemon")
        self.assertEqual(game_return[0].title, "Pokemon")
