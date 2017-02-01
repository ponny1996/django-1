from tempfile import template

from django.conf.urls import url
from pip import index

import mary
from mary import views

urlpatterns = [

    url(r'bb/', views.get ,name='pp'),

    url(r'^dd/',views.index,name='oo')

]