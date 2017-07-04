
from django.conf.urls import url

from comments import views


urlpatterns = [

    url(r'^create/$', views.create_comment, name='create'),

    url(r'^list/(?P<content_type>\d+)/(?P<object_id>\d+)/$',
        views.get_comments, name='list'),

]