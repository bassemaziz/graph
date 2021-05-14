from django.test import TestCase
from django.urls import reverse, resolve
from rest_framework.test import APIClient
from graph.node.models import Node
import json


class ConnectNodeTestCase(TestCase):
    def setUp(self):
        Node.objects.create(from_node="A", to_node="C")
        self.client = APIClient()
        self.connect_node_url = reverse("connect_node")
        self.data = {"from_node": "A", "to_node": "B"}
        self.same_path_data = {"from_node": "A", "to_node": "C"}
        self.node_str = "A --> C"
        return super().setUp()

    def test_connect_node_post_data(self):
        response = self.client.post(self.connect_node_url, self.data)
        self.assertEquals(response.status_code, 201)

    def test_connect_node_post_same_path_data(self):
        response = self.client.post(self.connect_node_url, self.same_path_data)
        self.assertEquals(response.status_code, 400)

    def test_node_model_str_function_return(self):
        node = Node.objects.get(from_node="A", to_node="C")
        self.assertEquals(node.__str__(), self.node_str)


class GetShortestPathTestCase(TestCase):
    def setUp(self):
        Node.objects.bulk_create(
            [
                Node(from_node="A", to_node="B"),
                Node(from_node="A", to_node="E"),
                Node(from_node="A", to_node="C"),
                Node(from_node="B", to_node="D"),
                Node(from_node="B", to_node="E"),
                Node(from_node="C", to_node="F"),
                Node(from_node="C", to_node="G"),
                Node(from_node="D", to_node="E"),
            ]
        )
        self.client = APIClient()
        self.path_url = reverse("path")
        self.data = "?from_node=A&to_node=D"
        self.not_connected_node_data = "?from_node=A&to_node=Z"
        self.same_path_data = "?from_node=A&to_node=A"
        self.wrong_param_data = "?from_bassem=A&to_khaled=A"
        self.success_result = {"success": True, "path": "A, B, D"}
        return super().setUp()

    def test_get_shortest_path(self):
        response = self.client.get(self.path_url + self.data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, self.success_result)  # type: ignore

    def test_get_shortest_path_not_connected_node(self):
        response = self.client.get(self.path_url + self.not_connected_node_data)
        self.assertEquals(response.status_code, 400)

    def test_get_shortest_path_same_path_data(self):
        response = self.client.get(self.path_url + self.same_path_data)
        self.assertEquals(response.status_code, 400)

    def test_get_shortest_path_wrong_param_data(self):
        response = self.client.get(self.path_url + self.wrong_param_data)
        self.assertEquals(response.status_code, 400)
