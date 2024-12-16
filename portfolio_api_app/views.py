from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse

from .models import CustomUser
from .schemas import *
from .errors import ERROR_MESSAGES
from .serializers import *


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            error_response = {
                "details": ERROR_MESSAGES['InvalidCredential']
            }
            return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
            if not user.check_password(password):
                error_response = {
                    "details": ERROR_MESSAGES['WrongPassword']
                }
                return Response(error_response,
                                status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            error_response = {
                "details": ERROR_MESSAGES['EmailNotFound']
            }
            return Response(error_response,
                            status=status.HTTP_401_UNAUTHORIZED)

        try:
            response = super().post(request, *args, **kwargs)
            return response
        except Exception as e:
            error_response = {
                "details": ERROR_MESSAGES['InternalError']
            }
            return Response(error_response,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@extend_schema(
    summary="Get User Details",
    description="Returns authenticated user details. Requires Authorization.",
    responses={
        200: CustomUserSerializer,
        401: Schemas.UNAUTHORIZED_RESPONSE,
    }
)
@api_view(['GET'])
def get_user(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    user_serializer = CustomUserSerializer(user)
    return Response(user_serializer.data)


@extend_schema(request=PortfolioSerializer)
@api_view(['PATCH'])
def update_portfolio(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    try:
        portfolio, created = Portfolio.objects.get_or_create(user=user)

        serializer = PortfolioSerializer(portfolio,
                                         data=request.data, partial=True)

        if serializer.is_valid():
            # Save the updated portfolio
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    except Portfolio.DoesNotExist:
        return JsonResponse({'error': 'Portfolio not found'}, status=404)


@api_view(['GET'])
def get_work_experinces(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = getattr(user, 'portfolio', None)

    if not portfolio:
        return JsonResponse({'error': 'Portfolio not found for this user'},
                            status=404)

    work_experiences = WorkExperince.objects.filter(user=portfolio)
    user_serializer = WorkExperinceSerializer(work_experiences, many=True)
    return Response(user_serializer.data)


@extend_schema(request=WorkExperinceSerializer)
@api_view(['POST'])
def create_work_experince(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio, created = Portfolio.objects.get_or_create(user=user)

    serializer = WorkExperinceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=portfolio)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=str)
@api_view(['DELETE'])
def delete_work_experince(request, id):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = Portfolio.objects.get(user=user)

    work_experience = get_object_or_404(WorkExperince, id=id, user=portfolio)

    work_experience.delete()
    return Response({'description': 'Work experience deleted successfully.'})


@extend_schema(request=WorkExperinceSerializer)
@api_view(['PUT'])
def update_work_experince(request, id):
    user = request.user

    if not user.is_authenticated:
        return Response({'error': 'User not authenticated'},
                        status=status.HTTP_401_UNAUTHORIZED)

    portfolio = get_object_or_404(Portfolio,
                                  user=user)

    work_experience = get_object_or_404(WorkExperince, id=id, user=portfolio)

    serializer = WorkExperinceSerializer(work_experience, data=request.data,
                                         partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
