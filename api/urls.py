from django.urls import path
from .views import  *

urlpatterns=[
    path('students/',AllStudentsView.as_view(),name='students'),
    path('one-student/<int:id>/',StudentView.as_view(),name='student'),
]