var world = [],
    n = [],
    m = []

function generN(x) {
    for (var i = 0; i < x; i++) {
        if (i % 2 === 1) {
            n[i] = 1
        } else {
            n[i] = 0
        }
    }
}

function generM(x) {
    for (var i = 0; i < x; i++) {
        if (i % 2 === 0) {
            m[i] = 1
        } else { m[i] = 0 }
    }
}
y = document.getElementById('col').innerText
generM(y);
generN(y);
console.log(m);
console.log(n);

function creatworld(y, n, m) {

    for (var i = 0; i < y; i++) {
        if (i % 2 === 1) {
            world[i] = m;
        } else {
            world[i] = n;
        }
    }

}

x = document.getElementById('number').innerText
creatworld(x, n, m);
console.log(world);




class_name1 = document.getElementById('class_name1').innerText
class_name2 = document.getElementById('class_name2').innerText
console.log(class_name1, class_name2)
var colorobj = {
    0: 'none_color',
    1: 'none_color'
}

function color(name1, name2) {
    colorobj[0] = name1;
    colorobj[1] = name2;
}
color(class_name1, class_name2);
console.log(colorobj);

function drwaworld() {
    var output = ''
    for (var i = 0; i < world.length; i++) {
        output += "<div class='row'>"
        for (var j = 0; j < world[i].length; j++) {
            output += "<div class='cube' style='background-color:" + colorobj[world[i][j]] + "'></div>"
        }
        output += "</div>"
    }
    console.log(output);
    document.getElementById('wrapper').innerHTML = output
}
drwaworld();