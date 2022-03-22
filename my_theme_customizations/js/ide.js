var tagHdr = "#--- HDR ---#";

$('[id^=editor_]').each(function() {
    let number = this.id.split('_').pop();
    //let url_pyfile = $('#'+this.id).text()  // Extracting url from the div before Ace layer
    let url_pyfile = $('#content_'+this.id).text()  // Extracting url from the div before Ace layer

    if (url_pyfile.includes(tagHdr)) {
        splitHdrPyFile = url_pyfile.match(new RegExp(tagHdr + "(.*)" + tagHdr + "(.*)"));
        if (splitHdrPyFile === null) { pyFile = `Missing ${tagHdr} tag. Please check !\n\n` + url_pyfile } 
        else {
            hdrFile = splitHdrPyFile[1];
            pyFile = splitHdrPyFile[2];
            newline = 'bksl-nl';
            while(pyFile.startsWith(newline)) { pyFile = pyFile.substring(newline.length); }
        }
    } else {
        pyFile = url_pyfile;
    }

    let id_editor = "editor_" + number
    function createACE(id_editor){
        let paletteElement = document.querySelector('label[for="__palette_2"]')
        if (paletteElement.previousElementSibling.dataset.mdColorMedia === "(prefers-color-scheme: dark)") {
            var defineTheme = paletteElement.hidden ? "ace/theme/crimson_editor" : 'ace/theme/tomorrow_night_bright'
        } else {
            var defineTheme = paletteElement.hidden ? 'ace/theme/tomorrow_night_bright' : "ace/theme/crimson_editor"
        }
        ace.require("ace/ext/language_tools");
        var editor = ace.edit(id_editor, {
            theme: defineTheme,
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            printMargin: false   // hide ugly margins...
        });
        editor.setOptions({
            enableBasicAutocompletion: true,
            enableSnippets: true,
            enableLiveAutocompletion: true
        });
        // Decode the backslashes into newlines for ACE editor from admonitions 
        // (<div> autocloses in an admonition) 
        editor.getSession().setValue(pyFile.replace(/bksl-nl/g, "\n").replace(/py-und/g, "_").replace(/py-str/g, "*"))  
    }
    window.IDE_ready = createACE(id_editor)           // Creating Ace Editor #id_editor

    if (url_pyfile === '') { 
        let editor = ace.edit(id_editor)
        editor.getSession().setValue('\n\n\n\n\n');  // Creates 6 empty lines for UX
    }

    // A correction Element always exists (can be void)
    prevNode = document.getElementById("corr_content_" + id_editor)
    var key = prevNode.dataset.strudel
    var workingNode = prevNode
    var remNode = document.createElement("div");

    console.log(remNode)
    if (prevNode.parentNode.tagName === 'P') {
        
        // REM file on top level
        // console.log('51',id_editor,workingNode, workingNode.parentNode.innerHTML.includes('<strong>A</strong>'))
        workingNode = prevNode.parentNode.nextElementSibling //'<strong>A</strong>'
        // if (workingNode.nex)

        if (workingNode.innerHTML.includes('<strong>A</strong>') && workingNode.nextElementSibling.innerHTML.includes('<strong>Z</strong>')) {
            remNode.innerHTML = 'Pas de remarque particulière.';
            workingNode.nextElementSibling.remove()
            workingNode.remove()

        } else {
        workingNode.remove()
        workingNode = prevNode.parentNode.nextElementSibling

        var tableElements = [];
        while (!workingNode.innerHTML.includes('<strong>Z</strong>')) {
            tableElements.push(workingNode)
            workingNode = workingNode.nextElementSibling;
        }
        workingNode.remove()

        for (let i = 0; i < tableElements.length; i++ ){
            remNode.append(tableElements[i])
        }
    }

    } else {
        // Search for the rem DIV.
        workingNode = workingNode.nextElementSibling
        // console.log(prevNode, workingNode)
        // If workingNode is a <p> (admonition), we continue
        // else, we are outside an admonition
        if (workingNode !== null) {
            workingNode = workingNode.nextElementSibling
        }
    // }
    // No remark file. Creates standard sentence.
    if (workingNode === null) {
        remNode.innerHTML = 'Pas de remarque particulière.';
    } else {

        var tableElements = [];
        while (workingNode !== null) {
            tableElements.push(workingNode)
            workingNode = workingNode.nextElementSibling;
        }

        for (let i = 0; i < tableElements.length; i++ ){
            remNode.append(tableElements[i])
        }
        
    }}
    // Should create a global div
    console.log('LAAÀ',remNode, prevNode)
    if (key == "")  
    /* another possible condition is this : 
    !remNode.innerHTML.includes('<h1'))  */
    {  
        prevNode.insertAdjacentElement('afterend', remNode)
        remNode.setAttribute("id", "rem_content_" + id_editor);
        document.getElementById("rem_content_" + id_editor).style.display = "none"
    } else {
        // console.log("hack", key)
        // console.log("result", md5('e-nsi' + key ))
        let folder = md5('e-nsi+' + key)
        remNode = document.createElement("div");
        remNode.innerHTML = `Vous trouverez une analyse détaillée de la solution <a href = "../${folder}/exo_REM/" target="_blank"> ici </a>`
        prevNode.insertAdjacentElement('afterend', remNode)
        remNode.setAttribute("id", "rem_content_" + id_editor);
        document.getElementById("rem_content_" + id_editor).style.display = "none"
    }

});

