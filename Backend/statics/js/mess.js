let total1 = 0;
let total2 = 0;
let total3 = 0;
let total4 = 0;
let total5 = 0;
let total6 = 0;

function increment_value_1() {
    document.getElementById('number_quant_1').style.color = 'black';
    document.getElementById('temp_quant_1').style.color = 'black';

    var count = parseInt(document.getElementById('number1').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number1').value = count;
    document.getElementById('number_quant_1').innerHTML = count;
    total1 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;

}

function decrement_value_1() {
    var count = parseInt(document.getElementById('number1').value, 10);

    if (count > 0) count = count - 1;
    document.getElementById('number1').value = count;
    document.getElementById('number_quant_1').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_1').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_1').style.color = 'rgba(33,37,41,0.35)';

    }
    total1 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function MyFunc_1() {
    var count = parseInt(document.getElementById('number1').value, 10);
    document.getElementById('number_quant_1').innerHTML = count;


    var pount = parseInt(document.getElementById('number2').value, 10);
    document.getElementById('number_quant_2').innerHTML = pount;

    var zount = parseInt(document.getElementById('number3').value, 10);
    document.getElementById('number_quant_3').innerHTML = zount;

    var dount = parseInt(document.getElementById('number4').value, 10);
    document.getElementById('number_quant_4').innerHTML = dount;

    var gount = parseInt(document.getElementById('number5').value, 10);
    document.getElementById('number_quant_5').innerHTML = gount;

    var kount = parseInt(document.getElementById('number6').value, 10);
    document.getElementById('number_quant_6').innerHTML = kount;



}

function increment_value_2() {
    document.getElementById('number_quant_2').style.color = 'black';
    document.getElementById('temp_quant_2').style.color = 'black';
    var count = parseInt(document.getElementById('number2').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number2').value = count;
    document.getElementById('number_quant_2').innerHTML = count;
    total2 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;


}

function decrement_value_2() {
    var count = parseInt(document.getElementById('number2').value, 10);

    if (count > 0) count = count - 1;
    document.getElementById('number2').value = count;
    document.getElementById('number_quant_2').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_2').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_2').style.color = 'rgba(33,37,41,0.35)';

    }
    total2 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function increment_value_3() {
    document.getElementById('number_quant_3').style.color = 'black';
    document.getElementById('temp_quant_3').style.color = 'black';

    var count = parseInt(document.getElementById('number3').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number3').value = count;
    document.getElementById('number_quant_3').innerHTML = count;

    total3 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;

}

function decrement_value_3() {
    var count = parseInt(document.getElementById('number3').value, 10);



    if (count > 0) count = count - 1;
    document.getElementById('number3').value = count;
    document.getElementById('number_quant_3').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_3').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_3').style.color = 'rgba(33,37,41,0.35)';

    }
    total3 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function increment_value_4() {
    document.getElementById('number_quant_4').style.color = 'black';
    document.getElementById('temp_quant_4').style.color = 'black';

    var count = parseInt(document.getElementById('number4').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number4').value = count;
    document.getElementById('number_quant_4').innerHTML = count;

    total4 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;

}

function decrement_value_4() {
    var count = parseInt(document.getElementById('number4').value, 10);



    if (count > 0) count = count - 1;
    document.getElementById('number4').value = count;
    document.getElementById('number_quant_4').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_4').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_4').style.color = 'rgba(33,37,41,0.35)';

    }
    total4 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function increment_value_5() {
    document.getElementById('number_quant_5').style.color = 'black';
    document.getElementById('temp_quant_5').style.color = 'black';

    var count = parseInt(document.getElementById('number5').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number5').value = count;
    document.getElementById('number_quant_5').innerHTML = count;

    total5 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;

}

function decrement_value_5() {
    var count = parseInt(document.getElementById('number5').value, 10);



    if (count > 0) count = count - 1;
    document.getElementById('number5').value = count;
    document.getElementById('number_quant_5').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_5').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_5').style.color = 'rgba(33,37,41,0.35)';

    }
    total5 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function increment_value_6() {
    document.getElementById('number_quant_6').style.color = 'black';
    document.getElementById('temp_quant_6').style.color = 'black';
    var count = parseInt(document.getElementById('number6').value, 10);

    if (count < 9) count = count + 1;
    document.getElementById('number6').value = count;
    document.getElementById('number_quant_6').innerHTML = count;

    total6 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;

}

function decrement_value_6() {
    var count = parseInt(document.getElementById('number6').value, 10);



    if (count > 0) count = count - 1;
    document.getElementById('number6').value = count;
    document.getElementById('number_quant_6').innerHTML = count;
    if (count == 0) {
        document.getElementById('number_quant_6').style.color = 'rgba(33,37,41,0.35)';
        document.getElementById('temp_quant_6').style.color = 'rgba(33,37,41,0.35)';

    }

    total6 = count * 30;
    document.getElementById('Total_Extras').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
    document.getElementById('Final').innerHTML = total1 + total2 + total3 + total4 + total5 + total6;
}

function Confirm() {
    user.Messorders
}