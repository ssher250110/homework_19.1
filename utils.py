from settings import INDEX_HTML


def index_html_content():
    with open(INDEX_HTML, encoding="utf-8") as file:
        return file.read()
