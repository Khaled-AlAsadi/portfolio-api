from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from portfolio_api_app.serializers import CustomUserSerializer
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers


class Schemas:
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
