from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contactlist/", views.contactList, name="contactList"),
    path('contacts/<int:pk>/', views.contactView, name="contacts"),
    path("login/", views.loginpage, name="login"),
    path("signup/", views.signup, name="signup"),
    path('logout/',views.logoutuserpage, name="logout"),
    path('Newcontact/' ,views.createContact, name="newcontact"),
    path('add_to_favourite/<int:pk>/', views.add_to_favourite, name='add_to_favourite'),
    path('remove_favorite/<int:pk>/', views.remove_favorite, name='remove_favorite'),
    path('add_to_emergency/<int:pk>/', views.add_to_emergency, name='add_to_emergency'),
    path('remove_emergency/<int:pk>/', views.remove_emergency, name='remove_emergency'),
    path('profile/', views.userprofile, name='profile'),
    path('edit_profile/', views.updateuser, name="edit_profile"),
    path('delete_contact/<int:contact_id>/', views.delete_contact, name='delete_contact'),
]