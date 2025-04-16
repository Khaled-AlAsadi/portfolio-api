from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from portfolio_api_app.serializers import EducationSerializer
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, inline_serializer
from rest_framework import serializers


class Schemas:
    EducationSchemaGet = {
        "summary": "Retrive User Educations",
        "description": "Retrive Saved User Educations",
        "responses": {
            200: EducationSerializer,
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

    EducationSchemaPost = {
        "summary": "Creates User Education",
        "description": "Creates User Education",
        "request": EducationSerializer,
        "responses": {
            200: EducationSerializer,
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

    EducationSchemaDelete = {
        "summary": "Deletes Saved User Education",
        "description": "Deletes Saved User Education with given ID",
        "request": str,
        "responses": {
            200: EducationSerializer,
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

    EducationSchemaPut = {
        "summary": "Updates User Education",
        "description": "Updates User Education",
        "request": EducationSerializer,
        "responses": {
            200: EducationSerializer,
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
