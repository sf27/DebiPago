/////////mensaje de error personalizado con jquery
jQuery.fn.asError = function() {
	return this.each(function() {
		$(this).replaceWith(function(i, html) {
			var newHtml = "<div class='ui-state-error ui-corner-all' style='padding: 0 .3em;'>";
			newHtml += "<span class='ui-icon ui-icon-alert' style='float: left; margin-right: .1em;'>";
			newHtml += "</span><p>";
			newHtml += html;
			newHtml += "</p></div>";
			return newHtml;
		});
	});
};

jQuery.fn.asSuccess = function() {
	return this.each(function() {
		$(this).replaceWith(function(i, html) {
			var newHtml = "<div class='ui-state-highlight ui-corner-all' style='padding: 0 .3em;'>";
			newHtml += "<span class='ui-icon ui-icon-info' style='float: left; margin-right: .1em;'>";
			newHtml += "</span><p>";
			newHtml += html;
			newHtml += "</p></div>";
			return newHtml;
		});
	});
};

function msg(id_comp, msn, f, type) {
	if (!$(id_comp).empty()) {
		$(id_comp).empty();
	}
    $(id_comp).dialog("open");
	return $('<p>').text(msn).appendTo(id_comp);
}
