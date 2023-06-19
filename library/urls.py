from django.urls import path, include
from rest_framework.routers import DefaultRouter
from libraryAPI import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
router.register(r'author', views.AuthorViewSet, basename="author")
router.register(r'publisher', views.PublisherViewSet, basename="publisher")
router.register(r'book', views.BookViewSet, basename="book")


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
