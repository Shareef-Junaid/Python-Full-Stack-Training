function student(){
    this.firstName =  "Bill";
    var getName = function() {
        return this.firstName ;
    }
}