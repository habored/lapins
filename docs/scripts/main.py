env.variables['term_counter'] = 0
@env.macro
def terminal(prem = 0) -> str:
    tc = env.variables['term_counter']
    env.variables['term_counter'] += 1
    return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

def read_ext_file(nom_script : str, tc : int) -> str:
    short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
    if len(nom_script) > 0: 
        f = open(f"""{short_path}/scripts/{nom_script}.py""")
        content = ''.join(f.readlines())
        f.close()
        return content 
    else : return
    
env.variables['REPL_counter'] = 0
@env.macro
def REPLv(nom_script='',last = 0) -> str:
    tc = env.variables['REPL_counter']
    short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
    content = read_ext_file(nom_script, tc)
    if len(nom_script) > 0: 
        div_edit = f"""<div id="editor_{tc}">{content}</div>"""        
    else : div_edit = f'<div id="editor_{tc}"></div>'
    env.variables['REPL_counter'] += 1
    div_edit = f'<div class="wrapper"><div class="interior_wrapper">{div_edit}</div>\
    <div id="term_editor_{tc}" class="term_editor"></div></div><button onclick=\'interpretACE("editor_{tc}","vert")\' style="font-size:2em">⚙️</button>'
    return f"""{div_edit}<script src="../xtra/javascripts/repl.js"></script> """ if last==-1 else div_edit

@env.macro
def REPL(nom_script='', last = 0) -> str:
    tc = env.variables['REPL_counter']
    short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
    content = read_ext_file(nom_script, tc)
    if len(nom_script) > 0: 
        div_edit = f"""<div class="line" id="editor_{tc}">{content}</div>"""        
    else : div_edit = f'<div class="line" id="editor_{tc}"></div>'        
    env.variables['REPL_counter'] += 1
    div_edit = f'<div class="wrapper_h">{div_edit}<div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div><button onclick=\'interpretACE("editor_{tc}","hori")\' style="font-size:2em">⚙️</button>' 
    return f"""{div_edit}<script src="../xtra/javascripts/repl.js"></script> """ if last==-1 else div_edit