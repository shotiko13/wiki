from django.shortcuts import render

from . import util

from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    entry_md =  util.get_entry(entry)

    if entry_md != None:
        entry_h = Markdown().convert(entry.md)
        return render(request, "encyclopedia/entry.html", {
            "title" : entry,
            "entry": entry_h
        })

    return render(request, "encyclopedia/error.html", {
        "title" :entry
    })

