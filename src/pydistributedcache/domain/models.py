class Node:
    """
    Double linked list implementation
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
