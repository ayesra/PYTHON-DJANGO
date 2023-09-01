from django.urls import path,include
from .views import (
    home,
    body,
    studentView,
    student_addView,
    StudentAddView,
    StudentListView,
    StudentDetailView,
    StudentUpdateView
)
urlpatterns = [
    path('', body),
    path('home', home),
    path('student', studentView,name='list2'), # name ler uniq olmalı
    # forms
    #fbv
    # path('add', student_addView)
    #cbv
    path('student-list',StudentListView.as_view(),name='list'),
    path('student-add', StudentAddView.as_view(),name='add'),
    path('student-detail/<int:pk>',StudentDetailView.as_view(),name='detail'),
    path('student-update/<int:pk>',StudentUpdateView.as_view(),name='update'),
]
