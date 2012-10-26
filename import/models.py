from django.db import models

# Create your models here.

class character(models.Model):
	name = 
	realm = 
	player_class = 
	

class characters(models.Model):
	user = model.ForeignKey(User)
	character = model.ForeignKey(character)