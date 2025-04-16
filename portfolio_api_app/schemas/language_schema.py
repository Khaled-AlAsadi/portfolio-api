from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from portfolio_api_app.serializers import LanguageSerializer


class Schemas:
    LanguageSchemaGet = {
        "summary": "Retrive User Languages",
        "description": "Retrive User Languages",
        "responses": {
            200: LanguageSerializer,
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

    LanguageSchemaPost = {
        "summary": "Creates User Language",
        "description": "Creates User Language",
        "request": LanguageSerializer,
        "responses": {
            200: LanguageSerializer,
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

    LanguageSchemaDelete = {
        "summary": "Deletes Saved User Language",
        "description": "Deletes Saved User Language with given ID",
        "request": str,
        "responses": {
            200: LanguageSerializer,
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

    LanguageSchemaPut = {
        "summary": "Updates User Language",
        "description": "Updates User Language with given ID",
        "request": LanguageSerializer,
        "responses": {
            200: LanguageSerializer,
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
