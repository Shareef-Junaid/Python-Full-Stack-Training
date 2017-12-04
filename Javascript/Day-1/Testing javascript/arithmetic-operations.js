/*var num1 =2;
var num2 =2;

result = num1+num2;

document.write("Result : ", result);*/

function keywaspressed() {
    document.getElementById("val1msg").textContent = "value was entered";
}

function addNumbers() {
    var val1 = parseInt(document.getElementById("val1").value);
    var val2 = parseInt(document.getElementById("val2").value);
    if(isNaN(val1))
    {
        //alert("Please enter valid number for value1 ");
        document.getElementById("val1msg").textContent = "Please enter valid number for value1";
        return; // Stop the execution
    }
    else if(isNaN(val2))
    {
        //alert("Please enter valid number for value2 ");
        document.getElementById("val2msg").textContent = "Please enter valid number for value2 ";
        return; // Stop the execution
    }
    else{
        var result = document.getElementById("answer");
        result.value = val1 + val2;

    }

}