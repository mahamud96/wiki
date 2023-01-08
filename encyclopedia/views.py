from django.shortcuts import render
from markdown2 import Markdown

from . import util

def md_conversion(title):
    article = util.get_entry(title)
    markdowner = Markdown()
    if article == None:
        return None
    else:
        return markdowner.convert(article)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    html_article = md_conversion(title)
    if html_article == None:
        return render(request, "encyclopedia/errorpage.html", {
            "error_message": "This article does not exist"
        })
    else:
        return render(request, "encyclopedia/entries.html", {
            "title": title,
            "article": html_article,
        })
