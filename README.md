# A generator for context free grammar

- currently does not take into account repeated definitions, the second one will override the first. 

## Usage

Takes a grammar file (examples see `grammars` folders)

Generating the `grammar.py` file
```sh
python gen.py -g grammars/poetry-ch.gram
```

Running the flask server
```
python main.py
```