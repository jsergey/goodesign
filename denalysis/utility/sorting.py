from operator import itemgetter


def dict_by_value(dict):
    return sorted(dict.items(), key=itemgetter(1))
