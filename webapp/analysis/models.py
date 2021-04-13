from django.db import models
from query.models import Tweet, Tumblr

class Study(models.Model):
	user = models.CharField('user',max_length=60)
	study_id = models.CharField('study_id',max_length=100)
	tweets = models.ManyToManyField(Tweet)
	count = models.BigIntegerField('count')

class Tumblr_Study(models.Model):
	user = models.CharField('user',max_length=60)
	tumblr_study_id = models.CharField('tumblr_study_id',max_length=100)
	posts = models.ManyToManyField(Tumblr)
	count = models.BigIntegerField('count')
