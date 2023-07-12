from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .pagination import MyCustomPagination


class BookLists(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    pagination_class=MyCustomPagination

class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class=BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes=[TokenAuthentication]

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    def post(self,request,*args,**kwargs):
        response=super().post(request,*args,**kwargs)
        return Response({"message":"book created"}, status=200)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def patch(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.author != request.user:
                raise Exception("User is not the author of the book")
            return super().patch(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})


    def put(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.author != request.user:
                raise Exception("User is not the author of the book")
            return super().put(request, *args, **kwargs)
        except Exception as e:
            return Response({'error': str(e)})


    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.author != request.user:
                raise Exception("User is not the author of the book")
            response = super().delete(request, *args, **kwargs)
            return Response({'message': 'Book deleted'})
        except Exception as e:
            return Response({'error': str(e)})
    
    
