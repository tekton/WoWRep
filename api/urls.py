from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('',
    # Trial Pay Integration.
    (r'/(.*)/(.*)/','api.views.get_data'),
)