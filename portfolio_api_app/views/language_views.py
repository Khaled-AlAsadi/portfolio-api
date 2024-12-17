from portfolio_api_app.serializers import LanguageSerializer
from portfolio_api_app.schemas import *
from portfolio_api_app.models import *
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def get_languages(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = getattr(user, 'portfolio', None)

    if not portfolio:
        return JsonResponse({'error': 'Portfolio not found for this user'},
                            status=404)

    language = Language.objects.filter(user=portfolio)
    user_serializer = LanguageSerializer(language, many=True)
    return Response(user_serializer.data)


@extend_schema(request=LanguageSerializer)
@api_view(['POST'])
def add_language(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio, created = Portfolio.objects.get_or_create(user=user)

    serializer = LanguageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=portfolio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=str)
@api_view(['DELETE'])
def delete_language(request, id):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = Portfolio.objects.get(user=user)

    language = get_object_or_404(Language, id=id, user=portfolio)

    language.delete()
    return Response({'description': 'Language deleted successfully.'})


@extend_schema(request=LanguageSerializer)
@api_view(['PUT'])
def update_language(request, id):
    user = request.user

    if not user.is_authenticated:
        return Response({'error': 'User not authenticated'},
                        status=status.HTTP_401_UNAUTHORIZED)

    portfolio = get_object_or_404(Portfolio,
                                  user=user)

    language = get_object_or_404(Language, id=id, user=portfolio)

    serializer = LanguageSerializer(language, data=request.data,
                                    partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
