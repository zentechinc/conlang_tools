from src.database.utils import print_table_from_cursor

def match_terms(invoke, printTable = True):
    print('<------- marker 1 ------->')

    query = "SELECT * FROM term_matches WHERE term IN (%s)" % ','.join('?' * len(invoke.arguments.term_split))
    invoke.cursor.execute(query, invoke.arguments.term_split)

    if printTable:
        print_table_from_cursor(invoke.cursor)
