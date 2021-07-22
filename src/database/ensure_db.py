def ensure_langdb(con, cur):
    print('<------- inside: ensure_langdb ------->')

    cur.execute('''CREATE TABLE if not exists 
        con_languages (
            language_name text primary key
        )''')

    cur.execute('''CREATE TABLE if not exists 
        words_natural (
            natural_word text,
            definition text
        )''')

    cur.execute('''CREATE TABLE if not exists 
        words_constructed (
            constructed_word text,
            langauge_name text,
            translation text,
            FOREIGN KEY(language_name) REFERENCES con_languages(language_name)
        )''')

    cur.execute('''CREATE TABLE if not exists 
        nat_to_con (
            nat_id integer,
            con_id integer,
            con_lang text,
            FOREIGN KEY(nat_id) REFERENCES words_natural(rowid),
            FOREIGN KEY(con_id) REFERENCES words_constructed(rowid),
            FOREIGN KEY(con_lang) REFERENCES con_languages(language_name)
        )''')
