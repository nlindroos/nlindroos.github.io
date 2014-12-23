window.addEventListener("load", function() {

	var headers = document.getElementsByTagName("h1");
	var positions = new Array();
	function getPositions() {
		for (var i=0; i<document.getElementsByTagName("h1").length; i++){
			console.log(headers[i]);
			positions[i] = $("h1").offset().top;
		}
	}
	getPositions();
	var i = 0;
	$("h1").each( function() {
		positions[i] = $(this).offset().top;
		i++;
	});

	for (var j=0; j<positions.length; j++){
		console.log(positions[j]);
	}

	$(window).scroll( function() {
		for (var j=1; j<=(positions.length); j++) {
			if ((window.scrollY+300)>=positions[j-1] && (window.scrollY+300)<positions[j]) {
				document.getElementById(""+j).className = "active";
				if (j!=1) {
					document.getElementById(""+(j-1)).className = "";
				}
				if (j!=positions.length) {
					document.getElementById(""+(j+1)).className = "";
				}
			}
			if ((window.scrollY+300)>=positions[positions.length-1]) {
				document.getElementById(""+positions.length).className = "active";
				document.getElementById(""+(positions.length-1)).className = "";
			}
		}
		
		//console.log(window.scrollY);
	});


	


});

function getPositions() {
	for (var i=0; i<document.getElementsByTagName("h1").length; i++){
		console.log(headers[i]);
		positions[i] = $("h1").offset().top;
	}
}

$("window").on("resize", getPositions());




