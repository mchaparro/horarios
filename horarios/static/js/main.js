$(document).ready(function() {
	
	//class to use colorbox plugin
	$('a.colorbox-link').colorbox({
		trapFocus:false,
		onComplete:function(){
			$("#crud-table-title").text($("#cboxTitle").text());
			
			$('.close-colorbox').click(function(){
				$.colorbox.close();
			});
			
		},
		onCleanup:function(){
			
		}
	});
	
	//include csrftoken for ajax requests
	function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie != '') {
	        var cookies = document.cookie.split(';');
	        for (var i = 0; i < cookies.length; i++) {
	            var cookie = jQuery.trim(cookies[i]);
	            // Does this cookie string begin with the name we want?
	            if (cookie.substring(0, name.length + 1) == (name + '=')) {
	                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
	                break;
	            }
	        }
	    }
	    return cookieValue;
	}

	$.ajaxSetup({
	    headers: { "X-CSRFToken": getCookie("csrftoken") }


	});

});


