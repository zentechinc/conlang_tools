def ensure_langdb(con, cur):
    print('<------- inside: ensure_langdb ------->')

    cur.execute('''CREATE TABLE if not exists 
        languages (
            language_name text PRIMARY KEY
        )''')

    cur.execute('''CREATE TABLE if not exists 
            dictionary_parts (
                part text PRIMARY KEY
            )''')

    cur.execute('''CREATE TABLE if not exists 
        dictionary (
            term text,
            language text ,
            class text,
            definitions text,
            plurality text,
            PRIMARY KEY (term, language, class),
            FOREIGN KEY (language) REFERENCES languages(language_name),
            FOREIGN KEY(class) REFERENCES dictionary_parts(part)
        )''')

    cur.execute('''CREATE TABLE if not exists 
        term_matches (
            term text,
            language text,
            class text,
            matching_term text,
            matching_language text,
            primary key (term, language, class),
            FOREIGN KEY(language) REFERENCES languages(language_name),
            FOREIGN KEY(matching_language) REFERENCES languages(language_name),
            FOREIGN KEY(term,language, class) REFERENCES dictionary(term,language, class),
            FOREIGN KEY(matching_term, matching_language, class) REFERENCES dictionary(term,language, class)
        )''')

    # cur.execute('''CREATE TABLE if not exists
    #     nat_to_con (
    #         nat_id integer,
    #         con_id integer,
    #         con_lang text,
    #         FOREIGN KEY(nat_id) REFERENCES words_natural(rowid),
    #         FOREIGN KEY(con_id) REFERENCES words_constructed(rowid),
    #         FOREIGN KEY(con_lang) REFERENCES con_languages(language_name)
    #     )''')
