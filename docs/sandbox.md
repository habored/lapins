# Bac à sable

<!-- {{IDE()}}
{{IDE()}} -->

<!-- <div class = "can_wrapper">
<canvas id ="tracer" width="500" height="300"></canvas>
<canvas id="pointer" width="500" height="300"></canvas>
</div> -->

<script type="text/javascript">
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
</script>