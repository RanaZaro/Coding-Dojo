function pizza(crustType1,sauceType1,cheeses1,toppings1){
    var pizza = {};
    pizza.crustType = crustType1
    pizza.sauceType = sauceType1
    pizza.cheeses = cheeses1
    pizza.toppings = toppings1

    return pizza;

}

var pizza1 = pizza("deep dish", "traditional", "mozzarella", ["pepperoni", "sausage"]);

console.log(pizza1);


var pizza2 = pizza("hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"]);

console.log(pizza2);


var pizza3 = pizza("wheat", "barbique","feta", "mushrooms");


console.log(pizza3);

var pizza4 = pizza("bread", "katchup", "chedder", "sausage");

console.log(pizza4);
