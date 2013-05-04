enviar_comentario = function(url_p, articulo_id, token, src_img) {
	//enviar comentario
	var ubi = $("section#comentarios > .ui-widget");
	var comment_button = $("#send_comment", ubi);
	comment_button.button().click(function() {
		var c = $("#comment", ubi).val();
		c = $.trim( c );
		console.log("comentario: " + c + c.length)
		if (c === "" || c === null || c === undefined){
			if (!$('#error-message').empty()) {
				$('#error-message').empty();
			}
			$('<p>').text('Debe ingresar un contenido.').appendTo('#error-message').asError();
			$('#error-message').dialog("open");

		} else {
			var request = $.ajax({
				type : "POST",
				//url: "{% url comentar_ajax %}",
				url : url_p,
				data : {
					'comentario' : c,
					//'id_articulo':{{articulo.id}},
					'id_articulo' : articulo_id,
					//csrfmiddlewaretoken: '{{ csrf_token }}'
					csrfmiddlewaretoken : token
				},
				beforeSend : function() {
					var img_load = $('<img></img>', {
						id: 'loader',
						src : src_img+"/spinner.gif"
					});
					$('#enviandoAjax').append(img_load)
				}
			});
			request.done(function(msn) {
                return msg('#done-message', 'Comentario registrado.').asSuccess();
			});

			request.fail(function(jqXHR, textStatus) {
                return msg('#error-message', 'Ocurrio un error en la petición. <br/> Comuniquese con el administrador.').asError();
			});
		}//else
	});

}



comprar = function(url_p, src_img) {
	$('#form_compra').submit(function(event) {
        event.preventDefault();
		var that = $(this);
		//bloquea accion normal de boton submit
		var cantidad_art = parseInt($("#dialog input#cantidad").val());
		var cantidad_max = parseInt($("#dialog input#cantidad_hidden").val());
		if (cantidad_art <= cantidad_max) {
			comprar_ajax(url_p, src_img);
			that.dialog("close");
		} else {
            return msg('#error', 'Ingrese un valor dentro del rango').asError();
		}
	});
}

comprar_ajax = function(url_p, src_img) {
	var ubi = $("#dialog > #datos_compra");
	var cantidad_art = $("input#cantidad", ubi).val();
	var precio_art = $("#hidden input#precio_hidden", ubi).val();
	var id_articulo = $("#hidden input#id_hidden", ubi).val();
	var request = $.ajax({
		type : "GET",
		//url : "{% url compra_ajax %}?",
		url : url_p,
		data : "cantidad=" + cantidad_art + "&precio=" + precio_art + "&id=" + id_articulo,
		beforeSend : function() {
			var img_load = $('<img></img>', {
				id : 'loader',
				src : src_img + "/spinner.gif"
			});
			$('#enviandoAjax').append(img_load)
		}
	});
	request.done(function(msn) {
        return msg('#done-message', 'Compra registrada.').asSuccess();
	});

	request.fail(function(jqXHR, textStatus) {
        return msg("#error-message", '').asError();
	});
}


