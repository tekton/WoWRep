from django.db import models
from django.contrib.auth.models import User

# Create your models here.
	
class character(models.Model):
	name = models.CharField(max_length=255)
	realm = models.CharField(max_length=255)
	player_class = models.IntegerField(max_length=255,blank=True,null=True) ### int TODO get class table
	player_level = models.IntegerField(blank=True,null=True) ###int, TODO get class table
	player_race = models.IntegerField(max_length=255,blank=True,null=True) ### int, TODO table to translate race
	def __unicode__(self):
		return self.name + " ("+self.realm+")"
		
class character_reputation(models.Model):
	character = models.ForeignKey(character)
	standing = models.CharField(max_length=255,blank=True,null=True)
	max_for_rank = models.CharField(max_length=255,blank=True,null=True)
	rep_id = models.CharField(max_length=255)
	rank_value = models.CharField(max_length=255,blank=True,null=True)
	name = models.CharField(max_length=255,blank=True,null=True)
	def __unicode__(self):
		return self.name + " ["+self.character.name+"("+self.character.realm+")"+"]"
		#return self.name + " | " + self.rank_value + "/" + self.max_for_rank
		# + "["+self.character.name+"("+self.character.realm+")"+"]"

class characters(models.Model):
	user = models.ForeignKey(User)
	character = models.ForeignKey(character)