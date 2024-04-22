from django.urls import path, include
from rest_framework_nested import routers

from . import views
# from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
router = routers.DefaultRouter()
router.register("books", views.BookViewSet, "book")
router.register("authors", views.AuthorViewSet, "author")
# router.register("reviews", views.ReviewViewSet, "review")
print(router.urls)

review_router = routers.NestedDefaultRouter(router, "books", lookup='book')
review_router.register("reviews", views.ReviewViewSet,'review')

urlpatterns = router.urls + review_router.urls

# urlpatterns = router.urls

# urlpatterns = [
#     # path('books/', views.BookList.as_view(), name='books'),
#     # path('books/<int:pk>/', views.BookDetails.as_view(), name='book_details'),
#     path('authors/', views.AuthorList.as_view()),
#     path('authors/<int:pk>', views.AuthorDetails.as_view(), name='author_detail'),
#     path("", include(router.urls))
# ]
