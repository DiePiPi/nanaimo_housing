# views.py
#dir /


import os
from django.shortcuts import render

from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.http import HttpResponse,HttpResponseRedirect

from utils import ls_dir, clean_ext, get_label_id


# Create your views here.

def nav_dict():
    view_dict = {
    'tutorials' : ls_dir("templates/tutorials"),
    'project' : ls_dir("templates/projects"),
    'about': 'about',
    'nav': 'nav.html',
    }
    return view_dict


def nothing_here(request):
    return Http404()


def home(request):
    return render(request, 'home.html', {'hello': 'Hello!'})


def logo(request):
    return render(request, 'logo.html')
    

def about(request):
    view_dict = nav_dict()
    return render(request, 'about.html', view_dict)


def tutorials_list(request):
    view_dict = nav_dict()
    html_link = ""
    view_dict['folder'] = 'tutorials'
    view_dict['html_file'] = ''
    view_dict['title_text'] = 'Sharing recent findings'
    return render(request, 'tutorials.html', view_dict)



def tutorials(request, file_name):
    view_dict = nav_dict()
    html_link = "templates/tutorials/{0}".format(file_name)
    if os.path.isfile(html_link):
        view_dict['divs'] = get_label_id(html_link)
        view_dict['folder'] = 'tutorials'
        view_dict['html_file'] = "tutorials/{0}".format(file_name)
        view_dict['title_text'] = 'Sharing recent findings'
        return render(request, 'tutorials.html', view_dict)
    else:
        raise Http404()
