$(document).ready(function() {
    $(".nav-tab").on('click', function() {
        $(".content-page").addClass("hidden");
        var id = $(this).attr('id');
        $("."+id).removeClass("hidden");
    });
});