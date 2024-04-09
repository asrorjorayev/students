from rest_framework import serializers
from .models import Student


class AllStudentsSerializerView(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields=['id','first_name','last_name','email','phone_number','location']

    def validate(self, data):
        first_name=data.get('first_name')

        if len(first_name)<4 or len(first_name)>30:
            result={
                'messege':'Uzunlik 4 dan uzun 30 dan qisqa bolishi kerak'
            }
            raise serializers.ValidationError(result)
    def create(self, validated_data):
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        email=validated_data.get('email')
        phone_number=validated_data.get('phone_number')
        location=validated_data.get('location')
        Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            location=location
        )
        return validated_data
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        
        return instance
    