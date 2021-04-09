from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.detail, name='detail' ),
    path('user/<int:user_id>/', views.user, name='user'),
    path('newpost', views.post, name = 'new_post')
]