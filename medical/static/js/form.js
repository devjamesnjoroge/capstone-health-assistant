$(document).ready(function(){
    $('#btn1').click(function(){
        validatep1()
    })
    $('#btn2').click(function(){
        $('.p1').css('display', 'block')
        $('.p2').css('display', 'none')
    })
})

function validatep1(){
    if ($('#first_name').val() == '' | $('#second_name').val() == '' | $('#email').val() == ''){
        alert('Fill in all the inputs to proceed')
    } else{
        $('.p1').css('display', 'none')
        $('.p2').css('display', 'block')
    }
}