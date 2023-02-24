$(document).ready(function(){
    uname=document.getElementById('username');
    pswd=document.getElementById('password');
    msgbox=document.getElementById("msgbox");
    msgbox.setAttribute("hidden","hidden");
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
        if (uname.checkValidity() && pswd.checkValidity()){
            $.ajax({
            url:'',
            type:'POST',
            contentType: 'application/json',
            data:{}       
            })
            .done(function(response){
            
            msgbox.innerHTML = response.data
            msgbox.removeAttribute("hidden")
            });
        
        }
        
    })
    

       

});