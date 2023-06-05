from django.shortcuts import render, redirect
# import Markdown to convert MD files to HTML. 
from markdown2 import Markdown
# from .models import Event
from . import util
import random


# Converting MD extension file to HTML file if content exist otherwise return NONE.
def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# HTML file will be displayed according to the result we receive from Convert_md_to_HTML Function. 
def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Requested Page is not found !"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": html_content,
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
    if html_content is not None:
       return render(request, "encyclopedia/entry.html", {
            "title": entry_search,
            "content": html_content,
        })
    # Getting data from search form with the name 'q'. converting that data to HTML.
    # and if data exist than rendering it in entry.html. 
    else:
        allEnteries = util.list_entries()
        data = []
        for entry in allEnteries:
            if entry_search.lower() in entry.lower():
                data.append(entry)
        return render(request, "encyclopedia/search.html", {
            "data": data,
            "entry_search": entry_search
        })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['content']
        titleExist = util.get_entry(title)
        if titleExist is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Title already exists !"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content,
            })

def edit(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    

def edit_saved(request):
    if request.method == "POST":
        title = request.POST['entry_title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
                "title": title,
                "content": html_content
        })

def rndm(request):
    allEnteries = util.list_entries()
    rndm_entry = random.choice(allEnteries)
    html_content = convert_md_to_html(rndm_entry)
    return render(request, "encyclopedia/entry.html", {
        "title": rndm_entry,
        "content": html_content
    })
