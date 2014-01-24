$(document).ready(function(){
	$('.week-day-picker td').click(function(){
		$('.week-day-picker td').removeClass('activo');
		$(this).toggleClass('activo');
											
	})
	
	salon = "BIGROOM";
	$("tr:odd").addClass("odd");
	
	$('.escoger-fecha').click(function(){
		fecha = $(this).attr('data-fecha');
	});
	
		
});