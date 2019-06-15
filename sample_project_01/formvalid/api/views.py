from rest_framework.viewsets import ModelViewSet
from formvalid.models import Student
from formvalid.api.serializers import StudentSerializers


class StudentView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
