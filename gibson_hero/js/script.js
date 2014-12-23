var canv = null;
var ctxt = null;
var WIDTH = 0;
var HEIGHT = 0;
var leftBound = 740;
var rightBound = 1050;
var gameScore = 0;
var audio = null;
var wrongKey = null;
var gameStopped = true;


window.addEventListener("load", function() {

	init();
	
	function init(){
		canv = document.querySelector("canvas");
		ctxt = canv.getContext("2d");
		WIDTH = ctxt.canvas.width;
		HEIGHT = ctxt.canvas.height;
		var img = document.createElement("img");
		img.onload = function(){
			ctxt.drawImage(img, 0, 0);
			ctxt.fillRect(leftBound,330,5,300);
			ctxt.fillRect(850,330,5,300);
		}
		img.src = "images/kitara.png";
		audio = document.getElementsByTagName("audio")[0];
		wrongKey = document.getElementsByTagName("audio")[1];
		createButton("start");
		createButton("stop");
	}
	
	function createButton(type){
		var txt = null;
		var button = document.createElement("button");
		if (type==="start"){
			txt = document.createTextNode("Start");
			button.id = "startButton";
		}
		else if (type==="stop"){
			txt = document.createTextNode("Stop");
			button.id = "stopButton";
		}
		button.appendChild(txt);
		document.body.appendChild(button);
	}
	
	// Mouse click listener
	window.onmousedown = function(e){
		$("#startButton").click(function(){
			startGame();
		});
		$("#stopButton").click(function(){
			stopGame();
		});
	}
	
	function stopGame(){
		if (!gameStopped){	
			$("#startButton").show();
			$("#overlay").show();
			$("#stopButton").hide();
			$("#help").show();
			audio.pause();
			audio.currentTime = 0;
			gameStopped = true;
			removeAllNotes();
		}
	}
	
	function startGame(){
		if (gameStopped) {
			$("#startButton").hide();
			$("#stopButton").show();
			$("#overlay").hide();
			$("#help").hide();
			resetScore();
			startSong();
			audio.play();
			gameStopped = false;
		}
	}
	
	// Keyboard listener
	window.onkeydown = function(e){
		var key = e.keyCode ? e.keyCode: e.which;
		if (!gameStopped){
			if (key===65){	// A
				checkNote("greenNote");
			}
			else if (key===83){	// S
				checkNote("redNote");
			}
			else if (key===68){	// D
				checkNote("yellowNote");	
			}
			else if (key===70){	// F
				checkNote("blueNote");
			}
			else if (key===71){	// G
				checkNote("orangeNote");
			}
		}
		if (key===13){	// Enter, starts  the game
			if(gameStopped){
				startGame();
			}
			else {
				stopGame();
			}
		}
		if (key===32){	// Enter, starts  the game
			if(gameStopped){
				startGame();
			}
			else {
				stopGame();
			}
		}		
		else if (key===80){	// S, stops the game
			stopGame();
		}
	}
	
	function checkNote(key){
		var notePressed = key;
		var $allPressedNotes = $("img[title*='"+ notePressed + "']"); //find all notes matching the key
		var $rightMost = $allPressedNotes.nearest({x:680, y: 325, w:1, h: 260}); // note nearest the area
		var left = $rightMost.css("left"); //get left -property from css
		var left = parseInt(left, 10); //parse integer 
		var leftBoundForPressing = leftBound - 50;
		var rightBoundForPressing = rightBound - 200;
		if(left < rightBoundForPressing && left > leftBoundForPressing){ //if note is between bounds
			// switch note colour
			$rightMost.attr({'src':'images/white.png'});
			//changing the title to make sure that it is not pressed again
			$rightMost.attr({'title':'pressed'}); 
			//add score based on variable "left" 
			addScore(Math.round(10000/(left - leftBoundForPressing)));
		}
		else {
			addScore(-50); // decrease score if tapping the keys at the wrong time
			wrongKey.play();
			$("#gameScore").effect("shake", 5);
		}			
	}
	
	function addScore(amount){
		gameScore += amount;
		$("#gameScore").html(gameScore);
	}
	
	function resetScore(){
		gameScore = 0; 
		$("#gameScore").html(gameScore);
	}
	
	audio.addEventListener('ended', function(){
		stopGame();
	});

});