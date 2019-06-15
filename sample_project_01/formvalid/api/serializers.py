from rest_framework.serializers import ModelSerializer
from formvalid.models import Student

class StudentSerializers(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'