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