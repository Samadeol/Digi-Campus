function increment_value_1(){
    document.getElementById('number_quant_1').style.color='black';
    document.getElementById('temp_quant_1').style.color='black';
    
    var count=parseInt(document.getElementById('number1').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number1').value=count;
    document.getElementById('number_quant_1').innerHTML=count;

}
function decrement_value_1(){
    var count=parseInt(document.getElementById('number1').value,10);
    
    if(count>0) count=count-1;
    document.getElementById('number1').value=count;
    document.getElementById('number_quant_1').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_1').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_1').style.color='rgba(33,37,41,0.35)';

    }
}
function MyFunc_1(){
    var count=parseInt(document.getElementById('number1').value,10);
    document.getElementById('number_quant_1').innerHTML=count;


    var pount=parseInt(document.getElementById('number2').value,10);
    document.getElementById('number_quant_2').innerHTML=pount;

    var zount=parseInt(document.getElementById('number3').value,10);
    document.getElementById('number_quant_3').innerHTML=zount;

    var dount=parseInt(document.getElementById('number4').value,10);
    document.getElementById('number_quant_4').innerHTML=dount;

    var gount=parseInt(document.getElementById('number5').value,10);
    document.getElementById('number_quant_5').innerHTML=gount;

    var kount=parseInt(document.getElementById('number6').value,10);
    document.getElementById('number_quant_6').innerHTML=kount;


    
}
function increment_value_2(){
    document.getElementById('number_quant_2').style.color='black';
    document.getElementById('temp_quant_2').style.color='black';
    var count=parseInt(document.getElementById('number2').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number2').value=count;
    document.getElementById('number_quant_2').innerHTML=count;


}
function decrement_value_2(){
    var count=parseInt(document.getElementById('number2').value,10);
   
    if(count>0) count=count-1;
    document.getElementById('number2').value=count;
    document.getElementById('number_quant_2').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_2').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_2').style.color='rgba(33,37,41,0.35)';

    }
}

function increment_value_3(){
    document.getElementById('number_quant_3').style.color='black';
    document.getElementById('temp_quant_3').style.color='black';
    
    var count=parseInt(document.getElementById('number3').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number3').value=count;
    document.getElementById('number_quant_3').innerHTML=count;

}
function decrement_value_3(){
    var count=parseInt(document.getElementById('number3').value,10);
    
   

    if(count>0) count=count-1;
    document.getElementById('number3').value=count;
    document.getElementById('number_quant_3').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_3').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_3').style.color='rgba(33,37,41,0.35)';

    }
}

function increment_value_4(){
    document.getElementById('number_quant_4').style.color='black';
    document.getElementById('temp_quant_4').style.color='black';
    
    var count=parseInt(document.getElementById('number4').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number4').value=count;
    document.getElementById('number_quant_4').innerHTML=count;

}
function decrement_value_4(){
    var count=parseInt(document.getElementById('number4').value,10);
    
   

    if(count>0) count=count-1;
    document.getElementById('number4').value=count;
    document.getElementById('number_quant_4').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_4').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_4').style.color='rgba(33,37,41,0.35)';

    }
}

function increment_value_5(){
    document.getElementById('number_quant_5').style.color='black';
    document.getElementById('temp_quant_5').style.color='black';
    
    var count=parseInt(document.getElementById('number5').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number5').value=count;
    document.getElementById('number_quant_5').innerHTML=count;

}
function decrement_value_5(){
    var count=parseInt(document.getElementById('number5').value,10);
    
  

    if(count>0) count=count-1;
    document.getElementById('number5').value=count;
    document.getElementById('number_quant_5').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_5').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_5').style.color='rgba(33,37,41,0.35)';

    }
}

function increment_value_6(){
    document.getElementById('number_quant_6').style.color='black';
    document.getElementById('temp_quant_6').style.color='black';
    var count=parseInt(document.getElementById('number6').value,10);
    
    if(count<9) count=count+1;
    document.getElementById('number6').value=count;
    document.getElementById('number_quant_6').innerHTML=count;

}
function decrement_value_6(){
    var count=parseInt(document.getElementById('number6').value,10);
    
    

    if(count>0) count=count-1;
    document.getElementById('number6').value=count;
    document.getElementById('number_quant_6').innerHTML=count;
    if(count==0){
        document.getElementById('number_quant_6').style.color='rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_6').style.color='rgba(33,37,41,0.35)';

    }
}
