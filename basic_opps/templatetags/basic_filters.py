from django import template
from django.template import Variable, VariableDoesNotExist
register = template.Library()
@register.filter
def gVal(object, attr):
	pseudo_context = { 'object' : object }
	print "gVal" + str(attr) +" - "+ str(pseudo_context)
	try:
		value = Variable('object.%s' % attr).resolve(pseudo_context)
	except VariableDoesNotExist:
		value = None
	return value

@register.filter
def xVal(a,b):
	print "xVal",a,b
	if b.has_key(a):
		value = b[a]
	else:
		value = "0"
	return value