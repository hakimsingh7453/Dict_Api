from rest_framework import fields, serializers
from .models import dicts

class dict_serializers(serializers.ModelSerializer):
    class Meta:
        model=dicts
        fields='__all__'