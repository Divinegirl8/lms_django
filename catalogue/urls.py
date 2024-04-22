from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("books", views.BookViewSet, "book")
router.register("authors", views.AuthorViewSet, "author")
router.register("reviews", views.ReviewViewSet, "review")
print(router.urls)

urlpatterns = router.urls

# urlpatterns = [
#     # path('books/', views.BookList.as_view(), name='books'),
#     # path('books/<int:pk>/', views.BookDetails.as_view(), name='book_details'),
#     path('authors/', views.AuthorList.as_view()),
#     path('authors/<int:pk>', views.AuthorDetails.as_view(), name='author_detail'),
#     path("", include(router.urls))
# ]
