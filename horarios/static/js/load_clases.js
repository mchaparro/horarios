$(document).ready(function(){
	load_clases(fecha);
	$('.week-day-picker td').click(function(){
		
		$('.week-day-picker td').removeClass('activo');
		
											
	});
	
	$("tr:odd").addClass("odd");
	
	$('.escoger-fecha').click(function(){
		fecha = $(this).attr('data-fecha');
		$(this).toggleClass('activo');
		$('*[data-id="saloncito"]').remove();
		load_clases(fecha);
	});
});

function load_clases(fecha){
		$.ajax({
			type:'POST',
			url: '/get/clases/',
			dataType: 'json',
			beforeSend: function() {
			    $('#loading').show();
			},
		    complete: function(){
			    $('#loading').hide();
			},
			data: { 'fecha':fecha },
			success: function(response) {
				$('*[data-id="saloncito"]').remove();
				$.each(response, function(){
				var td = $('.grupo-'+this.grupo+'-hora-'+this.hora);
				td.append("<div data-id='saloncito' class='" +this.salon+ "'>"+this.salon+" "+this.cantidad_alumnos+" </div>").remove;
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
