from django.urls import path
from .views import result_query, check

urlpatterns = [
    path('proccedquery/', result_query, name='result_query'),
    path('check/', check, name='check'),
]