from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView


router = DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'referrals'

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('redoc/', TemplateView.as_view(template_name='redoc.html', extra_context={'schema_url':'openapi-schema'}), name='redoc'),

]


