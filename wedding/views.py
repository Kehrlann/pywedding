#coding=utf-8

from flask import render_template, request, redirect, url_for
from wedding import app
import db


@app.route("/", methods=["GET"])
@app.route("/infos", methods=["GET"])
def index():
    return render_template("index.html", text=app.config['INFO_PAGE'])

@app.route("/honeymoon", methods=["GET"])
def honeymoon():
    return render_template("honeymoon.html", text=app.config['HONEYMOON_PAGE'])

@app.route("/wishlist", methods=["GET"])
def wishlist():
    items = db.load_wishlist()
    return render_template("wishlist.html", items=items, text=app.config['WISHLIST_HEADER'])

@app.route("/accommodation", methods=["GET"])
def accommodation():
    items = db.load_accommodation()
    return render_template("accommodation.html", items=items, text=app.config['ACCOMMODATION_HEADER'])

@app.route("/gift", methods=["POST"])
def gift():
    up = db.update_wishlist_by_id(request.form['id'], request.form['mail'])
    return redirect(url_for('wishlist'))

@app.template_filter("gmap")
def gmap(input):
    return input.replace(" ", "+")