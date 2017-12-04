var num1 = 10;
var num2 = 20;
show();

function show() {
    console.log("Value is :",num1);
}
var show = function () {
    console.log("Value is :", num2);
}
var show = function () {
    console.log("Value is 30");
}

show();