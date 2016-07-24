$( document ).ready(function() {

    // Change Email
    $('#change-email').click(function() {
        var userEmailAPIUrl = "/api/user/email/";
        var newEmail = $("#new-email").val();
        var data = {
            new_email: newEmail, 
        };
        
        $.ajax({
            type:"PATCH",
            data: data,
            url: userEmailAPIUrl,
            success: function(data) {
                alert("변경되었습니다.");
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
});
