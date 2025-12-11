let a=Number(prompt("Enter first number"));
let opr=prompt("Enter Operation");
let b=Number(prompt("Enter second number"));
let random_number = Math.random();

// If I don't define the variables as "Number" , then JS would take those numbers as strings and instead of adding them, it would just write them together as : 6+3=63

console.log("Random no.: ",random_number);
console.log("First Number: ", a);
console.log("Operation: ", opr);
console.log("Second Number: ", b);

if(random_number<0.1){

if(opr=="+"){
    console.log("Result: ", a-b);
}
else if(opr=="*"){
    console.log("Result: ", a+b);
}
else if(opr=="-"){
    console.log("Result: ", a/b);
}
else if(opr=="/"){
    console.log("Result: ", a**b);
}
else{
    console.log("Wrong operations or input")
}
}


else{
   
    if(opr=="+"){
    console.log("Result: ", a+b);
}
else if(opr=="*"){
    console.log("Result: ", a*b);
}
else if(opr=="-"){
    console.log("Result: ", a-b);
}
else if(opr=="/"){
    console.log("Result: ", a/b);
}
else{
    console.log("Wrong operations or input")
}
}