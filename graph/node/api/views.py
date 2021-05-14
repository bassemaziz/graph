from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .serializers import NodeModelSerializer, NodeGetPathSerializer
from graph.node.models import Node
from graph.utils.build_graph import build_graph
from graph.utils.get_short_path import breadth_first_search


class ConnectNodeAPI(APIView):
    """Connect Node endpoint
    Example :
    [POST] /connect-node

    {
        "from_node":"A",
        "to_node":"B"
    }
    """

    permission_classes = [AllowAny]
    serializer_class = NodeModelSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetShortestPathAPI(APIView):
    """Get shortest path endpoint
    Example :
    [GET] /path?from_node=A&to_node=D
    """

    permission_classes = [AllowAny]
    serializer_class = NodeGetPathSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(data=request.GET)
        if serializer.is_valid():
            nodes = Node.objects.all().values_list("from_node", "to_node")
            graph = build_graph(list(nodes))
            short_path = breadth_first_search(
                graph,
                serializer.validated_data["from_node"],
                serializer.validated_data["to_node"],
            )
            if short_path["success"] is True:
                return Response(short_path, status=status.HTTP_200_OK)
            if short_path["success"] is False:
                return Response(short_path, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
