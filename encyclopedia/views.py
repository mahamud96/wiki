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

def search(request):
    if request.method == "POST":
        article_search = request.POST['q']
        html_article = md_conversion(article_search)
        if html_article is not None:
            return render(request, "encyclopedia/entries.html", {
            "title": article_search,
            "article": html_article,
            })
        else:
            # substring search
            substr_search = util.list_entries()
            # substring result
            substr_result = []
            for entry in substr_search:
                if article_search.lower() in entry.lower():
                    substr_result.append(entry)
            return render(request, "encyclopedia/search.html",{
                "substr_result": substr_result
            })

def new_article(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newarticle.html")
    else:
        title = request.POST["title"]
        article = request.POST["article"]
        entry_title = md_conversion(title)
        if entry_title is not None:
            return render(request, "encyclopedia/errorpage.html",{
                "error_message":"This article already exists"
            })
        else:
            util.save_entry(title, article)
            html_article = md_conversion(title)
            return render(request, "encyclopedia/entries.html",{
                "title": title,
                "article": html_article,
            })

def edit_article(request):
    if request.method == "POST":
        title = request.POST['article_title']
        article = util.get_entry(title)
        return render(request, "encyclopedia/editarticle.html",{
            "title": title,
            "article": article,
        })

def save_changes(request):
    if request.method == "POST":
        title = request.POST['title']
        article = request.POST['article']
        util.save_entry(title, article)
        html_article = md_conversion(title)
        return render(request, "encyclopedia/entries.html",{
            "title": title,
            "article": html_article,
        })
