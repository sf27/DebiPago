
var Articulo = {
      config: {
        a_id: 0,
        files_config: "{{MEDIA_URL}}",
        csrf_tok: "{{ csrf_token }}"
      },
      init:function(config){
          $.extend(this.config, config);
          //configura el campo de texto del comentario
          $('#comment').val("");
		      $('#comment').autosize();
      },//init
      comentar: function(url_comentar){
			enviar_comentario(url_comentar,  this.config.a_id,  this.config.csrf_tok,  this.config.files_config);

      },//comentar
      comprar: function(url_compra){
			comprar(url_compra, this.config.files_config);

      },//comprar
      infinite_scroll: function(url_infinite_scroll){
          var load_button = $("#principal #articulos #lista_articulos #comentarios #load_comments"),
              id =  this.config.a_id,
              token = this.config.csrf_tok;
          var counter = {
              number: 2
          };
          load_button.button().click(function () {
              $.post(url_infinite_scroll, {'id_articulo':  id,
                                           'number_page': counter.number,
                                            csrfmiddlewaretoken: token},
                  //function que retorna los datos
                  function (data) {
                      if (data == false) {
                          load_button.hide();
                      } else {
                          counter.number = parseInt(data.pop()[0]);
                          for (i = 0; i < data.length; i++) {
                              var context = $('<article></article>', {
                                  class: 'caja_comentario'

                              });
                              var texto = $('<p></p>', {
                                  text: data[i][0]
                              });
                              var fecha = $('<p></p>', {
                                  class: 'fecha',
                                  text: data[i][1]
                              });
                              context.append(fecha, texto);
                              context.appendTo('#new_comments');

                          }
                      }
                  }, "json");

          });
      }//infinite_scroll
}//Articulo
