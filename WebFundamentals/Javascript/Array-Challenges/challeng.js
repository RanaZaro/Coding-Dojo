// var food =0;
function alwaysHungry(arr) {
    

    for( var i=0; i<arr.length;i++){
    if (arr[i]=="food"){
    	console.log ("yummy");
    }
    else{ (arr[i]!="food")
    	console.log ("I'm hungry'");
    
   }
}
 
}
    
alwaysHungry([3.14, "food", "pie", true, "food"]);

alwaysHungry([4, 1, 5, 7, 2]);


function highPass(arr, cutoff) {
    var filteredArr = [];
   for(var i=0; i<arr.lenght; i++){
   if(arr[i]<cutoff){
    filteredArr.pop(arr[i]);
   }
}
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result);
