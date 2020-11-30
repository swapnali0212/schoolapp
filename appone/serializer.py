from rest_framework.serializers import ModelSerializer
from appone.models import Student, Teacher, Subject, UserProfi

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class UserProfiSerializer(ModelSerializer):
    class Meta:
        model = UserProfi
        fields = '__all__'
