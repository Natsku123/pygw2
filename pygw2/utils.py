def list_to_str(l: list, delimiter: str=","):
    """
    Convert list to string with delimiter.
    :param l: list
    :param delimiter: str=","
    :return: str
    """
    string = ""
    for item in l:
        if l.index(item) == len(l)-1:
            string += str(item)
        else:
            string += str(item) + delimiter

    return string
