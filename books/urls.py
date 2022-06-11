from django.urls import path

from books import views

urlpatterns = [
    path('search-form/', views.search_form),
    path('search/', views.search),
    path('contact/', views.contact),
]
