
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Secure API')
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'swagger/', schema_view),  # http://localhost:8000/swagger
    path('appone/', include('appone.urls')),
    path('api-auth', include('rest_framework.urls')),
    path('api/token',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]
