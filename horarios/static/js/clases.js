$(document).ready(function(){
	
	
	$('.escoger-fecha').click(function(){
		$('#tabla-clases h1').text($(this).attr('data-fecha'));
		
	});
	
	
});