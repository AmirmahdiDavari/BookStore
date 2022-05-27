from Book.models import Book
from Common.api import response, check_token
from Book.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class BookViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        user =check_token(request)
        queryset = Book.objects.all()
        username = request.user.id
        # print(username)
        print("________________________________")
        # print(user)
        serializer = BookSerializer(queryset, many=True)
        return Response({'____________'})

