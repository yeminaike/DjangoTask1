from django.urls import path
from . import views

urlpatterns = {
        path('like/', views.like, name='like'),
        path('post/', views.post, name='post'),
        path('message/', views.message, name='message'),

}