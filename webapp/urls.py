from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'), 
    path('help/', views.help_page, name='help'),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),

]
