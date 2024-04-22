import segno
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author, Review
from .pagination import DefaultPagination
from .serializers import BookSerializer, AuthorSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
class BookViewSet(ModelViewSet):
    pagination_class = DefaultPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    # serializer_class = ReviewSerializer
    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_context(self):
        return {'book_pk': self.kwargs['book_pk']}


class Book_List(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True,
                                    context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


"=========================================================================="


class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_serializer_context(self):
        return {"request": self.request}


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#
#
#     elif request.method == 'POST':
#


# @api_view()
# def book_detail(request, id):
#     try:
#         book = Book.objects.get(id=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
"================================================================="


class Book_Details(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        book = get_object_or_404(Book, id=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def book_detail(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == 'GET':
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
"=============================================================================="


class AuthorList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class AuthorList(APIView):
#     def get(self, request):
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
"=================================================================================="


class AuthorDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Author_Details(APIView):
    def get(self, request, pk):
        author = get_object_or_404(Author, id=pk)
        serializer = AuthorSerializer(author)
        author_qrcode = segno.make_qr("welcome to Django")
        author_qrcode.save("welcome.png")
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        author = get_object_or_404(Author, id=pk)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, pk):
        author = get_object_or_404(Author, id=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'PUT', 'DELETE'])
# def author_details(request, pk):
#     author = get_object_or_404(Author, id=pk)
#
#     if request.method == 'GET':
#         author = get_object_or_404(Author, id=pk)
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr("welcome to Django")
#         author_qrcode.save("welcome.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "DELETE":
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
