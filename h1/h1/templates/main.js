$(document).ready(function() {
    //Navigation button behavior
    $(".nav-tab").on('click', function() {
        $(".content-page").addClass("hidden");
        var id = $(this).attr('id');
        $("."+id).removeClass("hidden");
    });

    //Select ride button behavior
    $("#select-ride").on('click', function() {
        $(".content-page").addClass("hidden");
        $(".ride-profile").removeClass("hidden");
    });
    
    //Post ride button behavior
});