$(document).ready(function(){
    uname=document.getElementById('username');
    pswd=document.getElementById('password');
    $('.btn').click(function(e){
        $.ajax({
            url:'',
            type:'GET',
            contentType: 'application/json',
            data:{
                btn_text: $(this).text(),
                username: $('#username').val(),
                password: $('#password').val(),
            }            
        })
        .done(function(){
            if (uname.validity.valueMissing){
                alert('Username is required!!!');
                return false;
            }
            if (pswd.validity.valueMissing){
                alert('Password is required!!!');
                return false;
            }
        });
        e.preventDefault();
    })

    $('.btn').click(function(e){
        $.ajax({
            url:'',
            type:'POST',
            contentType: 'application/json',
            data:{}       
        })
        .done(function(response){
            msgbox=document.getElementById("msgbox")
            msgbox.innerHTML = response.data
        });
        e.preventDefault();
    })
    

       

});