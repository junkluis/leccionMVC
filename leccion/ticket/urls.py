from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^FormActualizar/(?P<Id>[0-9]+)$', views.updateTicket, name='updateTicket'),
    url(r'^update/(?P<factId>[0-9]+)$', views.update, name='update'),
]
