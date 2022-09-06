var cookie=document.querySelector(".stop");
function fun(){
    cookie.remove()
}

function city(element){
    alert("Loading weather report...")
}




var temp1 = document.querySelectorAll("#deg3");
function convert(elem) {
    if(elem.value=="Fahrenheit"){
        console.log("F");
        for (var i=0; i<temp1.length; i++){
            // console.log(temp1[i].innerText);
            temp1[i].innerText=Math.floor((parseInt(temp1[i].innerText)*1.8+32)*10/10)+"°";
        }
    }

  else  if(elem.value=="celsius"){
    console.log("c");
        for (var i=0; i<temp1.length; i++){
            temp1[i].innerText=Math.ceil(((parseInt(temp1[i].innerText)-32)/1.8)*10/10)+"°";
        }
    }
}

