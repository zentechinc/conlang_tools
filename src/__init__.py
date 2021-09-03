from src.database.utils import print_table_from_cursor, print_table_from_invoke
from src.utils.classes import Matched_Entry
import json


def match_terms(invoke, printTable=True):
    print('-------> inside: match_terms')
    term_list = invoke.arguments.term_split

    query = "SELECT * FROM term_matches WHERE term IN (%s) and language = %s" % (
        ','.join('?' * len(invoke.arguments.term_split)), '?')

    term_list.append(invoke.arguments.lang)
    invoke.execute(query, term_list)

    if printTable:
        print_table_from_invoke(invoke)


def map_terms_to_dictionary(invoke):
    print('-------> inside: map_terms_to_dictionary')
    records = invoke.mrr()
    attributes = invoke.mra()

    for record in records:
        print('-------> record: {}'.format(record))
        if record[0] not in invoke.terms:
            invoke.terms[record[0]] = {
                'matches': {}
            }

        # for index, attribute_name in enumerate(attributes[2:]):
        #     print(attribute_name)
        
        invoke.terms[record[0]]['class'] = record[2]
        
        print('<------- marker 1 ------->')
        print('-------> json.dumps(invoke.__dict__): {}'.format(json.dumps(invoke.__dict__)))
        # invoke.matches[record[0]][record[1]] = build_json_dictonary_entry(invoke, record, attributes)


def build_json_dictonary_entry(invoke, term_match, attributes):
    print('-------> term_match: {}'.format(term_match))
    dict_entry = {
        'term': ''
    }

    matched = Matched_Entry(attributes, term_match)
    print('-------> json.dumps(matched.__dict__): {}'.format(json.dumps(matched.__dict__)))
    query = 'select term, definitions, class from main.dictionary where term = ? and language = ?;'
    params = [term_match[0], term_match[1]]
    invoke.execute(query, params)

    mrr = invoke.mrr()
    matched.definition = mrr[0][1]
    return json.dumps(matched.__dict__)
