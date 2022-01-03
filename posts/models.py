from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

choices_location = (
    ('head', 'head'),
    ('knee', 'knee'),

)

choices_type = (
    ('simple', 'simple'),
    ('CTscan', 'CTscan'),
)


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)


class Report(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(choices=choices_location, max_length=20)
    type = models.CharField(choices=choices_type, max_length=20)

    def __str__(self):
        return self.user.username + "-" + self.title

#report image is coded for many images and in two field can be unique
# first: user
# second : report

class ReportImages(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True)
    report = models.ForeignKey(Report, default=None, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.user.username
