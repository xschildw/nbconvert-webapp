from urllib import urlopen
from flask import Flask
from flask import request
from nbconvert import HTMLExporter
import nbformat

app = Flask(__name__)
 
# Converts ipynb file referenced by url parameter 'file' to html
# Ideally we would convert to pdf.  Tried using command line call (via subprocess), but it depends on TeX being installed (which is a heavy ask for the lambda environment).
# https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
@app.route("/html")
def convertToHtml():
    response = urlopen(request.args.get('file')).read().decode()
    notebook = nbformat.reads(response, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(notebook)
    return body
 
if __name__ == "__main__":
    app.run()

    
