import os

# print(env.variables.config['theme']['palette']) # access palette color. Automatic toggle of color ?

def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
#        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>
        return f"""<iframe src="https://console.basthon.fr/?from=https://raw.githubusercontent.com/bouillotvincent/coursNSI/master/morpion.py" width=100% height={hauteur}></iframe>"""

    @env.macro
    def linux(height : int ) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
#        return f"""<iframe src="https://console.basthon.fr/?from={env.variables.site_url}{env.variables.page.url}../{exo}" width=100% height={hauteur}></iframe>
        return f"""<iframe src="https://bellard.org/jslinux/vm.html?url=alpine-x86.cfg&mem=192" width=100% height={height}></iframe>"""

    @env.macro
    def console(height : int ) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        return f"""<iframe width="100%" height={height} name="embedded_python_anywhere" src="https://pyodide.org/en/stable/console.html"></iframe>"""

    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""
    # f"docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom}.py"

    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    @env.macro
    def html_fig(num: int) -> str:
        "Renvoie le code HTML de la figure n° `num`"
        return f'--8<-- "docs/' + os.path.dirname(env.variables.page.url.rstrip('/')) + f'/figures/fig_{num}.html"'

    env.variables['compteur_exo'] = 0
    @env.macro
    def exercice(var = True, prem = None):
        # si var == False, alors l'exercice est placé dans une superfence.
        if prem is not None : env.variables['compteur_exo'] = prem
        env.variables['compteur_exo'] += 1
        root = f"Exercice { env.variables['compteur_exo']}"
        return f"""exo \"{root}\"""" if var else '\"'+root+'\"'

    @env.macro
    def cours():
        return f'done "Cours"'

    @env.macro
    def ext():
        return f'ext "Pour aller plus loin"'

    @env.macro
    def tit(ch = "", text = ""):
        # Tasklist In Table
        checked = 'checked=""' if ch == 'x' else ''
        return f"""<ul class="task-list"><li class="task-list-item">\
            <label class="task-list-control"><input type="checkbox" {checked}>\
            <span class="task-list-indicator"></span>\
            </label>{text}</li></ul>"""

    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0

    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str, filetype : str = 'py') -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/"""
        print('ici',short_path)
        print(f"""{short_path}/scripts/{nom_script}.{filetype}""")
        try: 
            f = open(f"""{short_path}/scripts/{nom_script}.{filetype}""")
            content = ''.join(f.readlines())
            f.close()
            content = content+ "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            # change backslash_newline by backslash-newline
            return content.replace('\n','backslash-newline').replace('_','python-underscore').replace('*','python-star')
        except :
            return
        
    def generate_content(nom_script : str, filetype : str = 'py') -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script, filetype)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()"><img src="images/buttons/icons8-upload-64.png"></button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""
        # return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
        #         <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, mode: str) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/{stripped_nom_script}_test"
        content = read_ext_file(nom_script)
        # print("yoyo", env.variables.base_url )
        if content is not None: 
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji" onclick=\'executeTest("{tc}","{mode}")\'><img src="images/buttons/icons8-check-64.png"></button><span class="compteur">5/5</span>"""
            # return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji_dark" onclick=\'executeTest("{tc}","{mode}")\'>🛂</button><span class="compteur">5/5</span>"""
        else: 
            return ''


    def blank_space() -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="indent-text:5em"> </span>"""

    @env.macro
    def IDEv(nom_script : str ='') -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, 'v')


    @env.macro
    def IDE(nom_script : str ='', mode : str = 'h') -> str:
        """
        Purpose : Create an IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functional calls.
        Last span hides the code content of the IDE if loaded.
        """
        content, tc = generate_content(nom_script)
        rem_content, tc = generate_content(f"""{nom_script}_rem""", "txt")
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/{nom_script.split('/')[-1]}_corr""")
        div_edit = f'<div class="ide_classe">'
        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
        relative_path = '/'.join(nom_script.split('/')[:-1])
        print('toto', env.variables.page.url, nom_script, relative_path, env.variables.page.abs_url,env.variables.page.abs_url.split('/')[1])
        div_edit += f"""<button class="emoji" onclick='interpretACE("editor_{tc}","{mode}")'><img src="/{env.variables.page.abs_url.split('/')[1]}/images/buttons/icons8-play-64.png"></button>"""
        div_edit += f"""{blank_space()}<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'><img src="images/buttons/icons8-download-64.png"></button>{blank_space()}"""
        div_edit += create_upload_button(tc)
        div_edit += create_unittest_button(tc, nom_script, mode)
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
        div_edit += f'''
        --8<--- "docs/scripts/{nom_script}_rem.txt"
        '''
        return div_edit
    
    @env.macro
    def mult_col(*text):
        cmd = """<table style="border-color:transparent;background-color:transparent"><tr>"""
        for column in text:
            cmd += f"""<td><b style="font-size:1.2em">{column}</td>"""
        cmd += f"""</tr></table>"""
        return cmd