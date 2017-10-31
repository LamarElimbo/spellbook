from string import Template

def getHTMLSeg():
    htmlTemplate = Template("""<div class="profile_container">

                            <h1>$title</h1>
                            <p>$sourceShow</p>
                            <p><i>$spell</i></p>
                            <p><b>$description</b></p>
                    </div>
                    <div id='divider'></div><br><br>""")
    return htmlTemplate