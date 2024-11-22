from django.urls import path
from . import views
from .views import index,signup_view,signin_view,dashboard


urlpatterns = [
    path('',views.index, name='index'),
    path('signup/',views.signup_view, name='signup'),
    path('signin/',views.signin_view, name='signin'),
    path('dashboard/',views.dashboard, name='dashboard'),
]