$('[id^=editor_]').each(function() {
    let number = this.id.split('_').pop();
    let url_pyfile = $('#'+this.id).text()  // Extracting url from the div before Ace layer
    let id_editor = "editor_" + number
    function createACE(id_editor){
        var editor = ace.edit(id_editor, {
            theme: "ace/theme/tomorrow_night_bright",
            mode: "ace/mode/python",
            autoScrollEditorIntoView: true,
            maxLines: 30,
            minLines: 6,
            tabSize: 4,
            printMargin: false   // hide ugly margins...
        });
    }
    window.REPL_ready=createACE(id_editor)           // Creating Ace Editor #id_editor

    if (url_pyfile === '') { 
        let editor = ace.edit(id_editor)
        editor.getSession().setValue('\n\n\n\n\n');  // Creates 6 empty lines for UX
    }
});

// Javascript to upload file from customized buttons
$('[id^=input_editor_]').each(function() {
    let number = this.id.split('_').pop();
    let id_editor = "editor_" + number
    document.getElementById('input_'+id_editor).addEventListener('change', function(e) {readFile(e,id_editor)}, false);

});
function readFile (evt, id_editor) {
    var files = evt.target.files;
    var file = files[0];
    var reader = new FileReader();
    var editor = ace.edit(id_editor);
    reader.onload = function(event) {
        editor.getSession().setValue(event.target.result);
        console.log('plaf')
    }
    reader.readAsText(file)
};