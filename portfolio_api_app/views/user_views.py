from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from portfolio_api_app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from portfolio_api_app.schemas.user_schema import Schemas
from django.http import HttpResponse, JsonResponse
from portfolio_api_app.models import *
from portfolio_api_app.errors import *


@extend_schema(
    summary=Schemas.UserSchema["summary"],
    description=Schemas.UserSchema["description"],
    responses=Schemas.UserSchema["responses"],
)
@api_view(["GET"])
def get_user(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    user_serializer = CustomUserSerializer(user)
    return Response(user_serializer.data)


@extend_schema(
    summary=Schemas.UserSchema["summary"],
    description=Schemas.UserSchema["description"],
    responses=Schemas.UserSchema["responses"],
    request=Schemas.UserSchema["request"],
)
@api_view(["PUT"])
def update_user(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    try:
        serializer = CustomUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Portfolio.DoesNotExist:
        return JsonResponse({"error": "Portfolio not found"}, status=404)
