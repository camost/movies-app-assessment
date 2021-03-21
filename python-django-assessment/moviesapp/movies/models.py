# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from star_ratings.models import Rating
from django.contrib.contenttypes.fields import GenericRelation

class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255,unique=True)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64,default='PG-13')
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    photo = models.ImageField(upload_to='img',default='img/default-cover.jpg')
    # Todo: add Rating models
    rating= GenericRelation(Rating)


    class Meta:
       ordering = ['-rating__average','created_at']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'pk': self.pk})
