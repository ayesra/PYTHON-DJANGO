from django.urls import path, include
from rest_framework import routers
from .views import (
    home,
    student_api,
    student_create,
    student_detail,
    student_delete,
    student_update,
    
    #!Class Views
    StudentListCreate,
    StudentDetail,
    
    StudentGAV,
    StudentDetailGAV,
    
    StudentCV,
    StudentDetailCV,
    
    StudentMVS,
    PathMVS
    )

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)


urlpatterns = [

]

urlpatterns += router.urls