from flask import Flask, render_template, abort
import grammar as gr
import random
import time
import os

app = Flask(__name__)


def uniqid():
    return hex(int(time.time() * 10000000))[2:]


def clean_poem(poetry):
    poetry = poetry.strip()
    poetry = poetry.replace("\n\n\n", "\n\n")
    poetry = poetry.replace("一样一样", "一样")
    lines = poetry.split("\n")
    trimmed_lines = []
    for line in lines:
        if line == "\n" or len(line) <= 20:
            trimmed_lines.append(line)
        else:  # line too long, split the line
            line_length = len(line)
            first_len = random.randint(line_length // 4, 3 * line_length // 4)
            trimmed_lines.append(line[:first_len])
            trimmed_lines.append(line[first_len:])

    poetry = "\n".join(trimmed_lines)
    if poetry[-1] in ["，"]:  # ends with non-terminating punctuation
        terminating = ["。", "！", "？", ""]
        poetry = poetry[:-1] + random.choice(terminating)
    return poetry


@app.route('/')
def home():
    poetry = clean_poem(gr.top())
    poetry_html = poetry.replace("\n", "<br>")
    poemid = uniqid()

    # write to file
    os.makedirs("poems", exist_ok=True)
    with open(os.path.join("poems", poemid + ".txt"), "w", encoding="utf-8") as f:
        f.write(poetry)

    return render_template(
        'home.html',
        poetry=poetry_html,
        poem_id=poemid,
        single=False,
    )


@app.route('/poem/<poemid>')
def get_poem(poemid):
    filename = os.path.join("poems", poemid + ".txt")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            poetry = f.read()
    except FileNotFoundError:
        abort(404)
    poetry_html = poetry.replace("\n", "<br>")
    return render_template(
        "home.html",
        poetry=poetry_html,
        poem_id=poemid,
        single=True,
    )


@app.route('/poems')
def list_poems():
    poemids = []
    for file in os.listdir("poems"):
        poemid = file.rstrip(".txt")
        poemids.append(poemid)
    return render_template(
        "list.html",
        poem_ids=poemids
    )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
