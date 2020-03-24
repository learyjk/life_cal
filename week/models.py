from django.db import models


class Week(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    week_number = models.IntegerField()
    text = models.TextField(blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return "O"
