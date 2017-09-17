# utils.py

import os, urllib, re

from bs4 import BeautifulSoup
from django.conf import settings


def shorten_label(some_text):
    if len(some_text)<24:
        clean_label=some_text
    else:
        word_list = some_text.split()
        phrase = [word_list[0]]
        index = 1
        while index < len(word_list):
            if len(" ".join(x for x in phrase) + ' ' + word_list[index]) < 24:
                phrase.append(word_list[index])
                index = index + 1
            else:
                break
        clean_label = " ".join(x for x in phrase)
    return clean_label


def get_label_id(full_path):

    html_doc = urllib.urlopen(full_path)
    soup = BeautifulSoup(html_doc, 'html.parser')

    divs = soup.findAll("div", {"class":"section level3"})

    labels = []
    ids = []
    for tag in divs:
        shorty = shorten_label(tag.h3.text)
        labels.append(shorty)
        ids.append(tag['id'])
    return zip(labels, ids)


def clean_ext(list_of_files):
    """ take a list of strings with any extension and replaces _ by spaces
    and removes the extension. 
    Returns a list of pairs. 
    """
    out_list = []
    for file_name in list_of_files:
        short_name = file_name.split('.')[0: -1]
        full_name = ' '.join(short_name)
        with_spaces = re.sub(r'_', ' ', full_name)
        out_list.append((file_name, with_spaces))
    return sorted(out_list)


def ls_dir(folder):
    list_of_files = os.listdir(folder)
    clean_list = clean_ext(list_of_files)
    return(clean_list)
