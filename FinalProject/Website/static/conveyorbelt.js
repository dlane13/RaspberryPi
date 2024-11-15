var button = $("#conveyor_button");
button.click(function() {
    $.ajax({
        url: "/conveyor_on",
        type: "post",
        success: function(response) {
            console.log(response);
        }
    });
});
