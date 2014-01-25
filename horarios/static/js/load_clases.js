function load_clases(fecha){
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
				$.each(response, function(){
				var td = $('.grupo-'+this.grupo+'-hora-'+this.hora);
				td.append("<div data-id='saloncito' class='" +this.salon+ "'>"+this.salon+" </div>").remove;
				console.log(td);
				});				
				console.log(response);
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				//TODO Place proper error message 
	       		//alert('sucedio un error al intentar actualizar la clase');
	   		}  
		
		});
}
