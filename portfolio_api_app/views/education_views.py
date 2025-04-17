from portfolio_api_app.models import *
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from portfolio_api_app.serializers import EducationSerializer
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from portfolio_api_app.schemas.education_schema import Schemas


@extend_schema(
    summary=Schemas.EducationSchemaGet["summary"],
    description=Schemas.EducationSchemaGet["description"],
    responses=Schemas.EducationSchemaGet["responses"],
)
@api_view(["GET"])
def get_educations(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    portfolio = getattr(user, "portfolio", None)

    if not portfolio:
        return JsonResponse({"error": "Portfolio not found for this user"}, status=404)

    educations = Education.objects.filter(portfolio=portfolio)
    user_serializer = EducationSerializer(educations, many=True)
    return Response(user_serializer.data)


@extend_schema(
    summary=Schemas.EducationSchemaPost["summary"],
    description=Schemas.EducationSchemaPost["description"],
    responses=Schemas.EducationSchemaPost["responses"],
    request=Schemas.EducationSchemaPost["request"],
)
@api_view(["POST"])
def create_education(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    portfolio, created = Portfolio.objects.get_or_create(user=user)

    serializer = EducationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(portfolio=portfolio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary=Schemas.EducationSchemaDelete["summary"],
    description=Schemas.EducationSchemaDelete["description"],
    responses=Schemas.EducationSchemaDelete["responses"],
    request=Schemas.EducationSchemaDelete["request"],
)
@api_view(["DELETE"])
def delete_education(request, id):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    portfolio = Portfolio.objects.get(user=user)

    education = get_object_or_404(Education, id=id, portfolio=portfolio)

    education.delete()
    return Response({"description": "Education deleted successfully."})


@extend_schema(
    summary=Schemas.EducationSchemaPut["summary"],
    description=Schemas.EducationSchemaPut["description"],
    responses=Schemas.EducationSchemaPut["responses"],
    request=Schemas.EducationSchemaPut["request"],
)
@api_view(["PUT"])
def update_education(request, id):
    user = request.user

    if not user.is_authenticated:
        return Response(
            {"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED
        )

    portfolio = get_object_or_404(Portfolio, user=user)

    education = get_object_or_404(Education, id=id, portfolio=portfolio)

    serializer = EducationSerializer(education, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
