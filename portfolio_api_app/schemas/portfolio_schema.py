from drf_spectacular.utils import OpenApiResponse
from portfolio_api_app.serializers import PortfolioSerializer


class Schemas:
    PortfolioSchemaGet = {
        "summary": "Retrive Saved User Portfolio",
        "description": "Retrive Saved User Portfolio",
        "responses": {
            200: PortfolioSerializer,
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

    PortfolioSchemaPatch = {
        "summary": "Updates Saved User Portfolio",
        "description": "Updates Saved User Portfolio",
        "responses": {
            200: PortfolioSerializer,
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
