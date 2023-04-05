from flask import Blueprint, render_template

page = Blueprint('page', __name__)

# Base API to return home page
@page.route('/')
def index():
    return render_template('index.html')

# About page
@page.route('/about')
def about():
    return render_template('about.html')

# Display Gallery page
@page.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Display MyData page
@page.route('/mydata')
def mydata():
    return render_template('mydata.html')

# Display Upload page for global
@page.route('/upload-global')
def upload_page_global():
    return render_template('uploadglobal.html')

# Display Upload page for local
@page.route('/upload-local')
def upload_page_local():
    return render_template('uploadlocal.html')