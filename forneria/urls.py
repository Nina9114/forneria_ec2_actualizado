from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import CustomPasswordResetConfirmView
from rest_framework.routers import DefaultRouter
from shop.viewsets import ProductosViewSet, CategoriasViewSet

# Crear el router de DRF
router = DefaultRouter()
router.register(r'productos', ProductosViewSet, basename='producto')
router.register(r'categorias', CategoriasViewSet, basename='categoria')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-reset/confirmar/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('api/', include(router.urls)),  # Rutas de la API
    path('', include('shop.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
