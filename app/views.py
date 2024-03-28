from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import  ListCreateAPIView,  RetrieveUpdateDestroyAPIView
    

class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 



class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer