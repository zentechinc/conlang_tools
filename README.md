# conlang_tools (***clt***)

I'm writing a high-fantasy book and have had trouble making new words, phrases and names that fit well within the story

The solution to this seems to be building one or more "Constructed Language" (conlang) and using that language to help build convincing and feasible words 

However, keeping track of the words has become increasingly troublesome, and it is still onerous to build some of the names and phrases... hence this toolkit

My goal here is to build a Command Line Interface that will take a "Natural" language (like English) phrase, and translate that phrase into arbitrary conlang equivalents

For example:

```shell
> clt 'dire hound' -l somelang
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

The first version of this tool kit will do nothing more than direct word lookups and substitutions, but depending on the traction I make and my motivation I would like it to be significantly more advanced such that it will parse arbitrary natural languages and render the phrase in the constructed equivalents

A very rough version map looks something like this:
0. beta <- WE ARE HERE!
1. substitution - basically a multi-encoding word-valued substitution cypher tool
2. fuzzy - still a substitution library, but with 'fuzzy' substitution logic
    * for example: 'rudy fox'. 'rudy' may not have a direct match in the encoding language, so the library should attempt a best-fit match 
3. langFiles - a given input should be run through a target language's langFile so that an earnest semantic translation may be attempted

Additionally, once a language is registered, i.e. any word for the language is present in the wordlist, ***clt*** should help the user add any unknown equivalent words

Translations will take place using a langFile which acts as a sort of "driver" for any arbitrary language. Absence of a langFile for a language will result in a simple translation

Contributions and ideas are welcome!

--Ivan