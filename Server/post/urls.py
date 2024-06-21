from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserRegistrationView, UserLoginView,
                    EmployerViewSet, VacancyViewSet, CommentViewSet,
                    PublicationViewSet, ProfileView)

router = DefaultRouter()
router.register(r'employers', EmployerViewSet)
router.register(r'vacancies', VacancyViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include(router.urls)),
]
