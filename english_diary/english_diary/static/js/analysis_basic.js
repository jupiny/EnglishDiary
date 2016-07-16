$(document).ready(function() {
    $('#analysis_basic').click(function() {

        var diaryWrittenElement = $(".day.diary-written").not(".new").not(".old");
        var countDiaryWrittenElement = diaryWrittenElement.length; 
        var message = "한 달중 쓴 총 일기 : "+countDiaryWrittenElement;
        alert(message);
    });
});
