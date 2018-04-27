from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'teachers', views.TeacherViewSet)
router.register(r'register', views.RegisterViewSet)
router.register(r'level', views.LevelViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls))
]
