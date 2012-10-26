import json
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import Http404
from django.template import RequestContext

import hmac
import time
import urllib2

# Create your views here.

def get_data(request,realm,character):
	request_url = "http://us.battle.net/api/wow/character/"+realm+"/"+character+"?fields=professions,reputation,stats"
	print request_url
	try:
		result = urllib2.urlopen(request_url).read()
	except urllib2.URLError:
		print "URL ERROR!"
		return render_to_response("temp.html",{"result":"import error..."})
	#print result
	#json_result = json.loads(result)
	json_result = json.loads(result)
	#print json_result
	
	for k in json_result["reputation"]:
		print k
		#print k["standing"]
		for x in k:
			print k[x]
	
	return render_to_response("temp.html",{"result":json_result})