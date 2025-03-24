# users/urls.py
from django.urls import path
from .views import *


urlpatterns = [
    #path('', UserList.as_view(), name='user-list'),
    path('', get_student),
    path('students/', post_student, name='students' ),
]
