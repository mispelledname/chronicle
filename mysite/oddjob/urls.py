from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.detail, name='detail' ),
    path('user/<int:xid>/', views.user, name='user'),
    path('newpost', views.post, name = 'new_post'),
    path('login', views.login_view, name = 'login_view'),
    path('register', views.register_view, name = 'register_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('me', views.self_view, name="self_view"),
    path('accept/<int:job_id>/<int:user_id>', views.accept_job, name='accept') 
]