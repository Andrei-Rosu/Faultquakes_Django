from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User


class Newswall(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    video = models.URLField(blank=True)
    image = models.ImageField(upload_to='news_pics', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})



# Create your models here.
