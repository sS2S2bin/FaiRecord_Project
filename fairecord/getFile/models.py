import datetime
from django.db import models
from django.utils import timezone


class File(models.Model):
    file_content = models.CharField(max_length=200)
    down_date = models.DateTimeField('date downloaded')

    def __str__(self):
        return self.file_content
    def was_downloaded_recently(self):
        return self.down_date >= timezone.now() - datetime.timedelta(days=1)
