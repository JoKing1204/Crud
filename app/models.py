from django.db import models


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


# create game
def make_game(title):
    game = Game(title=title)
    game.save()


# read all
def read_all_games():
    return Game.objects.all()


# read filtered
def read_filter(title):
    return Game.objects.filter(title=title)


# reads by unique identifier(title)
def read_by_title(title):
    return Game.objects.get(title=title)


# updates game name
def update_game(old_title, new_title):
    game = Game.objects.get(title=old_title)
    game.title = new_title
    game.save()


# deletes game
def delete_game(title):
    D = Game.objects.filter(title=title)
    D.delete()
