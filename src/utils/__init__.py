import argparse


def get_arguments():
    print('-------> inside: get_arguments')
    parser = argparse.ArgumentParser(
        prog='clt',
        description='a tool kit for working with conlangs',
        epilog='Hail to you, Champion!',
    )

    parser.version = '1.0'

    parser.add_argument('term',
                        metavar='TERM',
                        help='a word or group of words comprising the subject to be translated')

    parser.add_argument('-l',
                        '--lang',
                        default='english',
                        help='the incoming language from which the input should be translated')

    parser.add_argument('-o',
                        '--output',
                        default='all',
                        help='the language to which the input term should be translated')

    parser.add_argument('-a',
                        '--add',
                        action='store_true',
                        help='add a word to a language dictionary')

    return parser.parse_args()
