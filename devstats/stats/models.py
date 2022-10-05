# django imports
from django.db import models


class Developer(models.Model):
    username = models.CharField(max_length=100,
                                unique=True)
    name = models.CharField(max_length=100,
                            blank=True)
    location = models.CharField(max_length=100,
                                blank=True)
    company = models.CharField(max_length=100,
                                blank=True)
    avatar_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)

    # counts
    total_followers = models.PositiveIntegerField(default=0)
    total_following = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username


class Repo(models.Model):
    name = models.CharField(max_length=250)
    developer = models.ForeignKey(Developer,
                                  related_name='repos',
                                  on_delete=models.CASCADE)

    stargazers_count = models.PositiveIntegerField(default=0)
    watchers_count = models.PositiveIntegerField(default=0)
    forks_count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [('developer', 'name')]

    def __str__(self):
        return f'{self.developer.username}/{self.name}'
