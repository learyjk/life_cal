from django.db import models


class Week(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.IntegerField()
    week_number = models.IntegerField()
    text = models.TextField(blank=True)

    def __str__(self):
        return str(self.week_number)
