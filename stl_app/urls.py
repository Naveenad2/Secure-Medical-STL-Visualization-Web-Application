from django.urls import URLPattern, path
from . import views

from django.conf import settings
from django.urls import  re_path


from django.views.static import serve

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),

    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

    path('', views.main, name='main'),
    path('models/<int:id>',views.models,name='models'),
    path('model_details/<int:id>',views.model_details,name='model_datails'),
    path('stl/<int:id>',views.stl,name='stl'),
    path('Login',views.Login,name='Login'),
    path('user_login',views.user_login, name='user_login')
]