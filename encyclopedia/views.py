from django.shortcuts import redirect,render

from . import util
from random import choice 
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
            if query in entry.lower():
                lst.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries":  lst,
            "search" : True,
            "query" :query,
        })

    
    return render(request, "encyclopedia/entry.html ", {
        "entry": mark(query)
    }) 
        

def gotoPage(request):

    return render(request, "encyclopedia/newpage.html")


def savepage(request):
    if request.method == 'POST':
        title = request.POST['newpagetitle']
        txt = "#"+title+"\n\n"+request.POST['newpagetext']
        if title == "":
            return render(request, "encyclopedia/newpage.html")
        if title in util.list_entries():
            return render(request , "encyclopedia/exists.html", {
                "query" : title,
            })
        util.save_entry(title,txt)
        return redirect(entry, entry = title)


def saveedit(request):
    if request.method == "POST":
        
        txt = request.POST['text']
        util.save_entry(request.POST['title'], txt)


        return redirect(entry, entry = request.POST['title'])

def editpage(request):
    if request.method == "POST":
        txt = util.get_entry(request.POST['title'])

        return render (request, "encyclopedia/edit.html", {
            "txt" : txt,
            "title" : request.POST['title']
            }
        )

def randompage(request):
    if request.method == "GET":
        return redirect(entry, entry = choice(util.list_entries()))




