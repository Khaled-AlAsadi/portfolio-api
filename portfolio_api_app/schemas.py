from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from .serializers import *


class Schemas:
    TokenObtainSchema = {
        "summary": "Obtain Token",
        "description": "Authenticates the user and returns a JWT token pair.",
        "responses": {
            200: inline_serializer(
                name="TokenObtainResponse",
                fields={
                    "access": serializers.CharField(),
                    "refresh": serializers.CharField(),
                }
            ),
            401: OpenApiResponse(
                description="Unauthorized access",
            ),
            404: OpenApiResponse(
                description="Not found",
            ),
            500: OpenApiResponse(
                description="Internal server error",
            ),
        },
    }

    UserSchema = {
        "summary": "Retrive User Info",
        "description": "",
        "request": CustomUserSerializer,
        "responses": {
            200: CustomUserSerializer,
            401: OpenApiResponse(
                description="Unauthorized access",
            ),
            404: OpenApiResponse(
                description="Not found",
            ),
            500: OpenApiResponse(
                description="Internal server error",
            ),
        },
    }
