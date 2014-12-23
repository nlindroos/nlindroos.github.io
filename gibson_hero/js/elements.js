var hideTime = 100; //hide animation time
var endXPosition = 950	; //animation end X position 
var greenPositionY = 325;
var redPositionY = 390;
var yellowPositionY = 455;
var bluePositionY = 520;
var orangePositionY = 580;
var noteNumber = 0; // note index from 0 to n
var noteList = new Array();


function moveit(noteID, newPositionX, newPositionY) {
    var newTop = newPositionY;
    var newLeft = newPositionX;
	var note = noteID;
    var newDuration = 4000;
	
    $(noteID).animate({
      top: newTop,
      left: newLeft,
      }, newDuration, function() {
		moveit();
      });
}

/*Switch-statement for noteColour: 
	1: greenNote
	2: redNote
	3: yellowNote
	4: blueNote
	5: orangeNote
NoteTime: milliseconds from song start
*/
function spawnNote(noteColour, noteTime){
	var note = noteColour;
	var time = noteTime;
	var positionY;
	noteNumber++;
	
	//select y position and create unique ID
	switch(note)
	{
		case 1:
			note = "greenNote" + noteNumber;
			positionY = greenPositionY;
			break;
		case 2:
			note = "redNote" + noteNumber;
			positionY = redPositionY;
			break;
		case 3:
			note = "yellowNote" + noteNumber;
			positionY = yellowPositionY;
			break;
		case 4:
			note = "blueNote" + noteNumber;
			positionY = bluePositionY;			
			break;
		case 5:
			note = "orangeNote" + noteNumber;
			positionY = orangePositionY;
			break;
	}
	/* append string to inject html
		scr: green at first, changed in scripts.js if hit correctly
		title: is for gameScore and matching in scripts.js, changed to "pressed" if  it is pressed 
		id: to match in spawnNote
		note: note colour + unique ID 
	*/
	var appendString = '<img src="images/green.png" title="' + note + '" id="' + note + '"/>';
	//we need to have # before this to use the id inside jquery
	note = '#'+note;
	//append image to the site body
	$("body").append(appendString);
	//modify the image's css
	$(note).css({"z-index":"700", "position":"absolute", "display":"none", "left":"0px", "top":positionY+"px"});
	//show the note in planned time
	$(note).show(time);
	// animate and move it to right position
	moveit(note, endXPosition, positionY);
	//hide the note
	$(note).hide(hideTime,"linear");
	noteList[noteNumber] = note;
	//delete old notes
/*	setTimeout(function() {
		$(note).remove();
	}, 8000);
*/
	//done!
}

function removeAllNotes(){
		$("img[title*='"+ "greenNote" + "']").remove(); //find all notes matching the key
		$("img[title*='"+ "redNote" + "']").remove(); //find all notes matching the key
		$("img[title*='"+ "blueNote" + "']").remove(); //find all notes matching the key
		$("img[title*='"+ "orangeNote" + "']").remove(); //find all notes matching the key
		$("img[title*='"+ "yellowNote" + "']").remove(); //find all notes matching the key
}

// Returns a random number between 1 and 5
function getRandom() {
		return (Math.floor(Math.random() * 5) + 1);
}

function startSong() {
	noteList = [];
	audio = document.getElementsByTagName("audio")[0];
	var k = 0;
	var triggeredNote = 'spawnNote(getRandom(), 0)';
	var audioDuration = audio.duration * 1000;
	setInterval( function() {
		if(k<audioDuration){
			if(!gameStopped){
				spawnNote(getRandom(), k);
				k+=500;
			}
		}
	}, 250);
	var i = 0
	setTimeout( function() {
		setInterval ( function() {
			if(!gameStopped)
				$(noteList[i]).remove();
				i=i+1;
		}, 1000); 
	}, 5000);
}	
	
$(document).ready(function() {
	$('#overlay').show();
});
