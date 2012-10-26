import json
import hmac
import time
import urllib2
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from api.models import *
# Create your views here.

def basic_view(request):
	### Get all the characters and show
	rep_dict = {}
	characters = {}
	
	reps = character_reputation.objects.all().order_by('name','character')
	for e in reps:
		#print e.name + " :: " + str(e.character.pk)
		
		if rep_dict.has_key(e.name):
			pass
		else:
			rep_dict[e.name] = {}
			
		rep_dict[e.name][e.character.pk] = e.rank_value
		
		if characters.has_key(e.character.pk):
			pass
		else:
			characters[e.character.pk] = {}
			characters[e.character.pk]["name"] = e.character.name
			characters[e.character.pk]["realm"] = e.character.realm
			characters[e.character.pk]["id"] = e.character.pk
			
	#print rep_dict
	
	#query = "SELECT a.name from character_reputation as a LEFT JOIN rank_value, from character_reputation as b "
	
	#characters = character_reputation.objects.distinct('character')
	#for character in characters:
	#	print character
	### show a form for character importing
	return render_to_response("temp.html",{"result":rep_dict,"characters":characters})