$(document).ready(function(){
//    load_clases(fecha);
//    $('.week-day-picker td').click(function(){
//        $('.week-day-picker td').removeClass('activo');
//        $(this).toggleClass('activo');
//                                            
//    });
//    
    salon = "PARIS";
    $('#saloncitos div').click(function(){
        salon=$(this).attr('data-salon');
        $('#saloncitos div').removeClass('salon-activo');
        $(this).toggleClass('salon-activo');
    });
//    $("tr:odd").addClass("odd");
//    
//    $('.escoger-fecha').click(function(){
//        $('#tabla-clases h1').text($(this).attr('data-fecha'));
//        fecha = $(this).attr('data-fecha');
//        load_clases(fecha);
//    });
    
    
    $("td.clase").click(function(){
        
        
            if ($(this).find('.'+salon).length > 0){
                $(this).find('.'+salon).remove();
            }
            else if ($(this).parents('tr').find('td > div.'+salon).length == 0){
                $(this).append('<div class='+salon+'>'+salon+'</div>');
            }
            else {
                console.log('Ya esta en uso el salon '+salon+' a esa hora!');
                
            }
            var grupo = $(this).attr('data-grupo');
            var hora = $(this).attr('data-hora');
            var arreglo_clases =  new Array();
            
            $(this).children('div').each(function(){
                arreglo_clases.push($(this).attr('class'));
            });
                    $.ajax({
                        type:'POST',
                        url: '/update/clase/',
                        dataType: 'json',
                        beforeSend: function() {
                            // $('#loading-gif').show();
                        },
                        complete: function(){
                             //$('#loading-gif').hide();
                        },
                        data: { 'clases': JSON.stringify(arreglo_clases),'fecha':fecha,'grupo':grupo,'hora':hora },
                        success: function(response) {
                            console.log(response);
                        },
                        error: function(XMLHttpRequest, textStatus, errorThrown) {
                            //TODO Place proper error message 
                               //alert('sucedio un error al intentar actualizar la clase');
                           }  
                    });
        
            
    });
});