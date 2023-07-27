from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action


# Create your views here.

def home(request):
    return HttpResponse('<h1>API Page</h1>')

#http methods
# GET           veri çağır
# POST          create
# DELETE        veri sil
# PUT           veri değiştir
# PATCH         parçalı olarak veri değiştir

@api_view(["GET"])
def student_api(request):
    students=Student.objects.all() #veri tipi queryset
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data) # json fromatında

@api_view(["POST"])
def student_create(request):
    # print(request.data)
    # return Response("deneme")
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        message={"message":"Successfully Created"}
        return Response(message,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def student_detail(request,pk):
    # student=Student.objects.get(id=pk)
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(student)
    message={"Successfull"}
    data = {}
    data["message"] = message
    data["data"]= serializer.data
    return Response(data) 

@api_view(["DELETE"])
def student_delete(request,pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    message={"message":"Successfully Deleted"}
    return Response(message) 

# @api_view(["PUT"])
@api_view(["PATCH"])
def student_update(request,pk):
    student = get_object_or_404(Student, pk=pk)
    # PUT
    # serializer=StudentSerializer(instance=student, data=request.data)
    #PATCH
    serializer=StudentSerializer(instance=student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        message={"message":"Successfully Updated"}
        return Response(message)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#!########################### CLASS BASED VIEWS ###############################

#! APIView class

class StudentListCreate(APIView):
    
    
    def get(self, request):
        students=Student.objects.all() 
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            message={"message":"Successfully Created"}
            return Response(message,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class StudentDetail(APIView):
    
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def patch(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            'message': 'Student succesfully deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

#! Generic APIView and Mixins

#GenericAPIView
""" One of the key benefits of class-based views is the way they allow you to compose bits of reusable behavior. REST framework takes advantage of this by providing a number of pre-built views that provide for commonly used patterns.

GenericAPIView class extends REST framework's APIView class, adding commonly required behavior for standard list and detail views. Some Basic Attributes and Methods. """


#mixins
""" The mixin classes provide the actions that are used to provide the basic view behavior. Note that the mixin classes provide action methods rather than defining the handler methods, such as .get() and .post(), directly. This allows for more flexible composition of behavior. Tek başlarına bir işlem yapamazlar. GenericAPIView ile anlamlı oluyor """


class StudentGAV( mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class StudentDetailGAV( mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

#! Concrete View Classes

class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
#! ViewSets 

""" - Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. 

- Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.

There are two main advantages of using a ViewSet class over using a View class.

 - Repeated logic can be combined into a single class. In the above example, we only need to specify the queryset once, and it'll be used across multiple views.
 - By using routers, we no longer need to deal with wiring up the URL conf ourselves.

Both of these come with a trade-off. Using regular views and URL confs is more explicit and gives you more control. ViewSets are helpful if you want to get up and running quickly, or when you have a large API and you want to enforce a consistent URL configuration throughout. """


class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    
    @action(detail=False, methods=["GET"])
    def student_count(self, request):
        count  = {
            "student-count" : self.queryset.count(),
        }
        return Response(count)
    
    
class PathMVS(ModelViewSet):
    
    queryset = Path.objects.all()
    serializer_class = PathSerializer
    
    
    @action(detail=True)
    def student_names(self, request, pk=None):
        path = self.get_object()
        students = path.students.all()
        return Response([i.first_name for i in students])