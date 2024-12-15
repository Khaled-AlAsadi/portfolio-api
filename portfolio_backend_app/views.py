from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .schemas import *


@extend_schema(
    responses={200: HealthCheckSchemas.RESPONSE}
)
@api_view(['GET'])
def health_check(request):
    return Response({
        "status": "healthy",
        "message": "The application is running."
    })
