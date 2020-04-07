from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^submit$', submit, name='submit'),
    url(r'^ranking$', ranking, name='ranking'),
]