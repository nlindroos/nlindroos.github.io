//@TODO: Add exeption handling for missing content upon quote fetch with try .. catch(e)
//@TODO: https://developers.google.com/caja/ for the quote?

var loaded = 0;

/*	Updating the position of the div.inset-shadow */
function alignInsetShadow() {
	var imgLeftValue = $(".img-circle").position().left;
	$(".inset-shadow").css({left: imgLeftValue});
}

function addDate() {
	/*	Comma separated variable declarations decreases
		the number of look-ups required */
	var d = new Date(),
	day = d.getUTCDate(),

	monthShort = [];
	monthShort[0] = "Jan";
	monthShort[1] = "Feb";
	monthShort[2] = "Mar";
	monthShort[3] = "Apr";
	monthShort[4] = "May";
	monthShort[5] = "Jun";
	monthShort[6] = "Jul";
	monthShort[7] = "Aug";
	monthShort[8] = "Sep";
	monthShort[9] = "Oct";
	monthShort[10] = "Nov";
	monthShort[11] = "Dec";

	$("#dayOfMonth").html(day);
	$("#month").html(monthShort[d.getUTCMonth()]);
}

function addQuote() {
	/*	Picking out the cherries and removing the 
		rubbish from 'quote of the day' pull*/
	var quote = $("dt").html(),
	author = $(".tqpAuthor").html(),
	b = $("b")[0],
	dl = $("dl")[0],
	footer = $(".tqpFooter")[0],
	body = $("body")[0];
	body.removeChild(b);
	body.removeChild(dl);
	body.removeChild(footer);


	$("#quote").html(quote);
	$("#author").html(author);
}

function addError() {
	text = "The quote could not be loaded. (404)";
	$("#quote").html(text);
}


$(window).on("load", function() {
	/*	Execute if the quote content has been loaded 
		from the URL (a.k.a. no 404) */
	var bool = loaded ? addQuote() : addError();
	addDate();

	//addQuotee();


	var parent = $(".img-circle").parent();
	$(".img-circle").parent().append('<div class="inset-shadow"></div>');

	alignInsetShadow();
});

$(window).on("resize", function() {
	alignInsetShadow();
});

/*
function addQuotee() {
	$.ajax({
		type: "GET",
		url: "http://www.quotationspage.com/data/1qotd.js",
		dataType: "script"
	})
	.done( function(response) {
	})
	.fail( function() {
		alert("Failed");
	});
}
*/
