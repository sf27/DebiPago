$(function() {
			//limpia mensaje de error
			$("#cantidad").keypress(function() {
  				if (!$('#error').empty()){
 					$('#error').empty();
 				}
			});
            //valida input de solo numeros
		    $("#cantidad").bind("keyup paste", function(){
				setTimeout(jQuery.proxy(function() {
					this.val(this.val().replace(/[^0-9]/g, ''));
    			}, $(this)), 0);
			});

			//configuracion del dialog que se muestra al dar click en comprar
            $('#dialog').dialog({
  				autoOpen: false,
                height: 350,
                width: 320,
                modal: true,
                show: "fold",
                hide: "scale"
                    /**buttons: {
                        "Comprar": function() {
                    		//comprar_ajax();  
                    		$(this).dialog("close");                         
                        },
                        "Cancelar": function() {
                            $(this).dialog("close");
                        }
                    }*/
            });
                //accion del formulario
            
                // Dialog Link
            $('#comprar').button().click(function(){
                $('#dialog').dialog("open");
                return false;
            });
                //boton de cancelar en el dialog mostrado al dar click en comprar
            $('#cancelar').click(function(){
                $('#dialog').dialog("close");
                return false;
            });
                //muestra mensaje al realizar la compra exitosamente
            $( "#done-message" ).dialog({
                autoOpen: false,
            	modal: true,
            	buttons: {
                	Ok: function() {
                		$( this ).dialog( "close" );
                		location.reload();
                	}
           		}
            });
            $( "#error-message" ).dialog({
                    autoOpen: false,
                    modal: true,
                    buttons: {
                        Ok: function() {
                            $( this ).dialog( "close" );
                        }
                    }
            });
            //limite
            $("#comment").keyup(function(){
                	var characters = 300;
    				if($(this).val().length > characters){
        				$(this).val($(this).val().substr(0, characters));
					}
            });

});