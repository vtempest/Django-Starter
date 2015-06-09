$(document).ready(function() {

  $("#login-loginbutton").click(function() {
    $.get("/login", {username: $("#login-username").val(), password: $("#login-password").val() }, 
      function(r){
        if (r=="Success")
        location.reload();
      else
        $("#login-password").addClass('btn-danger');
      setTimeout(function(){
         $("#login-password").removeClass('btn-danger');
      }, 2000);
    });
  });

  $("#login-registerbutton").click(function() {

      if ( $("#login-username").val().length < 3){
       $("#login-username").addClass('btn-danger');
          setTimeout(function(){
             $("#login-username").removeClass('btn-danger');
          }, 2000);
          return;
      }

      if ( $("#login-password").val().length < 3){
       $("#login-password").addClass('btn-danger');
          setTimeout(function(){
             $("#login-password").removeClass('btn-danger');
          }, 2000);
          return;
      }      

      $.get("/register", {username: $("#login-username").val(), password: $("#login-password").val() }, 
        function(r){

            if (r=="Registered"){
            location.reload();
          } else if (r=="Taken"){
            $(".login-form").popover({ content : "Username is taken", location: "left"});
            $(".login-form").popover('show');
          } 
      });
  });

  $("#login-logoutbutton").click(function(event) {
      
      $.get("/logout" , function(r){
         location.reload();
      });
  });

});