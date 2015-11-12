# -*- coding: utf-8 -*-
import json
from flask import Blueprint, g, render_template
from config import API
from datausa import app
from datausa.utils.format import affixes, dictionary, percentages

mod = Blueprint("general", __name__)

@app.before_request
def before_request():
    g.cache_version = 5
    g.affixes = json.dumps(affixes)
    g.dictionary = json.dumps(dictionary)
    g.percentages = json.dumps(percentages)
    g.api = API

@mod.route("/")
def home():
    g.page_type = "home"
    return render_template("general/home.html")
