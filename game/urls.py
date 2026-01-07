"""
URL patterns for the game app.
"""
from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('select/', views.level_select_view, name='level_select'),
    path('calibrate/', views.calibration_view, name='calibration'),
    path('play/<str:mode>/<str:level>/', views.play_view, name='play'),
]
