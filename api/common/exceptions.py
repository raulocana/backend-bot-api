from rest_framework.response import Response
from rest_framework.views import exception_handler


# https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is None:
        status_code = 500
        if hasattr(exc, "status_code"):
            status_code = exc.status_code
        response = Response({"error": exc.args[0]}, status=status_code)

    if response is not None:
        response.data["status_code"] = response.status_code

    return response
