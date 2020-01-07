from django.urls import path
from . import views as diary_views
urlpatterns = [
    path('',diary_views.index,name='index'),
    path('add/',diary_views.add,name='add'),
]
