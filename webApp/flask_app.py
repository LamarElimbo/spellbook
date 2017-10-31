from flask import Flask, request, render_template, make_response
from string import Template
import spellGetter
import htmlSegCreator

import sys
sys.path.insert(0, './templates')
import searchResult


app = Flask(__name__)
requiredInfo=[]

@app.route('/')
@app.route('/search.html')
def search():
    return render_template('search.html')

@app.route('/result.html', methods=['POST'])
def result():
    inputDesire = request.form['desire']
    resultText = spellGetter.search(inputDesire)
    spellSeg = ''
    
    if len(resultText) == 0:
        spellSeg = "<center>Unfortunately, it seems that there are stonger forces than I preventing you from getting what you're looking for.</center>"
    else:
        spellSeg = htmlSegCreator.createHTML(resultText)
    
    resultTemplate = searchResult.getResult()
    return resultTemplate.substitute(resultSegment=spellSeg)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)