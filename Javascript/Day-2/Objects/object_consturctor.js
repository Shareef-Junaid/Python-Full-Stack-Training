var person = function () {
    this.firstName = "Bill";
    this.lastName =  "B";
    this.age = 25;
    this.address = {
        City: "Paris",
        Country:"France"
    }
    this.getFullName = function () {
        return this.firstName + " " + this.lastName;
    }
}