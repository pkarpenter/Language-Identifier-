from django.urls import path

from . import views  # Welcome, user

urlpatterns = [
    path('', views.Welcome, name='welcome'),
    path('user/', views.user, name='user'),
    path('predictor', views.predictor, name='predictor'),
    path('result/', views.result, name='result'),
    path('Services/', views.Services, name='Services'),
    path('Contect/', views.Contect, name='Contect'),
    path('about/', views.about, name='about'),
    # path('Home/', views.about, name='Home'),
    

]