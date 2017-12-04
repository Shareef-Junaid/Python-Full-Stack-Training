function callme() {
    document.getElementById("msg").textContent = "I was called from function";
}

function caller(callback) {
    callback();
}
