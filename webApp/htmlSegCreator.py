# Creates html segment from collected info

from string import Template
import htmlSeg

def createHTML(pSpells):
    
    htmlSegs=''
    
    for spell in pSpells:

        htmlSegment = htmlSeg.getHTMLSeg()
        
        spellTitle = spell[1]
        spellSource = spell[4]
        spellVerbal = spell[3]
        spellDescription = spell[5]
        
        htmlSegs += htmlSegment.substitute(title=spellTitle, sourceShow=spellSource, spell=spellVerbal, description=spellDescription)
            
    return htmlSegs
