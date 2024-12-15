from drf_spectacular.utils import OpenApiExample, OpenApiResponse

# Example for a health check response
class HealthCheckSchemas:
    RESPONSE = {
        "type": "object",
        "properties": {
            "status": {"type": "string", "example": "healthy"},
            "message": {"type": "string", "example": "The application is running."}
        }
    }