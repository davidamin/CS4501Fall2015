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
    
    $("#adv-search-button").on('click', function() {
        if ($("#adv-search-span").hasClass("glyphicon-triangle-bottom")) {
            $("#adv-search-span").addClass("glyphicon-triangle-top");
            $("#adv-search-span").removeClass("glyphicon-triangle-bottom");
            $("#adv-search-group").removeClass("hidden");
        } else if ($("#adv-search-span").hasClass("glyphicon-triangle-top")) {
            $("#adv-search-span").addClass("glyphicon-triangle-bottom");
            $("#adv-search-span").removeClass("glyphicon-triangle-top");
             $("#adv-search-group").addClass("hidden");
        }
    });
    //Post ride button behavior
});