
from drf_spectacular.views import (
    SpectacularAPIView,
     SpectacularRedocView,
      SpectacularSwaggerView)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    #AUTENTICAÇAO JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #DOCUMENTAÇÃO DA API SWAGGER
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(
        url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(
        url_name='schema'), name='redoc'),
    #MINHAS APPS
    path('usuario/', include('usuario.urls')),
    path('', include('produto.urls')),
    path('carrinho/', include('carrinho.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)