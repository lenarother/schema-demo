from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    author_id = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'bookshelf\".\"books'