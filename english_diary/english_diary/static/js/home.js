$( document ).ready(function() {
    $('#datepicker').datepicker();

    // Auto click today after page is loaded
    $('.active').trigger('click');
    $('.active').addClass('diary-selected');

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
                        $('#diary-delete').attr("disabled", false);
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
                $('#diary-translated-content').val("");
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
        var special_pattern = /[`~!@#$%^&*|\\\'\";:\/?]/gi;
        if(findWord) {
            // Check blank and special letters
            if(special_pattern.test(findWord))
                alert("특수문자는 입력할 수 없습니다.");
            else {
                // Blank => "+"
                findWord.replace(" ","+");
                var naverDictionaryAPIUrl = "/api/naver/dict/" + findWord;
                $.ajax({
                    type: "GET",
                    url: naverDictionaryAPIUrl,
                    success: function(data) {
                        $("#modal-searched-word").text(data.searched_word);
                        if(data.word_meaning)
                            $("#modal-word-meaning").text(data.word_meaning);
                        else
                            $("#modal-word-meaning").text("검색결과가 없습니다.");
                        $('#dictionaryModal').modal('show');
                    },
                    error: function(error) {
                        console.log(error);
                    }
                });
            }
        }
        else {
            alert("검색어를 입력하세요");
        }
        return false;
    });

    // Translate
    $('#diary-translate').click(function() {
        if($("form")[0].checkValidity()) {
            var diaryTranslateAPIUrl = "/api/naver/translate/";
            var diaryContentTextareaElement = $("#diary-content");
            var diaryTranslatedContentTextareaElement = $("#diary-translated-content");
           
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
                    var diaryTranslatedContent = data.content;
                    diaryTranslatedContentTextareaElement.val(diaryTranslatedContent);
                },
                error: function(error) {
                    console.log(error);
                }
            });
            return false;
        }
    });

    // Clipboard 
    $('#clipboard').click(function() {
        var diaryClipboardAPIUrl = "/api/clipboard/";
        var diaryContent = $("#diary-content").val();
        var data = {
            content: diaryContent
        };
        
        $.ajax({
            type:"POST",
            data: data,
            url: diaryClipboardAPIUrl,
            success: function(data) {
                alert("클립보드에 복사되었습니다.");
            },
            error: function(error) {
                console.log(error);
            }
        });
        return false;
    });
});
