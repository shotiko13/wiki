from django.shortcuts import redirect,render

from . import util

from markdown2 import Markdown


def mark(entry):
    return Markdown().convert(util.get_entry(entry)) if entry else None

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entry_md =  util.get_entry(entry)

    if entry_md != None:
        entry_h = Markdown().convert(entry_md)
        return render(request, "encyclopedia/entry.html", {
            "title" : entry,
            "entry": entry_h
        })

    return render(request, "encyclopedia/error.html", {
        "title" :entry
    })

def search(request):

    query = request.GET.get('q', '')

    entries = util.list_entries()

    if util.get_entry(query) is None:
        lst = []

        for entry in entries:
            if query.lower() in entry.lower():
                lst.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries":  lst,
            "search" : True,
            "query" :query,
        })


    return render(request, "encyclopedia/entry.html ", {
        "entry": mark(query)
    }) 
        




