from portfolio_api_app.serializers import *
from portfolio_api_app.schemas import *
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from portfolio_api_app.models import *
from portfolio_api_app.schemas.portfolio_schema import Schemas


@extend_schema(
    summary=Schemas.PortfolioSchemaPatch["summary"],
    description=Schemas.PortfolioSchemaPatch["description"],
    responses=Schemas.PortfolioSchemaPatch["responses"],
)
@api_view(["PATCH"])
def update_portfolio(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    try:
        portfolio, created = Portfolio.objects.get_or_create(user=user)

        serializer = PortfolioSerializer(portfolio, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Portfolio.DoesNotExist:
        return JsonResponse({"error": "Portfolio not found"}, status=404)


@extend_schema(
    summary=Schemas.PortfolioSchemaGet["summary"],
    description=Schemas.PortfolioSchemaGet["description"],
    responses=Schemas.PortfolioSchemaGet["responses"],
)
@api_view(["GET"])
def get_portfolio(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    portfolio = getattr(user, "portfolio", None)

    user_serializer = PortfolioSerializer(portfolio)
    return Response(user_serializer.data)
