import json
import hmac
import time
import urllib2
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext
from api import *
# Create your views here.

def get_data(request,c_realm,c_name):
	request_url = "http://us.battle.net/api/wow/character/"+c_realm+"/"+c_name+"?fields=professions,reputation,stats"
	#print request_url
	try:
		result = urllib2.urlopen(request_url).read()
	except urllib2.URLError:
		print "URL ERROR!"
		return render_to_response("temp.html",{"result":"import error..."})

	json_result = json.loads(result)
	
	for x in json_result:
		print x
	
	level = json_result["level"]
	player_class = json_result["class"]
	player_race = json_result["race"]
	
	try:
		user_char = character.objects.get(name=c_name,realm=c_realm)
	except DoesNotExit:
		user_char = character()
	
	user_char.player_class = player_class
	user_char.player_level = level
	user_char.player_race = player_race
	
	try:
		user_char.save()
	except:
		print "database error"
		return render_to_response("temp.html",{"result":"database error..."})
	
	for k in json_result["reputation"]:
		#print k
		#print k["standing"]
		### character, standing, max_for_rank, rep_id, rank_value, name
		
		try:
			rep = character_reputation.object.get(character=user_char,rep_id=k["id"])
		except DoesNotExist:
			rep = character_reputation()
			rep.character=user_char
			rep.rep_id = k["id"]
			rep.name = k["value"]
		
		rep.standing = k["standing"]
		rep.max = k["max"]
		rep.value = k["value"]
		
		try:
			rep.save()
		except:
			print "unable to save rep..."
		
		for x in k:
			#print k[x]
			pass
	
	return render_to_response("temp.html",{"result":"see terminal"})