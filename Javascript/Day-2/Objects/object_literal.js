var person = {
    firstName: "Bill",
    lastName:  "B",
    age:25,
    address:{
        City: "Paris",
        Country:"France"
    },
    getFullName : function () {
        return this.firstName + " " + this.lastName;
    }
}