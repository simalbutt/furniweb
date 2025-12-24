from rest_framework.response import Response
from rest_framework import status


class APIResponse:
    """
    Standard API response format for the entire project
    """

    @staticmethod
    def success(
        data=None,
        message="Success",
        status_code=status.HTTP_200_OK
    ):
        return Response(
            {
                "success": True,
                "message": message,
                "data": data
            },
            status=status_code
        )

    @staticmethod
    def error(
        message="Something went wrong",
        errors=None,
        status_code=status.HTTP_400_BAD_REQUEST
    ):
        return Response(
            {
                "success": False,
                "message": message,
                "errors": errors
            },
            status=status_code
        )

    @staticmethod
    def not_found(message="Not found", status_code=status.HTTP_404_NOT_FOUND):
        return Response(
            {
                "success": False,
                "message": message,
            },
            status=status_code
        )