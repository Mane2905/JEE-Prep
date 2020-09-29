from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from . import views
urlpatterns=[
    path('',views.index,name="home"),
    path('physics',views.physics,name='physics'),
    path('chemistry',views.chemistry,name='chemistry'),
    url(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
