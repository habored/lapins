# Bac à sable

{{IDE('exo_test/exo', MAX = 3)}}

{{IDE('exo_test_HDR/exo', MAX = 3)}}

<!--<p id="formule" class="arithmatex">
\(x=3\)
</p>
<div id="formule" class="arithmatex">
\(x=3\)
</div>

<div id="formule" class="arithmatex">
\[
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
\]
</div>

<div id="formule" class="arithmatex">
$$
\operatorname{ker} f=\{g\in G:f(g)=e_{H}\}{\mbox{.}}
$$
</div>

$x=3$

<input type="button" onclick="MAJ_formule()" value="Mise à jour">-->

<!-- <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script> -->
<!-- <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js?"></script> -->
<!--<script>
function MAJ_formule() {
  let valeur = Math.floor(Math.random() * 10)
  console.log(valeur)
  document.getElementById("formule").innerHTML = "\\( x = \\sqrt{" + valeur + "}\\)"
	MathJax.typeset()}
</script>-->


<!--
{{multi_qcm(
  ["Age du capitaine ?", ["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D", '42'], [1,2, 5]],
  ["1+1=?", ["$12$", "2", "Je sais pas", "L'age du capitaine"], [2]],
  ["${x}^{p} = ?$", ["${x}^{p}$", "${x}+{p}$", "Je sais pas", "L'age du capitaine"], [1], {'x' : [8, 2], 'p' : 7} ]
)}}-->

<!-- <span id="truc_m">$x^p$</span>

<div id="frame">

<h1>MathJax v3: TeX &amp; MathML to HTML</h1>

<textarea id="input" rows="15" cols="10">

If $a \ne 0$, then $ax^2 + bx + c = 0$ has two solutions,
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

As MathML:
<math>
  <mi>a</mi>
  <msup>
    <mi>x</mi>
    <mn>2</mn>
  </msup>
  <mo>+</mo>
  <mi>b</mi>
  <mi>x</mi>
  <mo>+</mo>
  <mi>c</mi>
  <mo>=</mo>
  <mn>0</mn>
</math>.
</textarea>
<br />
<div class="right">
<input type="button" value="Render HTML" id="render" onclick="convert()"/>
</div>
<br clear="all" />
<div id="output"></div>
</div>

  <script>
    function convert() {
      //
      //  Get the input (it is HTML containing delimited TeX math
      //    and/or MathML tags
      //
      var input = document.getElementById("input").value.trim();
      //
      //  Disable the render button until MathJax is done
      //
      var button = document.getElementById("render");
      button.disabled = true;
      //
      //  Clear the old output
      //
      output = document.getElementById('output');
      output.innerHTML = input;
      //
      //  Reset the tex labels (and automatic equation numbers, though there aren't any here).
      //  Reset the typesetting system (font caches, etc.)
      //  Typeset the page, using a promise to let us know when that is complete
      //
      MathJax.texReset();
      MathJax.typesetClear();
      MathJax.typesetPromise()
        .catch(function (err) {
          //
          //  If there was an internal error, put the message into the output instead
          //
          output.innerHTML = '';
          output.appendChild(document.createElement('pre')).appendChild(document.createTextNode(err.message));
        })
        .then(function() {
          //
          //  Error or not, re-enable the render button
          //
          button.disabled = false;
        });
    }
  </script> -->


 <!-- <div id = "setQCM"> -->
<!-- Question 1:

{{ qcm(["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D"], [1,2]) }} -->
<!-- 
Question 2:

{{ qcm(["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D"], [1,2]) }}

Question 3:

{{ qcm(["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D"], [1,2]) }}

<div class="buttonWrapper">
<span class = "validationButton" id = "valider">Valider</span>
<span class = "validationButton" id = "recharger">Recharger</span>
</div>
<div class = "showScore" id="score"></div>
</div> -->

<!-- {{IDE()}}
{{IDE()}} -->

<!-- <div class = "can_wrapper">
<canvas id ="tracer" width="500" height="300"></canvas>
<canvas id="pointer" width="500" height="300"></canvas>
</div> -->

<!-- <script type="text/javascript">
// // jQuery cross domain ajax
// $.get("http://www.example.org/ajax.php").done(function (data) {
//     console.log(data);
// });

// // using XMLHttpRequest
// var xhr = new XMLHttpRequest();
// xhr.open("GET", "http://www.example.org/ajax.php", true);
// xhr.onload = function () {
//     console.log(xhr.responseText);
// };
// xhr.send();

// using the Fetch API
const myInit = {
  method: 'GET',
  mode: 'no-cors',
  cache: 'default',
};

fetch("https://gitlab.com/bouillotvincent/tests-avec-mkdocs/-/blob/main/main.py", myInit)
    .then(function(response) {
        return response.blob();
    })
    .then(function(myBlob) {
    const objectURL = URL.createObjectURL(myBlob);
    console.log(objectURL);
    });
</script> -->