from flask import Flask, request, render_template
from io import StringIO
import urllib
import csv
import spellGetter

app = Flask(__name__)

@app.route('/')
@app.route('/spellbook_search')
def spellbook_search():
    return render_template('search.html', 
                           css_source='../static/app.css', 
                           activeTab='spellbook')

@app.route('/spellbook_result', methods=['POST'])
def spellbook_result():
    inputDesire = request.form['desire']    
    resultSpells = spellGetter.search(inputDesire)
    return render_template('searchResultSpellbook.html', 
                           spellInfo=resultSpells, 
                           css_source='app.css', 
                           activeTab='spellbook')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)