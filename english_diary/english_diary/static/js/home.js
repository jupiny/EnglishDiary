$( document ).ready(function() {
    $('#datepicker').datepicker();

    // Auto click today after page is loaded
    $('.active').trigger('click');

    // Create Diary
    $('#diary-save').click(function() {
        if($("form")[0].checkValidity()) {
            var diaryContent = $('#diary-content').val();
            var diaryDatetime = $('#diary-datetime').val();
            var diaryCreateAPIUrl = "/api/diary/";
            var data = {
                datetime: diaryDatetime,
                content: diaryContent
            };
            $.ajax({
                type: "POST",
                url: diaryCreateAPIUrl,
                data: data,
                success: function(data) {
                    if(data.result) {
                        alert("저장되었습니다.");
                        $('.diary-selected').addClass('diary-written');
                    }
                    else {
                        alert("한글을 쓰시면 안되요!");
                    }
                },
                error: function(error) {
                    console.log(error);
                }
            });
            return false;
        }
    });

    // Delete Diary
    $('#diary-delete').click(function() {
        var diaryDatetime = $('#diary-datetime').val();
        var diaryDeleteAPIUrl = "/api/diary/" + diaryDatetime;
        var data = {
            datetime: diaryDatetime,
        };
        $.ajax({
            type: "DELETE",
            url: diaryDeleteAPIUrl,
            data: data,
            success: function(data) {
                alert("삭제되었습니다.");
                $('#diary-content').val("");
                $('.diary-selected').removeClass('diary-written');
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });

    // Dictionary
    $('#dictionary').click(function() {
        var findWord = $('#find-word').val();
        var naverDictionaryAPIUrl = "/api/naver/dict/" + findWord;
        $.ajax({
            type: "GET",
            url: naverDictionaryAPIUrl,
            success: function(data) {
                if(data.word_meaning)
                    alert(data.word_meaning);
                else
                    alert("검색결과가 없습니다.")
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });

    // Translate
    $('#diary-translate').click(function() {
        var diaryTranslateAPIUrl = "/api/naver/translate/";
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