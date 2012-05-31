
class OerpModel:
    """
    Map results of queries to object, for easy manipulation
    """

    def __init__(self, module, data):
        self.object = type(module, (), data)
