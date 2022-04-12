def black(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;30;1m{c}\033[m'
    if reverse:
        return f'\033[1;30;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;30;7;1m{c}\033[m'
    else:
        return f'\033[1;30m{c}\033[m'


def red(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;31;1m{c}\033[m'
    if reverse:
        return f'\033[1;31;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;31;7m{c}\033[m'
    else:
        return f'\033[1;31m{c}\033[m'


def green(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;32;1m{c}\033[m'
    if reverse:
        return f'\033[1;32;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;32;7m{c}\033[m'
    else:
        return f'\033[1;32m{c}\033[m'


def yellow(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;33;1m{c}\033[m'
    if reverse:
        return f'\033[1;33;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;33;7m{c}\033[m'
    else:
        return f'\033[1;33m{c}\033[m'


def blue(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;34;1m{c}\033[m'
    if reverse:
        return f'\033[1;34;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;34;7m{c}\033[m'
    else:
        return f'\033[1;34m{c}\033[m'


def magenta(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;35;1m{c}\033[m'
    if reverse:
        return f'\033[1;35;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;35;7m{c}\033[m'
    else:
        return f'\033[1;35m{c}\033[m'


def cyan(c, bold=False, reverse=False):
    if bold:
        return f'\033[1;36;1m{c}\033[m'
    if reverse:
        return f'\033[1;36;7m{c}\033[m'
    elif bold and reverse:
        return f'\033[1;36;7m{c}\033[m'
    else:
        return f'\033[1;36m{c}\033[m'
