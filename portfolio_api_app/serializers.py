from rest_framework import serializers
from .models import *


class WorkExperinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperince
        fields = ['id',
                  'occupation_title',
                  'company_name',
                  'date',
                  'description',
                  'tags'
                ]
                  
        extra_kwargs = {
            'id': {'read_only': True},
        }

class PortfolioSerializer(serializers.ModelSerializer):
    work_experiences = WorkExperinceSerializer(read_only=True, many=True)

    class Meta:
        model = Portfolio
        fields = ['role', 'introduction', 'work_experiences']


class CustomUserSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'mobile_number',
            'portfolio',
            'password'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
        }

    def validate_password(self, value):
        if len(value) < 6:
            raise ValidationError(ERROR_MESSAGES['WeakPassword'])
        return value

    def validate_email(self, value):
        current_instance_pk = self.instance.pk if self.instance else None
        if CustomUser.objects.filter(email=value).exclude(pk=current_instance_pk).exists():
            raise ValidationError(ERROR_MESSAGES['EmailExists'])
        return value

    def validate_mobile_number(self, value):
        current_instance_pk = self.instance.pk if self.instance else None
        if CustomUser.objects.filter(mobile_number=value).exclude(pk=current_instance_pk).exists():
            raise ValidationError(ERROR_MESSAGES['PhoneNumberExists'])
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        validated_data['is_staff'] = False
        validated_data['is_superuser'] = False

        return super().create(validated_data)
