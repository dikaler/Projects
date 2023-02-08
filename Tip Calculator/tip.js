function calculate() {
    var price = document.getElementById("price").valueAsNumber;
    var tip = document.getElementById("tip").valueAsNumber;
    console.log(tip);
    document.getElementById('tip-amount').innerHTML = ((price)*(tip/100)).toFixed(2);
    document.getElementById('tip-amount').value = (price)*(tip/100);
    var tipAmount = document.getElementById('tip-amount').value;
    document.getElementById('total').innerHTML = (price + tipAmount).toFixed(2);
};

