$(document).ready(function() {
    $('#analysis-basic').click(function() {
        
        //count diary written
        var diaryWrittenElement = $(".day.diary-written").not(".new").not(".old");
        var countDiaryWritten = diaryWrittenElement.length; 
        
        //count days in a present month
        var countDaysInMonth = $(".day").not(".new").not(".old").length;

        //calculate achievement
        var achievementString =  Math.round(countDiaryWritten / countDaysInMonth * 100).toString() + "%";
       
        //var achievementMessage = " 달성중"

        $(".progress-bar").css({
            "width": achievementString
        });

        $(".progress-bar").text(achievementString);

        var currentYearMonth = $("#current-year-month").val();
        var currentYear = currentYearMonth.split("/")[0];
        var currentMonth = currentYearMonth.split("/")[1].replace("0", "");
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
