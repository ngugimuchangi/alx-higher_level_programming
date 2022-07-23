"""
    Print module
    Functions:
        text_indentation(text)
"""


def text_indentation(text):
    """
        Function splits string based on delimiters
        Args:
            text: text to split (str)
        Return: nothing
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for i in range(len(text)):
        if text[i] in ".?:":
            line = (line + text[i]).strip()
            print("{:s}\n".format(line))
            line = ""
        else:
            line = line + text[i]
    line = line.strip()
    if line != "":
        print(line, end="")
