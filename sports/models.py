from django.db import models
from django.shortcuts import reverse


class Sport(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    sport_type = models.CharField(max_length=100)

    def get_detail_url(self):
        return reverse('sports:detail', args=[self.pk])

    def get_update_url(self):
        return reverse('sports:update', args=[self.pk])

    def get_delete_url(self):
        return reverse('sports:delete', args=[self.pk])


