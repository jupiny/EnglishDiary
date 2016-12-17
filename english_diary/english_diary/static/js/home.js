$( document ).ready(function() {
    $('#datepicker').datepicker();

    // Auto click today after page is loaded
    $('.active').trigger('click');
    $('.active').addClass('diary-selected');

    // Create Diary
    $('#diary-save').click(function() {
        if($("form")[0].checkValidity()) {
            var diaryContent = $('#diary-content').val();
            var diaryDatetime = $('#selected-datetime').val();
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
        var diaryDatetime = $('#selected-datetime').val();
        var diaryDeleteAPIUrl = "/api/diary/" + diaryDatetime;
        var data = {
            datetime: diaryDatetime,
        };
        if (confirm('정말 일기를 삭제하시겠습니까?')) {
            $.ajax({
                type: "DELETE",
                url: diaryDeleteAPIUrl,
                data: data,
                success: function(data) {
                    $('#diary-content').val("");
                    $('#diary-translated-content').val("");
                    $('.diary-selected').removeClass('diary-written');
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
        return false;
    });

    // Trigger a button click with JavaScript on the Enter key in a text box
    $("#find-word").keyup(function(event){
        if(event.keyCode == 13){
            $("#dictionary").click();
        }
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
    var clipboard = new Clipboard('#clipboard');
    clipboard.on('success', function(e) {
        e.clearSelection();
    });
    $('[data-toggle="tooltip"]').tooltip({
            trigger : 'focus'
    })


    // Analysis
    $('#analysis-basic').click(function() {

        //count diary written
        var diaryWrittenElement = $(".day.diary-written").not(".new").not(".old");
        var countDiaryWritten = diaryWrittenElement.length;

        //count days in a present month
        var countDaysInMonth = $(".day").not(".new").not(".old").length;

        //calculate achievement
        var achievementInt = Math.round(countDiaryWritten / countDaysInMonth * 100);
        var achievementString =  achievementInt.toString() + "%";

        //var achievementMessage = " 달성중"

        // Setting progress bar
        $(".progress-bar").css({
            "width": achievementString
        });
        $(".progress-bar").text(achievementString);

        // Clear existing class
        $(".progress-bar")
            .removeClass("progress-bar-danger")
            .removeClass("progress-bar-warning")
            .removeClass("progress-bar-info")
            .removeClass("progress-bar-success")

        if(achievementInt < 20)
            $(".progress-bar").addClass("progress-bar-danger");
        else if(achievementInt < 50)
            $(".progress-bar").addClass("progress-bar-warning");
        else if(achievementInt < 70)
            $(".progress-bar").addClass("progress-bar-info");
        else
            $(".progress-bar").addClass("progress-bar-success");

        var currentYearMonth = $("#current-year-month").val();
        var currentYear = currentYearMonth.split("/")[0];
        var currentMonth = Number(currentYearMonth.split("/")[1]);
        var formattedCurrentYearMonth = currentYear+"년 "+currentMonth+"월";
        $("#count-days-in-month").text(countDaysInMonth);
        $("#count-diary-written").text(countDiaryWritten);
        $(".formatted-current-year-month").text(formattedCurrentYearMonth);

        var diaryMonthlyWordsAPIUrl = "/api/diary/"+currentYearMonth+"words";
        $.ajax({
            type: "GET",
            url: diaryMonthlyWordsAPIUrl,
            success: function(data) {
                $("#monthly-words-count").text(data.count);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

function autoSave(){
if($("form")[0].checkValidity()) {
    var diaryContent = $('#diary-content').val();
    var diaryDatetime = $('#selected-datetime').val();
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
                $.bootstrapGrowl("자동저장 되었습니다.", {
                      ele: 'body', // which element to append to
                  type: 'info', // (null, 'info', 'danger', 'success')
                    offset: {from: 'top', amount: 20}, // 'top', or 'bottom'
                  align: 'right', // ('left', 'right', or 'center')
                    width: 250, // (integer, or 'auto')
                      delay: 2000, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
                  allow_dismiss: true, // If true then will display a cross to close the popup.
                  stackup_spacing: 10 // spacing between consecutively stacked growls.
                });
                $('.diary-selected').addClass('diary-written');
                $('#diary-delete').attr("disabled", false);
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
    return false;
  }
}
