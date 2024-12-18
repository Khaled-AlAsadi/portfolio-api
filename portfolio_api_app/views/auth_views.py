from portfolio_api_app.errors import *
from rest_framework.response import Response
from portfolio_api_app.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView


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