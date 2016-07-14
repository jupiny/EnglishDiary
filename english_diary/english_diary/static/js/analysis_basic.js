$(document).ready(function() {
    $('#analysis_basic').click(function() {

        var diaryWrittenElement = $(".day.diary-written").not(".new");
        var countDiaryWrittenElement = diaryWrittenElement.length; 
        alert(countDiaryWrittenElement);
    });
});
