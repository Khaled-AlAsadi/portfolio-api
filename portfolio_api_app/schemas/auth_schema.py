from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample, OpenApiResponse


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
                },
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
