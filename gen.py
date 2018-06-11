import textwrap
import re
import argparse

PATTERN_MAIN = re.compile(r'''((?:[^|"']|"[^"]*"|'[^']*')+)''')
PATTERN_SUB = re.compile(r'''((?:[^ "']|"[^"]*"|'[^']*')+)''')


def gen_expr(expr, tokens):
    total = len(tokens)
    output = []
    indent = "    "
    for index, token in enumerate(tokens):
        terms = []
        for term in token:
            term = term.strip()
            if term[0] == "\"" or term[0] == "\'":  # is string
                terms.append(term)
            else:
                terms.append("{}()".format(term))
        output.append(indent + "if {}/{} < r <= {}/{}:".format(index, total, index + 1, total))
        output.append(indent + indent + "return {}".format(" + ".join(terms)))
    return textwrap.dedent("""
def {}():
    r = random.random()
{}
    """.format(expr, '\n'.join(output)))
    # print(\"{}\")


def gen(infile, outfile):
    output = open(outfile, "w", encoding="utf-8")
    output.write("'''Warning: this is a generated file '''\n")
    output.write("import random\n")
    with open(infile, "r", encoding="utf-8") as f:
        data = f.readlines()
    for lineno, line in enumerate(data):
        if line == "\n" or line.startswith("#"):
            continue
        defn = line.split("->")
        if len(defn) != 2:
            raise Exception("Grammar is not valid")
        expr, tokens = [d.strip() for d in defn]
        tokens = PATTERN_MAIN.split(tokens)[1::2]
        tokens = [t.strip() for t in tokens]
        split_tokens = []
        for token in tokens:
            a = PATTERN_SUB.split(token)[1::2]
            split_tokens.append(a)
        output.write(gen_expr(expr, split_tokens))


def main(manual_args=None):
    parser = argparse.ArgumentParser(description='Options and Arguments')
    parser.add_argument('-g', metavar='Grammar file', help="Path of grammar file to use", dest="infile")
    parser.add_argument('-o', metavar='Output file', help="Path of output python grammar file", default="grammar.py", dest="outfile")
    args = parser.parse_args(manual_args)
    gen(args.infile, args.outfile)


if __name__ == "__main__":
    main()
