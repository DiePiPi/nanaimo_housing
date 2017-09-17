from django.conf.urls import url

from views import (tutorials, tutorials_list)


urlpatterns = [
    url(r'^$', tutorials_list),
    url(r'^(.*)$', tutorials),
    ]
