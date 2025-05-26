import markdown2
from django.shortcuts import render, redirect
import os
from django.views.decorators.csrf import csrf_protect
import random
from . import util

@csrf_protect
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search_bar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            content = util.get_entry(query)
            if content:
                return redirect('entry_page', title=query)
            elif substring(query):
                return render(request, "encyclopedia/search_results.html", {
                    "results": substring(query)
                })
            else:
                return render(request, "encyclopedia/error_page.html", {
                    "title": "The requested page was not found",
                    "error_message": "Try again with a different entry"
                })

def entry_page(request, title):
    content = util.get_entry(title) 
    if content:
        html_format = markdown2.markdown(content)
        return render(request, "encyclopedia/wiki_entries.html", {
            "entry_title": title,
            "content": html_format
            })
    else:
        return render(request, "encyclopedia/error_page.html", {
            "title": f"The entry '{title}' does not exist",
            "error_message": "The page you are trying to access does not exist or is currently unavailable, try again with a different entry"
        })

def create_entry(request):
    return render(request, "encyclopedia/add.html", {
    })

def edit(request, title):
    if request.method == "POST":
        new_content = request.POST.get("c", "").strip()
        if new_content:
            util.save_entry(title, new_content)
            return redirect('entry_page', title=title)
        else:
            return render(request, "encyclopedia/error_page.html", {
                "title": "Ediditing Error",
                "error_message": f"The content of '{title}' cannot be left blank"
            })
    content = util.get_entry(title)
    if content:
        return render(request, "encyclopedia/edit.html", {
            "current_title": title,
            "current_content": content
        })
    else:
        return render(request, "encyclopedia/error_page.html", {
                "title": "Error",
                "error_message": f"'{title}' either does not exist or is currently unavailable for editing purposes"
            })

def display_new_entry(request):
    if request.method == "POST":
        entry_title = request.POST.get("t", "").strip()
        entry_content = request.POST.get("c", "").strip()
        if entry_title in util.list_entries():
            return render (request, "encyclopedia/error_page.html", {
            "title": f"The entry '{entry_title}' already exist",
            "error_message": "Try creating an entry with a different title"
        })
        else:
            util.save_entry(entry_title, entry_content)
            return redirect('entry_page', title=entry_title)

def random_page(request):
    entry_list = util.list_entries()
    selected_page = random.choice(entry_list)
    if selected_page:
        return redirect('entry_page', title = selected_page)
    else:
        return render(request, "encyclopedia/error_page.html", {
            "title": "Error with Random Feature",
            "error_message": "There are no entries to display, try creating a new entry and try again later"
            })


def substring(input):
    available_entries = util.list_entries()
    results = []
    for entry in available_entries:
        if input in entry:
            results.append(entry)
    if results:
        return results
    return None

def delete(request, title):
    content = util.get_entry(title)
    if content:
        util.delete_entry(title)
        return redirect('index')
    else:
        return render(request, "encyclopedia/error_page.html", {
            "error_message": f"The entry '{title}' does not exist",
            "title": "Deletion Error"
        })