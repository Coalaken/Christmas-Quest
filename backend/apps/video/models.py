from django.db import models
from django.core.validators import FileExtensionValidator


class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to='video/%m/%d', validators=[
            FileExtensionValidator(['mp4'])
        ]
    )

    def __str__(self):
        return str(self.title)


