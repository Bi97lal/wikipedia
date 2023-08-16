from django.shortcuts import render
from markdown2 import Markdown
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdown = Markdown()
    if content is None:
        return None
    else:
        return markdown.convert(content)

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content is None:
        return render(request, "encyclopedia/error.html", {
            "message":"Sorry, there was an error! "
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content
        })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

