// String, console.log
let msg: string = "hello world!";
console.log(msg);

// string
let p1: string = "Steve";

// number
let radius: number = 182.225;

// Math: sin, cos
console.log("sin pi / 2 -->", Math.sin(Math.PI / 2));
console.log("sin pi / 6 -->", Math.sin(Math.PI / 6));

// array: number, boolean
let numbers: number[] = [4, 5, 6, 7];
let res: boolean[] = [true, false, true];

// any type
let uv: any = ["Awis", "Mirza", 4];

// tuple
let tp: [string, number, boolean] = ["Awis", 45, true];

// enum
enum doorState {
  "Open",
  "Closed",
  "Ajar"
}
console.log(doorState.Ajar);

// function
function log(val: any) {
  console.log(val);
}
log(doorState[1]);

// typed function
function tell_joke(): string {
  return "This is a joke.";
}

// union type (either type is valid)
var val_un: string | number;
val_un = 1;
val_un = "hello";

log(789 + "world");

// type guard function
function add_with_guard(
  argx: string | number,
  argy: string | number
): string | number {
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

// type alias
type StringOrNumber = string | number;

// Null & Undefined
function undef_fun1(test) {
  console.log("test parameter: ", test);
}
undef_fun1("undefined Value");
