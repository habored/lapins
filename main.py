import os

def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        print(exo)
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
    def exercice(prem = 1):
        if prem == 0 : env.variables['compteur_exo'] = 0
        env.variables['compteur_exo'] += 1
        return f"tip \"Exercice { env.variables['compteur_exo']}\""

    @env.macro
    def cours():
        return f'done "Cours"'

    env.variables['term_counter'] = 0
    @env.macro
    def terminal(prem = 0) -> str:
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"<div onclick='start_term(\"id{tc}\")' id=\"fake_id{tc}\" class=\"terminal_f\"><label class=\"terminal\"><span>>>> </span></label></div><div id=\"id{tc}\" class=\"hide\"></div>"

    @env.macro
    def terminal2(tc) -> str:
        return f"<div onclick='start_term(\"id{tc}\")' id=\"fake_id{tc}\" class=\"terminal_f\"><label class=\"terminal\"><span>>>> </span></label></div><div id=\"id{tc}\" class=\"hide\"></div>"

    env.variables['REPL_counter'] = 0
    @env.macro
    def REPL(nom_script='',prem = 0) -> str:
        print(f'{env.variables.site_url}{env.variables.page.url}../{nom_script}')
        tc = env.variables['REPL_counter']
        env.variables['REPL_counter'] += 1
        print('pif', nom_script, os.path.dirname(env.variables.page.url))
        if len(nom_script) > 0: div_edit = f'<div id="editor_{tc}">scripts/{nom_script}.py</div>'
        else : div_edit = f'<div id="editor_{tc}"></div>'
        return f'<div class="wrapper"><div class="interior_wrapper">{div_edit}</div>\
        <div id="term_editor_{tc}" class="term_editor"></div></div><button onclick=\'interpretACE("editor_{tc}")\' style="font-size:2em">⚙️</button>'