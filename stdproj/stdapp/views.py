from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from .models import Student,Teacher
from .serializers import StudentSerializer,TeacherSerializer

class StudentCreateAPIView(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[JSONWebTokenAuthentication,]
    permission_classes=[IsAuthenticated,]

class StudentListAPIView(generics.ListAPIView):
    serializer_class=TeacherSerializer
    # authentication_classes=[TokenAuthentication,]
    # permission_classes=[IsAuthenticated,]

    def get_queryset(self):
        qs=Teacher.objects.all()
        # qs=Teacher.objects.order_by('sid')

        # print(q
        # print(id1)
        # if id1 is not None:
        #     qs=qs.filter(Teacher__icontains=id1)
        return qs

# Create your views here.
