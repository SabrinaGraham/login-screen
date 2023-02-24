$(document).ready(function(){
    $('.btn').click(function(e){
        $.ajax({
            url:'',
            type:'GET',
            contentType: 'application/json',
            data:{
                btn_text: $(this).text(),
                username: $('#username').val(),
                password: $('#password').val(),
            },            
        })
        .done(function(){
            if (document.getElementById('username').validity.valueMissing){
                alert('Username is required!!!');
                return false;
            }
            if (document.getElementById('password').validity.valueMissing){
                alert('Password is required!!!');
                return false;
            }
        });
        e.preventDefault();
    })
});