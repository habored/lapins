env.variables['term_counter'] = 0
@env.macro
def terminal(prem = 0) -> str:
    tc = env.variables['term_counter']
    env.variables['term_counter'] += 1
    return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

def read_ext_file(nom_script : str) -> str:
    short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
    if len(nom_script) > 0: 
        f = open(f"""{short_path}/scripts/{nom_script}.py""")
        content = ''.join(f.readlines())
        f.close()
        return content 
    else : return
    
env.variables['REPL_counter'] = 0
def generate_content(nom_script : str, type: bool = False) -> str:
    tc = env.variables['REPL_counter']
    content = read_ext_file(nom_script)
    div_edit = "<div "
    if type : div_edit += "class=line"  # horizontal REPL
    if len(nom_script) > 0: div_edit += f""" id="editor_{tc}">{content}</div>"""        
    else : div_edit += f""" id="editor_{tc}"></div>"""
    env.variables['REPL_counter'] += 1
    return div_edit, tc

def create_upload_button(tc : str) -> str:
    return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
            <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide" />"""

@env.macro
def REPLv(nom_script='') -> str:
    div_edit, tc = generate_content(nom_script)
    div_edit = f'<div class="wrapper"><div class="interior_wrapper">{div_edit}</div>\
    <div id="term_editor_{tc}" class="term_editor"></div></div><button class="emoji" onclick=\'interpretACE("editor_{tc}","vert")\'>▶️</button>'
    div_edit += f"""<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>"""
    div_edit += create_upload_button(tc)
    return div_edit

@env.macro
def REPL(nom_script='') -> str:
    div_edit, tc = generate_content(nom_script, True)
    div_edit = f'<div class="wrapper_h">{div_edit}<div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div><button class="emoji" onclick=\'interpretACE("editor_{tc}","hori")\'>▶️</button>' 
    div_edit += f"""<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>"""
    div_edit += create_upload_button(tc)
    return div_edit