// Javascript to upload file from customized buttons
$('[id^=input_editor_]').each(function() {
    let number = this.id.split('_').pop();
    let id_editor = "editor_" + number
    document.getElementById('input_'+id_editor).addEventListener('change', function(e) {readFile(e, id_editor)}, false);
});

function readFile (evt, id_editor) {
    let files = evt.target.files;
    let file = files[0];
    let reader = new FileReader();
    var editor = ace.edit(id_editor);
    reader.onload = function(event) {
        editor.getSession().setValue(event.target.result);
    }
    reader.readAsText(file)
};

// turn off copy paste of code... A bit aggressive but necessary
$(".highlight").bind('copy paste',function(e) { e.preventDefault(); return false; });

// Following blocks paint the IDE according to the mkdocs light/dark mode 
function paintACE(theme) {
    for (var editeur of document.querySelectorAll('div[id^="editor_"], div[id^="corr_editor_"]')) {
        let editor = ace.edit(editeur.id);
        editor.setTheme(theme);
        editor.getSession().setMode("ace/mode/python");
    };
}

window.addEventListener('DOMContentLoaded', () => {
    let paletteElement = document.querySelector('label[for="__palette_2"]')
    if (paletteElement.previousElementSibling.dataset.mdColorMedia === "(prefers-color-scheme: dark)") {
        var defineTheme = paletteElement.hidden ? "ace/theme/crimson_editor" : 'ace/theme/tomorrow_night_bright'
    } else {
        var defineTheme = paletteElement.hidden ? 'ace/theme/tomorrow_night_bright' : "ace/theme/crimson_editor"
    }
    if (paletteElement.hidden == true) {
        paintACE(defineTheme) // bright mode
    } else {
        paintACE(defineTheme)  // night mode
    }
});


var p2 = document.querySelector('input[id="__palette_2"]')
p2.addEventListener('click', () => { 
    if (p2 === "(prefers-color-scheme: dark)") {
        paintACE('ace/theme/tomorrow_night_bright')
    } else {
        paintACE('ace/theme/crimson_editor')
    }
    
});

var p1 = document.querySelector('input[id="__palette_1"]')
p1.addEventListener('click', () => { 
    if (p1 === "(prefers-color-scheme: light)") {
        paintACE('ace/theme/crimson_editor')
    } else {
        paintACE('ace/theme/tomorrow_night_bright')
    }
});