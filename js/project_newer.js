window.addEventListener("load", function() {

	var positions = [];

	function getPositions() {
		var i = 0;
		$("h1").each( function() {
			positions[i] = $(this).offset().top;
			i++;
		});
	}

	var counter = 0;
	function updateActive() {
		console.log("New event");
		for (var j=0; j<positions.length; j++){
			console.log(positions[j]);
			console.log("success"+counter);
		}
		counter++;
	}

	for (var j=0; j<positions.length; j++){
		console.log(positions[j]);
		console.log("success again");
	}

	// Marks the correct navbar list item as "active" depending on the scroll position
	$(window).scroll( function() {
		for (var j=1; j<=(positions.length); j++) {
			if ((window.scrollY+100)>=positions[j-1] && (window.scrollY+300)<positions[j]) {
				document.getElementById("li"+j).className = "active";
				if (j!=1) {
					document.getElementById("li"+(j-1)).className = "";
				}
				if (j!=positions.length) {
					document.getElementById("li"+(j+1)).className = "";
				}
			}
			if ((window.scrollY+300)>=positions[positions.length-1]) {
				document.getElementById("li"+positions.length).className = "active";
				document.getElementById("li"+(positions.length-1)).className = "";
			}
		}
		
		//console.log(window.scrollY);
	});

	$("window").resize(getPositions());

	$("window").scroll(updateActive());

	positions=getPosition(positions);
	console.log("getPosition worked");
	for (var k=0; k<positions.length; k++) {
		console.log(positions[k]);
	}

});

var positions = [];
window.addEventListener("scroll", function() {
	for (var j=1; j<=(positions.length); j++) {
		if ((window.scrollY+100)>=positions[j-1] && (window.scrollY+300)<positions[j]) {
			document.getElementById("li"+j).className = "active";
			if (j!=1) {
				document.getElementById("li"+(j-1)).className = "";
			}
			if (j!=positions.length) {
				document.getElementById("li"+(j+1)).className = "";
			}
		}
		if ((window.scrollY+300)>=positions[positions.length-1]) {
			document.getElementById("li"+positions.length).className = "active";
			document.getElementById("li"+(positions.length-1)).className = "";
		}
	}

});



// Returns the y-value of all h1 tags in an array
function getPosition(array) {
	var i = 0;
	$("h1").each( function() {
		array[i] = $(this).offset().top;
		i++;
	});
	return array;
}






