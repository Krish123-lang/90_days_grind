from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    image=serializers.ImageField(required=False, allow_null=True)
    
    class Meta:
        model=Todo
        fields=['id', 'title', 'description', 'priority', 'completed', 'created_at', 'updated_at', 'image']
        read_only_fields=['created_at', 'updated_at', 'user']