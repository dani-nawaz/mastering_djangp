from django.urls import path

from . import views

urlpatterns = [
    path('', views.DroneList.as_view(), name='drone-list'),
    path('drone-category/', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    path('drone-category/<int:pk>', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    path('<int:pk>/', views.DroneDetail.as_view(), name='drone-detail'),
    path('competition/', views.CompetitionList.as_view(), name='competition-detail'),
    path('pilot/', views.PilotList.as_view(), name='competition-detail'),
]
