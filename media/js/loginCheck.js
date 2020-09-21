$(function(){
 $('.form-text').on('submit',function(e){
  e.preventDefault();
  // console.log($('input[name="csrfmiddlewaretoken"]').val() );
  $.ajax({
   url:'/website/ajax_check/',
   type:"POST",
   data:
   {
   	username:$('input[name="username"]').val(),	
   	password:$('input[name="password"').val(),
   	csrfmiddlewaretoken:$('input[name="csrfmiddlewaretoken"]').val() 
    },
   success:function(response){
   	console.log(response);
   	if(response['authenticate']==true)
   	 window.location.replace(response['url'])
   	else{
   	  $('.Ajax').html('<div class="alert alert-danger">'+response['errors']+'</div>');	
   	}
   	  	
   	 console.log("success");
   	},
   error:function(xhr,status){
    console.log('ajax error ='+xhr.statusText);
   },
  });
 });
});



