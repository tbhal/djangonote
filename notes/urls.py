from django.conf.urls import include, url
from django.urls import path
from notes.views import index_view, add_note, add_tag, tag_search, register, about

app_name = 'notes'

urlpatterns = [
    path('', index_view, name='index'),
    path('addnote/', add_note, name='addnote'),
    path('addtag/', add_tag, name='addtag'),
    path('register/', register, name='register'),
    path('about/', about, name='about'),
    url(r'^tags/(?P<slug>[-\w]+)/$', tag_search, name='tagsearch'),
]