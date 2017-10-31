from flask import Flask, request, render_template, make_response
from string import Template

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
    resultText = 'Almost there!'
    
    resultTemplate = searchResult.getResult()
    return resultTemplate.substitute(resultSegment=resultText)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)