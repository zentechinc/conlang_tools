import argparse


def get_arguments():
    print('<------- inside: get_arguments ------->')
    parser = argparse.ArgumentParser(
        prog='clt',
        description='a tool kit for working with conlangs',
        epilog='Hail to you, Champion!',
    )

    parser.version = '1.0'

    parser.add_argument('input',
                        metavar='INPUT',
                        help='a group of words comprising the subject to be translated')

    parser.add_argument('-l',
                        '--lang',
                        help='the specific language to which the input should be translated')

    parser.add_argument('-a',
                        '--add',
                        action='store_true',
                        help='add a word to a language dictionary')

    return parser.parse_args()
