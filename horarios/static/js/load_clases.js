function load_clases(){
		$.ajax({
			type:'POST',
			url: '/get/clases/',
			dataType: 'json',
			beforeSend: function() {
			    // $('#loading-gif').show();
			},
		    complete: function(){
			     //$('#loading-gif').hide();
			},
			data: { 'fecha':fecha },
			success: function(response) {
				response = response;
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				//TODO Place proper error message 
	       		//alert('sucedio un error al intentar actualizar la clase');
	   		}  
		});
}
