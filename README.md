# conlang_tools

I'm writing a high-fiction book and have had trouble making new words, phrases and names that fit well within the story.

The solution to this seems to be building a one or more "Constructed Language" (conlang) and using those languages to help build convincing and believable words. 

However, it seems like keeping track of the words has become increasingly troublesome, and it is still onerous to build some of the names and phrases... hence this toolkit

My goal here is to build a Command Line Interface that will take a "Natural" language (like English) phrase, and translate that phrase into arbitrary conlang equivalents.

For example:

```shell
clt 'dire hound' -l somelang
```

...will return something to the effect...

```shell
+------------+---------------+
| language   | translation   |
+============+===============+
| english    | dire hound    |
+------------+---------------+
| somelang   | tan hari      |
+------------+---------------+
```

The first version of this tool kit do nothing more than direct word lookups and translations, but depending on my traction and motivation I would like it to be significantly more advanced such that it will parse arbitrary natural languages and render the phrase in the constructed equivalent

Additionally, once a language is registered, i.e. any word for the language is present in the wordlist, clt should help the user add any unknown equivalent words 

Contributions and ideas are welcome!

--Ivan