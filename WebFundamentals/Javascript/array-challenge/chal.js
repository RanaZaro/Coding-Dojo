
function alwaysHungry(arr) {
    
    
    for(var i=0; i<arr.lenght; i++);
    if (arr[i]=="food"){
        console.log("yummy");
    }
   
    else{
       (arr[i]!="food")
        console.log("I'm hungry");
    }
    return alwaysHungry;
}
   
alwaysHungry([3.14, "food", "pie", true, "food"]);

alwaysHungry([4, 1, 5, 7, 2]);




function highPass(arr, cutoff) {
    var filteredArr = [];
   for(var i=0; i<arr.lenght; i++){
   if(arr[i]>cutoff){
    filteredArr.pop(arr[i]);
   }
}
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);



function betterthanaverage (arr){
    var sum = 0;
    for(var i=0; i<arr.length; i++){
        sum+= arr[i];
    }
    var avg = sum / arr.length;
    var count = 0;

    for (var i =0; i<arr.length; i++){
        if(arr[i]>avg){
            count++
        }
    }

    return count;
}

var result = betterthanaverage([6, 8, 3, 10, -2, 5, 9]);


function reverse (arr){
    var left =0;
    var right = arr.length-1;
    while (left < right){
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;

    }

    return arr;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log (result);


function fibonacciArray(n){
    var fibarr = [0,1];
    while(fibarr.length<n){
        var prev = fibarr[fibarr.length-1];
        var prevprev = fibarr[fibarr.length-2];
        fibarr.push(prfev + prevprev);

    }

    return fibarr;
}

var result = fibonacciArray(10);
console.log(result);


