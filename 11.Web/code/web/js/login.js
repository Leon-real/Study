$('#login-btn').on('click', function(){
    var params = {
        emailL: $('#email').val(),
        pw: $('#pw').val(),
    };
    if (params.emailL ==='admin@sample.com' && params.pw==='1234'){
        console.log('success');
    }else{
        console.log('Fail');
    }
    console.log(email,pw);
})