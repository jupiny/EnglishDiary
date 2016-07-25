$( document ).ready(function() {
    // https://github.com/ifightcrime/bootstrap-growl
    var message = $('#message').text();

    if(message) {
        $.bootstrapGrowl(message, {
              ele: 'body', // which element to append to
          type: 'success', // (null, 'info', 'danger', 'success')
            offset: {from: 'top', amount: 20}, // 'top', or 'bottom'
          align: 'right', // ('left', 'right', or 'center')
            width: 250, // (integer, or 'auto')
              delay: 4000, // Time while the message will be displayed. It's not equivalent to the *demo* timeOut!
          allow_dismiss: true, // If true then will display a cross to close the popup.
          stackup_spacing: 10 // spacing between consecutively stacked growls.
        });
    }
});
