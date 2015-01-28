
// Holds the y-value of all h1 tags in order of appearance
var positions = [];
var video;

// Event listeners
window.addEventListener("load", function() {
	getPositions(positions);
	updateActive();
	setNavAffixNames();
	video = document.getElementsByTagName("video")[0];
	setVideoVolume();
});

window.addEventListener("scroll", function() {
	updateActive();
});

window.addEventListener("resize", function() {
	getPositions(positions);
	updateActive();
});

window.addEventListener("click", function() {
	updateActive();
});

// Returns an array with the the y-values of all h1 tags
function getPositions(array) {
	var i = 0;
	$("h1").each( function() {
		array[i] = $(this).offset().top;
		i++;
	});
	return array;
}

// Sets class to "current" for the correct tag in #nav_affix
function updateActive() {
	// Resets all classnames
	for (var i=1; i<=positions.length; i++) {
		$("#li"+i).removeClass("current");
	}
	// Updates the active element
	for (var j=1; j<=(positions.length); j++) {
		if ((window.scrollY+110)>=positions[j-1] && (window.scrollY+100)<positions[j]) {
			$("#li"+j).addClass("current");
			if (j!=1) {
				$("#li"+(j-1)).removeClass("current");
			}
			if (j!=positions.length) {
				$("#li"+(j+1)).removeClass("current");
			}
		}
		if ((window.scrollY+300)>=positions[positions.length-1]) {
			$("#li"+positions.length).addClass("current");
			$("#li"+(positions.length-1)).removeClass("current");
		}
	}
}

// Sets the names of links in #nav_affix
function setNavAffixNames() {
	var names = $("div.project h1 a");
	var i = 0;
	$("#nav_affix li a").each( function() {
		$(this).html(names[i].innerHTML);
		i++;
	});
}

function setVideoVolume() {
	video.volume = 0.6;
}

function videoControl(e) {
	e.preventDefault();
	if (video.paused) {
		video.play();
	}
	else {
		video.pause();
	}
}