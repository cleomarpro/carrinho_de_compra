
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_e_user/', include('login_e_user.urls')),
    path('', include('produto.urls')),
    path('carrinho/', include('carrinho.urls')),
]
