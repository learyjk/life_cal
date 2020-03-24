from django.db import models
from datetime import date, timedelta


class Week(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    week_number = models.IntegerField()
    text = models.TextField(blank=True)
    date = models.DateField(null=True)

    def __str__(self):
        return "O"

    @property
    def is_past(self):
        return self.date <= date.today()

    @property
    def is_current_week(self):
        return self.date <= date.today() and self.date > (date.today() - timedelta(7))
