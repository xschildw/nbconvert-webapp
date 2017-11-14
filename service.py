# -*- coding: utf-8 -*-
from urllib import urlopen
from nbconvert import HTMLExporter
import nbformat

def handler(event, context):
    response = urlopen(event.get('file')).read().decode()
    notebook = nbformat.reads(response, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.template_file = 'basic'
    (body, resources) = html_exporter.from_notebook_node(notebook)
    return {
        "statusCode": 200,
        "headers": { "Content-Type": "text/html"},
        "body": body
    }
