# Bac à sable

{{terminal()}}

<canvas width="500" height="300">
  Désolé, votre navigateur ne prend pas en charge &lt;canvas&gt;.
</canvas>
<script>
var canvas = document.querySelector('canvas');
var ctx = canvas.getContext('2d');
ctx.fillStyle = 'white';
ctx.fillRect(10, 10, 300, 300);
ctx.beginPath()
ctx.moveTo(10, 10)
ctx.lineTo(310, 310)
ctx.stroke()

function boum(L) {
        var canvas = document.querySelector('canvas');
        var ctx = canvas.getContext('2d');
        ctx.beginPath()
        console.log('ligne 57', ctx)
        ctx.moveTo(50, 50)
        ctx.lineTo(50+L, 50)
        ctx.stroke()
    }

</script>