from portfolio_api_app.serializers import WorkExperinceSerializer
from portfolio_api_app.models import WorkExperince,Portfolio
from rest_framework.decorators import api_view
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from portfolio_api_app.schemas.work_schema import Schemas


@extend_schema(
    summary=Schemas.WorkSchemaGet["summary"],
    description=Schemas.WorkSchemaGet["description"],
    responses=Schemas.WorkSchemaGet["responses"],
)
@api_view(['GET'])
def get_work_experinces(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = getattr(user, 'portfolio', None)

    if not portfolio:
        return JsonResponse({'error': 'Portfolio not found for this user'},
                            status=404)

    work_experiences = WorkExperince.objects.filter(portfolio=portfolio)
    user_serializer = WorkExperinceSerializer(work_experiences, many=True)
    return Response(user_serializer.data)


@extend_schema(
    summary=Schemas.WorkSchemaPost["summary"],
    description=Schemas.WorkSchemaPost["description"],
    responses=Schemas.WorkSchemaPost["responses"],
    request=Schemas.WorkSchemaPost["request"],
)
@api_view(['POST'])
def create_work_experince(request):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio, created = Portfolio.objects.get_or_create(user=user)

    serializer = WorkExperinceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(portfolio=portfolio)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    summary=Schemas.WorkSchemaDelete["summary"],
    description=Schemas.WorkSchemaDelete["description"],
    responses=Schemas.WorkSchemaDelete["responses"],
    request=Schemas.WorkSchemaDelete["request"],
)
@api_view(['DELETE'])
def delete_work_experince(request, id):
    user = request.user

    if not user.is_authenticated:
        return JsonResponse({'error': 'User not authenticated'}, status=401)

    portfolio = Portfolio.objects.get(user=user)

    work_experience = get_object_or_404(WorkExperince, id=id,
                                        portfolio=portfolio)

    work_experience.delete()
    return Response({'description': 'Work experience deleted successfully.'})


@extend_schema(
    summary=Schemas.WorkSchemaPut["summary"],
    description=Schemas.WorkSchemaPut["description"],
    responses=Schemas.WorkSchemaPut["responses"],
    request=Schemas.WorkSchemaPut["request"],
)
@api_view(['PUT'])
def update_work_experince(request, id):
    user = request.user

    if not user.is_authenticated:
        return Response({'error': 'User not authenticated'},
                        status=status.HTTP_401_UNAUTHORIZED)

    portfolio = get_object_or_404(Portfolio,
                                  user=user)

    work_experience = get_object_or_404(WorkExperince, id=id,
                                        portfolio=portfolio)

    serializer = WorkExperinceSerializer(work_experience, data=request.data,
                                         partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
