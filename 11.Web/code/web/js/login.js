// 익명함수로 처리, 왜냐하면 전역변수로 설정시, 사용자가 확인할 수 있기 때문에
(function(){
    var Msg ={
        success : "Login Your Account.",
        fail : "Check Your Account."
    }

    var Event = {
        login: function(){
            $('#login-btn').on('click', function(){
                var params = {
                    emailL: $('#email').val(),
                    pw: $('#pw').val(),
                };
                if (params.emailL ==='admin@sample.com' && params.pw==='1234'){
                    $('.msg').text(Msg.success);
                    location.href = './contents.html';
                }else{
                    $('.msg').text(Msg.fail);
                };
                $('.msg').show();
                console.log(email,pw);
            })
        },
    }
    Event.login();
})();

