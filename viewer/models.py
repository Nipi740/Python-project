# Create your models here.
from django.db.models import CharField, Model, ForeignKey, DO_NOTHING, IntegerField, TextField, DateTimeField, DateField


class Genre(Model):
    name = CharField(max_length=128)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField(null=True)
    description = TextField()
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.released.year})"
