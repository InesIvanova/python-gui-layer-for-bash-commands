import os


def execute(command) -> int:
    """
    :param command: bash command as a string
    :return: integer representing the exit code of the command
    """
    return os.system(command)
