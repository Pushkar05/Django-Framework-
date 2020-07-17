from django.urls import path
from . import views


# / question
# /question/1/detail
# Here we provide a Path for our model

urlpatterns = [
    path('', views.index),
    path('new', views.new)




]