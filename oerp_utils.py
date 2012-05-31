
class OerpUtils:

    @staticmethod
    def translate_to_search_domain(args):
        """
        Converts the kwargs to the weird openerp notation
        """

        domain_search = []

        for key, value in args.iteritems():
            domain_search.append((key, '=', value))

        return domain_search