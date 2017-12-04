var person = function (p_firstName, p_lastName, p_age) {
    this.firstName = p_firstName || "Bill";
    this.lastName =  p_lastName || "B";
    this.age = p_age || 25;
    this.address = {
        City: "Paris",
        Country:"France"
    }
    this.getFullName = function () {
        return this.firstName + " " + this.lastName;
    }
    this.getAddress = function () {
        return this.address.City + " , " + this.address.Country;
    }
}