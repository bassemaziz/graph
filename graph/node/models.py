from django.db import models


class Node(models.Model):
    """
    Node model holds all nodes connected to each other
    """

    from_node = models.CharField(max_length=1)
    to_node = models.CharField(max_length=1)

    class Meta:
        """
        db constrain that not allow to store same connected nodes twice
        """

        unique_together = [["from_node", "to_node"]]

    def __str__(self):
        return self.from_node + " --> " + self.to_node
