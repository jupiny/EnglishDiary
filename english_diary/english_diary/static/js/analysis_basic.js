$(document).ready(function() {
    $('#analysis_basic').click(function() {
        
        //count diary written
        var diaryWrittenElement = $(".day.diary-written").not(".new").not(".old");
        var countDiaryWritten = diaryWrittenElement.length; 
        
        //count days in a present month
        var countDaysInMonth = $(".day").not("new").not(".old").length;

        //calculate achievement
        var achievementString =  Math.round(countDiaryWritten / countDaysInMonth * 100).toString() + "%";
       
        //var achievementMessage = " 달성중"

        $(".progress-bar").css({
            "width": achievementString
        });

        $(".progress-bar").text(achievementString);
    });
});
