# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render

from utils import ls_dir, clean_ext, get_label_id

# Create your views here.

def nav_dict():
    view_dict = {
    'tutorials' : ls_dir("tutorials/templates/tutorials"),
    'project' : ls_dir("tutorials/templates/projects"),
    'about': 'about',
    'nav': 'nav.html',
    }
    return view_dict



def tutorials_list(request):
    view_dict = nav_dict()
    html_link = ""
    view_dict['folder'] = 'tutorials'
    view_dict['html_file'] = ''
    view_dict['title_text'] = 'Sharing recent findings'
    return render(request, 'tutorials.html', view_dict)



def tutorials(request, file_name):
    view_dict = nav_dict()
    html_link = "tutorials/templates/tutorials/{0}".format(file_name)
    if os.path.isfile(html_link):
        view_dict['divs'] = get_label_id(html_link)
        view_dict['folder'] = 'tutorials'
        view_dict['html_file'] = "tutorials/{0}".format(file_name)
        view_dict['title_text'] = 'Sharing recent findings'
        return render(request, 'tutorials.html', view_dict)
    else:
        raise Http404()
