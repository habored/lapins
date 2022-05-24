import random

@env.macro
def qcm(list_answers, list_correct, shuffle = True):
    alphabet = [chr(ord('a') + i) for i in range(26)]
    if type(list_correct) == int : list_correct = [list_correct]
    list_correct = list(map(lambda x : x - 1, list_correct))  # back to 0 to n-1 indexing
    def spanify(html_tag):
        return f"""<span>{html_tag}</span>"""
    
    def generate_id():
        return "".join(random.choices(alphabet, k = 6))

    def buttonify(answer, id, correct):
        return f"""<input type="checkbox" id="{id}" class="qcm-checkbox {correct}"><span class="check-toggle"></span><label for="{id}" class="qcm-item arithmatex">{answer}</label>"""

    def latexify(answer):
        """$ might not be the first character :
        blabla $1+1$
        """
        if answer.count('$') - answer.count('\$') >= 2: #regex begin ___$ and end $____ and $ not preceded by \
            string = ''
            start_dollar = True
            for i in range(len(answer)):
                lettre = answer[i]
                if lettre == '$':
                    if i == 0 or (i >= 1 and answer[i-1] != '\\'): # case escaping dollar \$ 
                        string += '\(' if start_dollar else '\)'
                        start_dollar = not start_dollar
                    else:
                        string += '$'
                else :
                    string += lettre
            return string
        return answer
    
    def codeblockify(answer):
        if answer[0:3] == "`#!":
            sep = answer.index(" ")
            language = answer[3:sep]
            return f"""<pre style="display: inline;"><code style="display: inline;" class="language-python qcm">{answer[sep:-1]}</code></pre>"""
        return answer

    indices = [i for i in range(len(list_answers))]
    if shuffle: random.shuffle(indices)

    dict_correspondance = {indices[i] : i for i in range(len(list_answers))}
    inv_dict_correspondance = {i : indices[i] for i in range(len(list_answers))}
    
    id = generate_id()
    html_element = f"""<div class="wrapper_qcm" id = "qcm_{id}" data-n-correct = {len(list_correct)}>"""
    for i in range(len(list_answers)):
        answer = list_answers[inv_dict_correspondance[i]]
        if type(answer) != str : 
            try: 
                answer = str(answer)
            except:
                answer = "Erreur de format"
        answer = codeblockify(latexify(answer))
        id_answer = f"""{id}-{i}""" 
        correct_answer = "correct" if inv_dict_correspondance[i] in list_correct else "incorrect"
        html_element += f"""{spanify(buttonify(answer, id_answer, correct_answer))}"""
    html_element += "</div>"

    return html_element