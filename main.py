import os

# print(env.variables.config['theme']['palette']) # access palette color. Automatic toggle of color ?

def define_env(env):
    "Hook function"

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
    INFTY_SYMBOL = '\u221e'

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

    def read_ext_file(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/"""

        try: 
            if path == "":
                f = open(f"""{short_path}/scripts/{nom_script}.{filetype}""")
            else:
                # print('relp', f"""{short_path}/{path}/{nom_script}.{filetype}""")
                f = open(f"""{short_path}/{path}/{nom_script}.{filetype}""")
            # f = open(f"""{short_path}/scripts/{nom_script}.{filetype}""")
            content = ''.join(f.readlines())
            f.close()
            content = content + "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            # change backslash_newline by backslash-newline
            return content.replace('\n','backslash-newline').replace('_','python-underscore').replace('*','python-star')
        except :
            return
        
    def generate_content(nom_script : str, path : str, filetype : str = 'py') -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script, path, filetype)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        path_img = env.variables.page.abs_url.split('/')[1]
        return f"""<button class="tooltip" onclick="document.getElementById('input_editor_{tc}').click()"><img src="/{path_img}/images/buttons/icons8-upload-64.png"><span class="tooltiptext">Téléverser</span></button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, path : str, mode: str, MAX : int = 5) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/{stripped_nom_script}_test"
        content = read_ext_file(nom_script, path)
        if content is not None: 
            path_img = env.variables.page.abs_url.split('/')[1]
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span>\
                <button class="tooltip" onclick=\'executeTest("{tc}","{mode}")\'>\
                <img src="/{path_img}/images/buttons/icons8-check-64.png">\
                <span class="tooltiptext">Valider</span></button><span class="compteur">\
                {MAX}/{MAX}\
                </span>"""
        else: 
            return ''


    def blank_space() -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="indent-text:5em"> </span>"""

    @env.macro
    def IDEv(nom_script : str = '', MAX : int = 5) -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, mode = 'v', MAX = 5)

    def get_max_from_file(content : str) -> tuple:#[str, int]: # compatibilité Python antérieur 3.8
        split_content = content.split('backslash-newline')
        max_var = split_content[0]
        if max_var[:4] != "#MAX":
            MAX = 5 
        else:
            value = max_var.split('=')[1].strip()
            MAX = int(value) if value not in ['+', 1000] else INFTY_SYMBOL
            i = 1
            while split_content[i] == '':
                i += 1
            content = 'backslash-newline'.join(split_content[i:])
        return content, MAX

    def test_style(nom_script : str, element : str):
        guillemets = ["'", '"']
        ide_style = ["", "v"]
        styles = [f"""IDE{istyle}({i}{nom_script}{i}""" for i in guillemets for istyle in ide_style]
        return any([style for style in styles if style in element])


    @env.macro
    def IDE(nom_script : str = '', mode : str = 'h', MAX : int = 5) -> str:
        """
        Purpose : Create an IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functional calls.
        Last span hides the code content of the IDE if loaded.
        """
        path_img = env.variables.page.abs_url.split('/')[1]

        #        path_files = '/'.join([folder for folder in env.variables.page.abs_url.split('/')[:-1] if folder != ""])
        path_file = '/'.join(filter(lambda folder: folder != "", env.variables.page.abs_url.split('/')[2:-2]))
        content, tc = generate_content(nom_script, path_file)

        content, max_from_file = get_max_from_file(content)
        MAX = max_from_file if MAX == 5 else MAX
        MAX = MAX if MAX not in ['+', 1000] else INFTY_SYMBOL
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/{nom_script.split('/')[-1]}_corr""", path_file)
        div_edit = f'<div class="ide_classe" id={MAX}>'
        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
        div_edit += f"""<button class="tooltip" onclick='interpretACE("editor_{tc}","{mode}")'><img src="/{path_img}/images/buttons/icons8-play-64.png"><span class="tooltiptext">Lancer</span></button>"""
        div_edit += f"""{blank_space()}<button class="tooltip" onclick=\'download_file("editor_{tc}","{nom_script}")\'><img src="/{path_img}/images/buttons/icons8-download-64.png"><span class="tooltiptext">Télécharger</span></button>{blank_space()}"""
        div_edit += create_upload_button(tc)
        div_edit += create_unittest_button(tc, nom_script, path_file, mode, MAX)
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
        elt_insertion = [elt for elt in env.page.markdown.split("\n") if test_style(nom_script, elt)]
        elt_insertion = elt_insertion[0] if len(elt_insertion) >=1 else ""
        spaces = " "*(len(elt_insertion) - len(elt_insertion.lstrip()))
        if nom_script == '' : spaces = " "
        print(tc, spaces == "", elt_insertion, len(elt_insertion) - len(elt_insertion.lstrip()))
        if spaces == "":
            div_edit += f'''
{spaces}--8<--- "docs/xtra/start.md"
'''
        div_edit += f'''
{spaces}--8<--- "docs/{path_file if path_file != "" else 'scripts'}/{nom_script}_REM.md"'''
        if spaces == "":
            div_edit += f'''
{spaces}--8<--- "docs/xtra/end.md"
'''

# {spaces}--8<--- "docs/xtra/start.md"
#         '''

        # div_edit += f'''
        # --8<-- "docs/dentiste/exo_REM.md"
        # '''
        # print(env.page.markdown)
        # print(tc, div_edit)
        return div_edit
    
    @env.macro
    def mult_col(*text):
        cmd = """<table style="border-color:transparent;background-color:transparent"><tr>"""
        for column in text:
            cmd += f"""<td><b style="font-size:1.2em">{column}</td>"""
        cmd += f"""</tr></table>"""
        return cmd