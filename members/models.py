from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


TEAM_CHOICES = (
    ('Geodesy', 'Geodesy'),
    ('Rock mechanics', 'Rock mechanics'),
    ('Modeling', 'Modeling')
)
STATUS = (
    ('Permanent', 'Permanent'),
    ('Postdoc', 'Postdoc'),
    ('Phd', 'Phd'),
    ('Visitor', 'Visitor'),
    ('Former', 'Former')
)


class Member(models.Model):
    name = models.CharField(max_length=250)
    status = MultiSelectField(max_choices=1, choices=STATUS)
    team = MultiSelectField(max_length=31, max_choices=3, choices=TEAM_CHOICES)
    office = PhoneNumberField(blank=True)
    email = models.EmailField(blank=True)
    www = models.URLField(blank=True)
    description = models.TextField()
    mobile = PhoneNumberField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='members_pics')
    uploaded_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('member-detail', kwargs={'pk': self.pk})




