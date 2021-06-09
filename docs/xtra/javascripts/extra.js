function sleep(s){
    return new Promise(resolve => setTimeout(resolve, s));
  }
  
async function main() {
    await loadPyodide({ indexURL : 'https://cdn.jsdelivr.net/pyodide/v0.17.0/full/' });
}

let pyodideReadyPromise = main();

async function pyterm(id) {
await pyodideReadyPromise;
let namespace = pyodide.globals.get("dict")();

// creates the console
// the variable pyconsole is created here.
pyodide.runPython(`
    import sys
    import js
    from pyodide import console
    import __main__

    class PyConsole(console._InteractiveConsole):
        def __init__(self):
            super().__init__(
                __main__.__dict__,
                persistent_stream_redirection=False,
            )

        def banner(self):
            return f"Welcome to the Pyodide terminal emulator 🐍\\n{super().banner()}"

    
    js.pyconsole = PyConsole()
`, namespace);
namespace.destroy();

let ps1 = '>>> ', ps2 = '... ';

async function lock(){
    let resolve;
    let ready = term.ready;
    term.ready = new Promise(res => resolve = res);
    await ready;
    return resolve;
}

async function interpreter(command) {  /// reads the commands
    let unlock = await lock();
    try {
    term.pause();
    // multiline should be splitted (useful when pasting)
    for( const c of command.split('\n') ) {
        let run_complete = pyconsole.run_complete;   // trying to run the commands
        try {
            const incomplete = pyconsole.push(c);    // wait for completion of a Python command
            term.set_prompt(incomplete ? ps2 : ps1); // set the prompt line
            let r = await run_complete;
            if(pyodide.isPyProxy(r)){
            r.destroy();
            }
        } catch(e){   // the completion of the Python command triggered an error (wrong Python syntax)
            if(e.name !== "PythonError"){
            term.error(e);
            throw e;
            }
        }
        run_complete.destroy();
    }
    } finally {
    term.resume();
    await sleep(10);
    unlock();
    }
}


let term = $(id).terminal(   // creates terminal
    interpreter,      // how to read the input
    {
    greetings: '',    // pyconsole.banner(),
    prompt: ps1,
    completionEscape: false,
    height: 200,
    completion: function(command, callback) {     // autocompletion
        callback(pyconsole.complete(command).toJs()[0]);
    }
    }
);

window.term = term;
pyconsole.stdout_callback = s => $.terminal.active().echo(s, {newline : false});   // this is thie line to change
    pyconsole.stderr_callback = s => {
        $.terminal.active().error(s.trimEnd());
    }


term.ready = Promise.resolve();
pyodide._module.on_fatal = async (e) => {
    term.error("Pyodide has suffered a fatal error. Please report this to the Pyodide maintainers.");
    term.error("The cause of the fatal error was:");
    term.error(e);
    term.error("Look in the browser console for more details.");
    await term.ready;
    term.pause();
    await sleep(15);
    term.pause();
};
}


function createACE(id_editor){
    var editor = ace.edit(id_editor, {
        theme: "ace/theme/tomorrow_night_bright",
        mode: "ace/mode/python",
        autoScrollEditorIntoView: true,
        maxLines: 30,
        minLines: 6,
        tabSize: 4
    });
}

async function evaluatePythonFromACE(code, id_editor) {
    await pyodideReadyPromise;

    $.terminal.active().clear();   
    pyodide.runPython(`
      import sys as __sys__
      import io as __io__
      __sys__.stdout = __io__.StringIO()
    `);

    // TODO WARNING memory leak : globals() should be cleaned. Code below is too aggressive !!  
    // pyodide.runPython(`
    // variable = 0
    // for variable in list(globals()):
    //     if variable[0:2] != "__":
    //         print('variable globale', globals()[variable])
    //         del globals()[variable]
    // `)
    // console.log(pyodide.globals.dict())

    // resize terminal to the size of editor on interpreting
    $.terminal.active().resize($.terminal.active().width(), document.getElementById(id_editor).style.height);

    try {
      let output = await pyodide.runPythonAsync(code);    // Running the code OUTPUT ????
      var stdout = pyodide.runPython("__sys__.stdout.getvalue()")  // Redirecting the output
      $.terminal.active().echo(">>> Script exécuté !\n"+stdout); 
    } catch(err) {
      $.terminal.active().echo(">>> Script exécuté !\n"+err);
    }
  }

async function interpretACE(id_editor) {
    $('#term_'+id_editor).terminal().focus(true)   // gives the focus to the corresponding terminal
    var editor = ace.edit(id_editor)
    let stream = await editor.getSession().getValue()
    evaluatePythonFromACE(stream, id_editor)
}


function start_term(nom_id) {
    document.getElementById(nom_id).className = "terminal terminal_f";
    document.getElementById('fake_'+nom_id).className = "hide";
    window.console_ready = pyterm('#'+nom_id);
    }
    
$(document).ready(function() {
    // auto-load the Terminals but slows down A LOT the global loading of pyodide (not a good idea)
    // $('[id^=cons_]').each(function() {
    //     let number = this.id.split('_').pop();
    //     window.console_ready = pyterm('#cons_'+number);
    // });

    $('[id^=editor_]').each(function() {
        let number = this.id.split('_').pop();
        let url_pyfile = $('#'+this.id).text()  // Extracting url from the div before Ace layer
        let id_editor = "editor_" + number

        createACE(id_editor)                  // Creating Ace Editor #id_editor

        if (url_pyfile === '') { 
            let editor = ace.edit(id_editor)
            editor.getSession().setValue('\n\n\n\n\n');  // Creates 6 empty lines for UX
        }
        window.console_ready = pyterm('#term_editor_'+number);
    });
    //  $('#term_editor_0').terminal().focus(true)
});