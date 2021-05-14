from rest_framework import serializers

from graph.node.models import Node


class NodeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ["from_node", "to_node"]


class NodeGetPathSerializer(serializers.Serializer):
    from_node = serializers.CharField(max_length=1)
    to_node = serializers.CharField(max_length=1)
