$( document ).ready(function() {

    // Initialize radio button
    var userEmailNotificationAPIUrl = "/api/user/email_notification/";
    
    $.ajax({
        type:"GET",
        url: userEmailNotificationAPIUrl,
        success: function(data) {
            if(data.email_notification)
                $('#on').prop('checked', true);
            else
                $('#off').prop('checked', true);
        },
        error: function(error) {
            console.log(error);
        }
    });

    // Change Email
    $('#change-email').click(function() {
        if($("form")[0].checkValidity()) {
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
        }
    });

    // Change Password 
    $('#change-password').click(function() {
        if($("form")[1].checkValidity()) {
            var userPasswordAPIUrl = "/api/user/password/";
            var currentPassword = $("#current-password").val();
            var newPassword = $("#new-password").val();
            var confirmNewPassword = $("#confirm-new-password").val();

            var data = {
                current_password: currentPassword,
                new_password: newPassword,
                confirm_new_password: confirmNewPassword,
            };
            
            $.ajax({
                type:"PATCH",
                data: data,
                url: userPasswordAPIUrl,
                success: function(data) {
                    var alertMessage = "";
                    if(data.is_current_password_valid && data.does_match_confirm_password)
                        alertMessage += "변경되었습니다. ";
                    else {
                        if(!data.is_current_password_valid)
                            alertMessage += "현재 비밀번호가 맞지 않습니다. ";
                            
                        if(!data.does_match_confirm_password)
                            alertMessage += "새 비밀번호가 일치하지 않습니다. ";
                    }
                    alert(alertMessage);
                },
                error: function(error) {
                    console.log(error);
                }
            });
            return true;
        }
    });

    // Change Email Notification
    $('input[name="radio"]').click(function() {
        var radioInputElement = $(this);
        var email_notification = $(radioInputElement).val();
        var userEmailNotificationAPIUrl= "/api/user/email_notification/";
        var data = {
            email_notification: email_notification, 
        };
        
        $.ajax({
            type:"PATCH",
            data: data,
            url: userEmailNotificationAPIUrl,
            success: function(data) {
                $(radioInputElement).prop('checked', true);
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });

    // Delete User 
    $('#delete-user').click(function() {
        var userDeleteAPIUrl= "/api/user/delete/";
        
        if (confirm('정말 계정을 삭제하시겠습니까?')) {
            $.ajax({
                type:"DELETE",
                url: userDeleteAPIUrl,
                success: function(data) {
                    window.location.href = "/signin/";
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
        return false;
    });
});
