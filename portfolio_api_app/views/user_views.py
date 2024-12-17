from rest_framework_simplejwt.views import TokenObtainPairView
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework import status
from portfolio_api_app.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from portfolio_api_app.schemas import *
from django.http import HttpResponse, JsonResponse
from portfolio_api_app.models import *


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
