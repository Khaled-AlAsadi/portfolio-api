from drf_spectacular.utils import OpenApiExample, OpenApiResponse
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes


class Schemas:
    UNAUTHORIZED_RESPONSE = OpenApiResponse(
        description="Unauthorized access",

    )
