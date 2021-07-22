from tabulate import tabulate


def attributes_and_records_from_cursor(cursor):
    attributes = [description[0] for description in cursor.description]
    records = cursor.fetchall()

    return attributes, records


def print_table_from_cursor(cursor):
    attributes, records = attributes_and_records_from_cursor(cursor)
    print(tabulate(records, attributes, tablefmt="grid"))