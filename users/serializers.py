from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fileds = ['id','name','email']

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


    def validate_name(self, data):
        if data['name']:
         for n in data['name']:
            if  n.isdigit():
             raise serializers.ValidationError({'error': "Name must only contain alphabetic characters (no numbers or special characters)"})
            
            
        return data