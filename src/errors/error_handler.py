from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityEntityError

def handler_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityEntityError):
        # enviar para um log
        # ou enviar para um email de notificação
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
