from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from portfolio_api_app.serializers import WorkExperinceSerializer


class Schemas:
    WorkSchemaGet = {
        "summary": "Retrive User Work Experiences",
        "description": "Retrive User Work Experiences",
        "responses": {
            200: WorkExperinceSerializer,
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

    WorkSchemaPost = {
        "summary": "Creates User Work Experience",
        "description": "Creates User Work Experience",
        "request": WorkExperinceSerializer,
        "responses": {
            200: WorkExperinceSerializer,
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

    WorkSchemaDelete = {
        "summary": "Deletes Saved User Work Experience",
        "description": "Deletes Saved User Work Experience",
        "request": str,
        "responses": {
            200: WorkExperinceSerializer,
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

    WorkSchemaPut = {
        "summary": "Updates User Language",
        "description": "Updates User Language with given ID",
        "request": WorkExperinceSerializer,
        "responses": {
            200: WorkExperinceSerializer,
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
