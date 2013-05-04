/**
 * Created with PyCharm.
 * User: elio
 * Date: 5/3/13
 * Time: 2:07 PM
 * To change this template use File | Settings | File Templates.
 */

var busqueda = function(){
    $("#id_query").focus(function () {
        // Petición AJAX
        $.get("/categorias_ajax/", function (data) {
            //$("#mensaje").html(data);
            $("#id_query").autocomplete({
                source: data
            });
        });
    });
}


$(function(){
    busqueda
});

