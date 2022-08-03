#!/usr/bin/python3
""" Search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """ Function to search for a particular search pattern and append
        new string at the line with the search pattern
        Args:
            filename(str): name of the file
            search_string(str): search pattern
            new_string(str): content to append
        Return: nothing
    """

    with open(filename, 'r', encoding='UTF8') as f:
        lines = []
        line = f.readline()
        while line:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
            line = f.readline()
    with open(filename, 'w', encoding='UTF8') as f:
        f.writelines(lines)
