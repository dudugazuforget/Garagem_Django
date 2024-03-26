from rest_framework.serializers import ModelSerializer
from core.models import Acessorios
class AcessoriosSerializer(ModelSerializer):
    class Meta:
        model = Acessorios
        fields = "__all__"
        max_length = 100


