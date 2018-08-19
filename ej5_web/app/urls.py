from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('table/<int:id>', views.disparities, name='disparities'),
]
