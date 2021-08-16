"""other utilities"""

# ------ modules ------
import os
import sys
import argparse


# ------ classes -------
class VariableNotFoundError(ValueError):
    pass


class FileError(ValueError):
    pass


class colr:
    WHITE = '\033[0;97m'
    WHITE_B = '\033[1;97m'
    YELLOW = '\033[0;33m'
    YELLOW_B = '\033[1;33m'
    RED = '\033[0;31m'
    RED_B = '\033[1;31m'
    BLUE = '\033[0;94m'
    BLUE_B = '\033[1;94m'
    CYAN = '\033[0;36m'
    CYAN_B = '\033[1;36m'
    ENDC = '\033[0m'  # end colour


class AppArgParser(argparse.ArgumentParser):
    """
    This is a sub class to argparse.ArgumentParser.
    Purpose
        The help page will display when (1) no argumment was provided, or (2) there is an error
    """


def error(self, message, *lines):
    string = "\n{}ERROR: " + message + "{}\n" + \
        "\n".join(lines) + ("{}\n" if lines else "{}")
    print(string.format(colr.RED_B, colr.RED, colr.ENDC))
    self.print_help()
    sys.exit(2)


# ------ functions -------
def addBoolArg(parser, name, help, input_type, default=False):
    """
    Purpose\n
        autmatically add a pair of mutually exclusive boolean arguments to the
        argparser
    Arguments\n
        parser: a parser object.\n
        name: str. the argument name.\n
        help: str. the help message.\n
        input_type: str. the value type for the argument\n
        default: the default value of the argument if not set\n
    """
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name,
                       action='store_true', help=input_type + '. ' + help)
    group.add_argument('--no-' + name, dest=name,
                       action='store_false', help=input_type + '. ''(Not to) ' + help)
    parser.set_defaults(**{name: default})


def error(message, *lines):
    """
    stole from: https://github.com/alexjc/neural-enhance
    """
    string = "\n{}ERROR: " + message + "{}\n" + \
        "\n".join(lines) + ("{}\n" if lines else "{}")
    print(string.format(colr.RED_B, colr.RED, colr.ENDC))
    sys.exit(2)


def warn(message, *lines):
    """
    stole from: https://github.com/alexjc/neural-enhance
    """
    string = '\n{}WARNING: ' + message + '{}\n' + '\n'.join(lines) + '{}\n'
    print(string.format(colr.YELLOW_B, colr.YELLOW, colr.ENDC))


def csvPath(string):
    # # (inactive) below: relative to the script dir
    # script_path = os.path.dirname(__file__)
    # full_path = os.path.normpath(os.path.join(script_path, string))

    # below: relative to working dir
    # use os.path.expanduser to understand "~"
    full_path = os.path.normpath(os.path.abspath(os.path.expanduser(string)))

    if os.path.isfile(full_path):
        # return full_path
        _, file_ext = os.path.splitext(full_path)
        if file_ext != '.csv':
            raise ValueError('Input file needs to be .csv type.')
        else:
            return full_path
    else:
        raise ValueError('Invalid input file or input file not found.')


def fileDir(string):
    # # (inactive) below: relative to the script dir
    # script_path = os.path.dirname(__file__)
    # full_path = os.path.normpath(os.path.join(script_path, string))

    # below: relative to working dir
    # use os.path.expanduser to understand "~"
    full_path = os.path.normpath(os.path.abspath(os.path.expanduser(string)))

    if os.path.isdir(full_path):
        return full_path
    else:
        raise ValueError('Directory not found.')


def flatten(x): return [item for sublist in x for item in sublist]
