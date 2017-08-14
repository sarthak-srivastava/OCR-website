from django.conf.urls import url
from . import views
url_patterns = [
     url(r'^$',views.home),
     url(r'^upload_pic',views.upload_pic),
]