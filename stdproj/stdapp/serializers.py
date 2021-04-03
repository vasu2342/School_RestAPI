from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    sid=serializers.IntegerField()
    sname=serializers.CharField(max_length=64)
    sclass=serializers.CharField(max_length=64)

class TeacherSerializer(serializers.Serializer):
    student=StudentSerializer(read_only=True)
    smarks=serializers.IntegerField()
    spercentage=serializers.CharField(max_length=64)
