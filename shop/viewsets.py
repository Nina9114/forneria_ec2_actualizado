from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Productos, Categorias
from .serializers import ProductosSerializer, CategoriasSerializer

class CategoriasViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Categorías.
    """
    queryset = Categorias.objects.filter(deleted_at__isnull=True)
    serializer_class = CategoriasSerializer
    
    def destroy(self, request, *args, **kwargs):
        """Soft delete: marcar como eliminado en lugar de borrar físicamente"""
        instance = self.get_object()
        instance.deleted_at = timezone.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductosViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar Productos.
    """
    queryset = Productos.objects.filter(eliminado__isnull=True)
    serializer_class = ProductosSerializer
    
    def get_queryset(self):
        """
        Permite filtrar productos por categoría
        Ejemplo: /api/productos/?categoria=1
        """
        queryset = Productos.objects.filter(eliminado__isnull=True)
        categoria = self.request.query_params.get('categoria', None)
        if categoria is not None:
            queryset = queryset.filter(Categorias_id=categoria)
        return queryset
    
    def destroy(self, request, *args, **kwargs):
        """Soft delete: marcar como eliminado en lugar de borrar físicamente"""
        instance = self.get_object()
        instance.eliminado = timezone.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
