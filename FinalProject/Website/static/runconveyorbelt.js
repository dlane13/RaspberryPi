function conveyor(onSuccess) {
    $.ajax({
        url: "conveyor_button",
        dataType: "json",
        type: "GET",
        success: function(response) {
            onSuccess(response);
        }
    });
}

$("#conveyor_button").on("click", function() {
    conveyor(function(decimal) {
        $("#decimal").text(decimal);
    });
});
