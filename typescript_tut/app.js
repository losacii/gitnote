// String, console.log
var msg = "hello world!";
console.log(msg);
// string
var p1 = "Steve";
// number
var radius = 182.225;
// Math: sin, cos
console.log("sin pi / 2 -->", Math.sin(Math.PI / 2));
console.log("sin pi / 6 -->", Math.sin(Math.PI / 6));
// array: number, boolean
var numbers = [4, 5, 6, 7];
var res = [true, false, true];
// any type
var uv = ["Awis", "Mirza", 4];
// tuple
var tp = ["Awis", 45, true];
// enum
var doorState;
(function (doorState) {
    doorState[doorState["Open"] = 0] = "Open";
    doorState[doorState["Closed"] = 1] = "Closed";
    doorState[doorState["Ajar"] = 2] = "Ajar";
})(doorState || (doorState = {}));
console.log(doorState.Ajar);
// function
function log(val) {
    console.log(val);
}
log(doorState[1]);
// typed function
function tell_joke() {
    return "This is a joke.";
}
// union type (either type is valid)
var val_un;
val_un = 1;
val_un = "hello";
log(789 + "world");
// type guard function
function add_with_guard(argx, argy) {
    if (typeof argx === "string") {
        console.log("first argument is a string");
        return argx + argy;
    }
    if (typeof argx === "number" && typeof argy === "number") {
        console.log("both number arguments");
        return argx + argy;
    }
    return argx.toString() + argy.toString();
}
// Null & Undefined
function undef_fun1(test) {
    console.log("test parameter: ", test);
}
undef_fun1("undefined Value");
