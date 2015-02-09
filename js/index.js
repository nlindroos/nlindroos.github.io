//@TODO: Add exeption handling for missing content upon quote fetch with try .. catch(e)
//@TODO: https://developers.google.com/caja/ for the quote?

var loaded = 0;

window.addEventListener("load", function() {
	var bool = checkQuote();
	// Execute if the quote content has been loaded from the URL (a.k.a. no 404)
	if (!bool) {
		addQuote();
	}
	addDate();
});

function addDate() {

	var d = new Date();
	var day = d.getUTCDate();

	var monthShort = [];
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
	// Picking out the cherries and removing the rubbish from 'quote of the day' pull
	var quote = $("dt").html();
	var author = $(".tqpAuthor").html();
	var b = $("b")[0];
	var dl = $("dl")[0];
	var footer = $(".tqpFooter")[0];
	var body = $("body")[0];
	body.removeChild(b);
	body.removeChild(dl);
	body.removeChild(footer);


	$("#quote").html(quote);
	$("#author").html(author);
}

// @TODO: return false?
function checkQuote() {
	var text = "The quote could not be loaded. (404)";
	if (loaded===0) {
		$("#quote").html(text);
		return true;
	}
}


/*
// Fetching joke of the day with HTTP GET. N.B. "send" also necessary.
function httpGet(theUrl)
{
    var xmlHttp = null;

    xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send("null");
    return xmlHttp.responseText;
}*/

