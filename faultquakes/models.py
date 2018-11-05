from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

TEAM_CHOICES = (
    ('Geodesy', 'Geodesy'),
    ('Rock mechanics', 'Rock mechanics'),
    ('Modeling', 'Modeling')
)


class Post(models.Model):
    title = models.CharField(max_length=250, default='Title', blank=True)
    authors = models.CharField(max_length=250, default='Authors', blank=True)
    journal = models.CharField(max_length=250, default='Journal', blank=True)
    # number = models.IntegerField
    # pages = models.IntegerField
    year = models.DateTimeField(default=timezone.now)
    # date_modified = models.DateTimeField
    publisher = models.CharField(max_length=250, default='Publisher', blank=True)
    url = models.CharField(max_length=250, default='Url', blank=True)
    doi = models.CharField(max_length=250, default='DOI', blank=True)
    # bdsk = models.CharField(max_length=250)
    team = MultiSelectField(max_length=31, max_choices=3, choices=TEAM_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(default='default.jpg', upload_to='publication_pics')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Research(models.Model):
        title = models.CharField(max_length=250, default='Title', blank=True)
        authors = models.CharField(max_length=250, default='Authors', blank=True)
        journal = models.CharField(max_length=250, default='Journal', blank=True)
        # number = models.IntegerField
        # pages = models.IntegerField
        year = models.DateTimeField(default=timezone.now)
        # date_modified = models.DateTimeField
        publisher = models.CharField(max_length=250, default='Publisher', blank=True)
        url = models.CharField(max_length=250, default='Url', blank=True)
        doi = models.CharField(max_length=250, default='DOI', blank=True)
        # bdsk = models.CharField(max_length=250)
        team = MultiSelectField(max_length=31, max_choices=3, choices=TEAM_CHOICES)
        date_posted = models.DateTimeField(default=timezone.now)
        uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
        image = models.ImageField(default='default.jpg', upload_to='research_pics')

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('research-detail', kwargs={'pk': self.pk})



