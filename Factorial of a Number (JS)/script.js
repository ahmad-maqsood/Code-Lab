// Factorial of a number
let a=prompt("Enter a number"); 
let b=a;  
let c=0;   

for(i=a;i!=1;i--){  

    a=a*--b;   
    
    a+=c;

}

console.log("Factorial: ",a);