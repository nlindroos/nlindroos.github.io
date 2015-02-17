window.addEventListener("load", function() {
	
	/*	Adds the current date to the lower left corner
		N.B. Has to be done once window has loaded so as 
		not to overwrite the HTML content*/
	var d = new Date();
	var dayArray = [];
	dayArray[0] = "Sunday";
	dayArray[1] = "Monday";
	dayArray[2] = "Tuesday";
	dayArray[3] = "Wednesday";
	dayArray[4] = "Thursday";
	dayArray[5] = "Friday";
	dayArray[6] = "Saturday";
	var vDay = dayArray[d.getUTCDay()];
	var day = d.getUTCDate();
	var month = [];
	month[0] = "January";
	month[1] = "February";
	month[2] = "March";
	month[3] = "April";
	month[4] = "May";
	month[5] = "June";
	month[6] = "July";
	month[7] = "August";
	month[8] = "September";
	month[9] = "October";
	month[10] = "November";
	month[11] = "December";
	var vMonth = month[d.getUTCMonth()];
	var year = d.getFullYear();
	var date = vDay+", "+day+" "+vMonth+ " "+ year;
	document.getElementById("date").innerHTML = date;


});

/*	Tried reducing duplicate code by loading it with ajax. 
	Seems to increases loading time, so abandoning that idea.

function addNavbar() {
	$.ajax({
		type: "GET",
		url: "navbar.html",
		dataType: "html"
	})
	.done(function(navbarContent) {
		try {
			$(".navbar-inverse").append(navbarContent);
		}
		catch (err) {
			console.log("Could not append the navbar, error: " + err);
		}
	})
	.fail(function() {
		console.log("Did not find the navbar.html file.");
	});
}*/

//var result = httpGet("http://api.icndb.com/jokes/random");

//console.log(result);
/*
document.writeln('<b><font size=\'+1\'><a target=\'_blank\' class=\'tqpHeader\' href=\"http://www.quotationspage.com/qotd.html\">Quote of the Day (September 11, 2014)</a></font></b><br>');
document.writeln('<dl>');
document.writeln('<dt class=\'tqpQuote\'>I have discovered that all human evil comes from this, man\'s being unable to sit still in a room.</dt>');
document.writeln('<dd> <b><font size=\'-1\'><a class=\'tqpAuthor\' target=\'_blank\' href=\"http://www.quotationspage.com/quotes/Blaise_Pascal\">Blaise Pascal</a></font></b></dd><p> </p>');
document.writeln('</dl>');
document.writeln('<span class=\'tqpFooter\'>Visit <a target=\'_blank\' href=\"http://www.quotationspage.com/\"><b>The Quotations Page</b></a> for more quotes.</span>');
*/
// TODO: pick author from the javascript. Then remove all the unnecessary shit with parentNode.removeChild()




