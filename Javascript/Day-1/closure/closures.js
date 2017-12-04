/*function addNumbers(num1,num2) {
    var result = "Result is : ";

    //This inner function has access to the outer functions variables & parameters

    function add() {
        return result+(num1+num2); // Result is : "sum"
    }
    return add()
}
var result = addNumbers(10,20);
console.log(result);*/

function addNumbers(num1,num2) {
    var result = "Result is : ";

    //This inner function has access to the outer functions variables & parameters

    function add() {
        return result+(num1+num2); // Result is : "sum"
    }
    return add
}
// myFunc will contain the function body returned from the addNumbers()
// it needs to be executed to get the result

// 1 way of executing
var myFunc = addNumbers(10,20);
var result = myFunc();
console.log(result);

// 2 way of executing IIEFs
var myFunc = addNumbers(10,10)();
console.log(myFunc);




