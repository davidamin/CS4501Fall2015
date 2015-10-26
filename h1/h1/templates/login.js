$(document).ready(function() {
    $("#create-account-btn").on('click', function() {
        $("#login-form").addClass("hidden");
        $("#create-form").removeClass("hidden");
    }); 
    
    $("#back-to-login-btn").on('click', function() {
        $("#create-form").addClass("hidden");
        $("#login-form").removeClass("hidden");
    });
});