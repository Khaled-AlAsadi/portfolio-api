from rest_framework import serializers
from .models import *


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id',
                  'language',
                  'level'
                  ]
        extra_kwargs = {
            'id': {'read_only': True},
        }


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id',
                  'tag',
                  ]
        extra_kwargs = {
            'id': {'read_only': True},
        }

class WorkExperinceSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    class Meta:
        model = WorkExperince
        fields = ['id',
                  'occupation_title',
                  'company_name',
                  'date',
                  'tags',
                  'description'
                  ]
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])

        work_experience = WorkExperince.objects.create(**validated_data)

        for tag_data in tags_data:
            Tag.objects.create(work_experience=work_experience, **tag_data)

        return work_experience

class PortfolioSerializer(serializers.ModelSerializer):
    work_experiences = WorkExperinceSerializer(read_only=True, many=True)
    languages = LanguageSerializer(many=True,
                                   read_only=True)

    class Meta:
        model = Portfolio
        fields = ['role', 'introduction', 'work_experiences', 'languages']


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'mobile_number',
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
