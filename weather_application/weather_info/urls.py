from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing_page, name="Home"),
    path('Services/', views.Services, name="Services"),
    path('About/', views.About, name="About"),
    path('Contact/', views.Contact, name="Contact")
]
