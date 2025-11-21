from rest_framework import serializers
from .models import Productos, Categorias, Nutricional

class CategoriasSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Categorias"""
    class Meta:
        model = Categorias
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')

class NutricionalSerializer(serializers.ModelSerializer):
    """Serializador para información nutricional (anidado)"""
    class Meta:
        model = Nutricional
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'deleted_at')

class ProductosSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Productos"""
    # Campos de solo lectura para mostrar información relacionada
    categoria_nombre = serializers.CharField(source='Categorias_id.nombre', read_only=True)
    categoria_descripcion = serializers.CharField(source='Categorias_id.descripcion', read_only=True)
    
    # Información nutricional anidada (opcional)
    nutricional = NutricionalSerializer(source='Nutricional_id', read_only=True)
    
    class Meta:
        model = Productos
        fields = [
            'id',
            'nombre',
            'descripcion',
            'marca',
            'precio',
            'caducidad',
            'elaboracion',
            'tipo',
            'Categorias_id',
            'categoria_nombre',
            'categoria_descripcion',
            'stock_actual',
            'stock_minimo',
            'stock_maximo',
            'presentacion',
            'formato',
            'Nutricional_id',
            'nutricional',
            'creado',
            'modificado',
            'eliminado'
        ]
        read_only_fields = ('creado', 'modificado', 'eliminado')
