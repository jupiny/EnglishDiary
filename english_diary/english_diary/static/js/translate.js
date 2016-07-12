$(document).ready(function() {
    $('#diary-translate').click(function() {
        var diaryTranslateAPIUrl = "/api/translate/";
        var diaryContentTextareaElement = $("#diary-content");
       
        // input 타입의 .val()로 받으세요(.text로 썼기에 에러났었음)
        var data = {
            content: diaryContentTextareaElement.val()
        };
        
        $.ajax({
            type:"POST",
            data: data,
            url: diaryTranslateAPIUrl,
       
            // translate.py 의 response 받기
            success: function(data) {
                var diaryContent = data.content;
               //TODO:alert 삭제
                alert(diaryContent);
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });

});
