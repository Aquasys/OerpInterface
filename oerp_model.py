
class OerpModel:
    """
    Map results of queries to object, for easy manipulation
    """

    def __init__(self, module, data):
        self.object = type(module, (), data)


    def to_dict(self):
        """
        We cannot pass the object as is
        So we convert to a dict
        """

        object_dict = {}

        for attr, value in self.object.__dict__.iteritems():
            if attr[:2] == "__":
                #We don't want the __name__ etc
                pass
            else:
                object_dict[attr] = value

        return object_dict
