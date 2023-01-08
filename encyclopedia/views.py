from django.shortcuts import render
from markdown2 import Markdown

from . import util

def md_conversion(title):
    page = util.get_entry
    markdowner = Markdown()
    if title == None:
        return None
    else:
        return markdowner.convert(title)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

