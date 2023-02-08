var pw = document.getElementById("password");
var length1 = document.getElementById("length1");
var number = document.getElementById("number");
var lowercase = document.getElementById("lowercase");
var uppercase = document.getElementById("uppercase");
var special = document.getElementById("special");

pw.onkeyup = function() {
    if (pw.value.length >= 8){
        length1.style.display = "block";
        document.getElementById("l1").className = 'complete';
    } else {
        length1.style.display = "none";
        document.getElementById("l1").className = 'incomplete';
    }
    var numbers = /[0-9]/g;
    if(pw.value.match(numbers)) {
        number.style.display = "block";
        document.getElementById("num").className = 'complete';
    } else {
        number.style.display = "none";
        document.getElementById("num").className = 'incomplete';
    }
    var lowerCaseLetters = /[a-z]/g;
    if (pw.value.match(lowerCaseLetters)) {
        lowercase.style.display = "block";
        document.getElementById("l").className = 'complete';
    } else {
        lowercase.style.display = "none";
        document.getElementById("l").className = 'incomplete';
    }
    var upperCaseLetters = /[A-Z]/g;
    if (pw.value.match(upperCaseLetters)) {
        uppercase.style.display = "block";
        document.getElementById("u").className = 'complete';
    } else {
        uppercase.style.display = "none";
        document.getElementById("u").className = 'incomplete';
    }
    const specialChars = /[`!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?~]/;
    if (pw.value.match(specialChars)) {
        special.style.display = "block";
        document.getElementById("s").className = 'complete';
    } else {
        special.style.display = "none";
        document.getElementById("s").className = 'incomplete';
    }
    if (document.getElementById("l1").className === 'complete' & document.getElementById("num").className === 'complete' & document.getElementById("l").className === 'complete' & document.getElementById("u").className === 'complete' & document.getElementById("s").className === 'complete') {
        message.style.display = "block";
    } else {
        message.style.display = "none";
    };
}

function show() {  
    var getPasword = document.getElementById("password");  
    if (getPasword.type === "password") {  
      getPasword.type = "text";  
    } else {  
      getPasword.type = "password";  
    }  
  }  