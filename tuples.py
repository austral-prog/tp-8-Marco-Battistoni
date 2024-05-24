"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """
    
    a = coordinate[0]
    b = coordinate[1]
    tuple = (a, b)
    return tuple


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """
    tuple = azara_record + rui_record
    rui_coordinates = rui_record[1][0] + rui_record[1][1] 
    azara_coordinates = azara_record[1][0:]
    if rui_coordinates == azara_coordinates:
        return tuple
    else:
        return "not a match"
