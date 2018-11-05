from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


LAB_CHOICES = (
    ('Within', 'Within'),
    ('Outside', 'Outside')
)


class Job(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    lab_choice = MultiSelectField(max_length=13, max_choices=1, choices=LAB_CHOICES)
    deadline = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('job-detail', kwargs={'pk': self.pk})



