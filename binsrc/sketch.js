var numbers = [];
var toFind = -1;

function setup() {
  if(displayWidth < 700)
    createCanvas(700,500);
  else
    createCanvas(displayWidth, 500);
  background(255);

  input = createInput();
  input.position(20, 100);
  input.class('input-group-text');

  button = createButton('Submit');
  button.position(input.x + input.width + 30, input.y);
  button.class('btn btn-dark');
  button.mousePressed(() => {
    submit()
  });



  greeting = createElement('h1', 'Binary search');
  greeting.position(18, 5);

  intro = createElement('p', 'Please input at least 2 numbers (use as less digits as possible, thanks!).');
  intro.position(20, 50);
  intro = createElement('p', 'I will sort the numbers for you.');
  intro.position(20, 70);

}

var chooserCreated = false;
function submit() {
  left = 0;
  right = -1;
  var arr = split(input.value(), ' ');
  arr = arr.filter(function(str) {
    return /\S/.test(str) && (!isNaN(parseFloat(str)) && isFinite(str));
  });
  var result = arr.map(function(x) {
    return parseInt(x, 10);
  });

  function sortNumber(a, b) {
    return a - b;
  }

  result.sort(sortNumber);

  if (result.length < 2) return;

  numbers = result;
  if(chooserCreated == false){
    chooserCreated = true;
    chooserInput = createInput();
    chooserInput.position(20, 170);
    chooserInput.class('input-group-text');

    chooser = createButton('Choose');
    chooser.position(chooserInput.x + chooserInput.width + 30, 170);
    chooser.class('btn btn-dark');
    chooser.mousePressed(() => {
      choose(chooserInput.value())
    });

    intro = createElement('p', 'Please input what number you want to find.');
    intro.position(20, 140);
  }
  print(numbers);
  createNumbers(numbers);
}




var left = 0, right = -1;
function createNumbers(arr) {
  if(right == -1) right = arr.length - 1;
  background(255);
  var x, y;
  var offset = displayWidth / arr.length;
  for (var i = 0; i < arr.length; ++i) {
    var value = arr[i];
    x = i * offset + offset / 2;
    y = 300;

    var length = getLength(value);
    strokeWeight(0);
    textAlign(CENTER);
    textFont('Monospace');
    textSize(32);
    fill(0)
    text(value, x, y);
    fill(0,0,255);
    if(i == left)
      text('[', x, y - 40);
    else if(i == right)
      text(']', x, y - 40);
    
    if (numbers[i] == toFind) {
      fill(0, 0, 0, 0);
      strokeWeight(2);
      stroke(255, 0, 0);
      rect(x - 10 * length, y - 30, 20 * length, 40);
      stroke(0);
    }
  }
  hasFound = false;
}

var advBtnCreated = false;
var hasFound = false;

function choose(val) {
  toFind = val;
  if (advBtnCreated == false) {
    advBtnCreated = true;
    btn = createButton('Advance');
    btn.position(displayWidth / 2 - 87 / 2, 330);
    btn.class('btn btn-dark');
    btn.mousePressed(advanceStep);
  }
  if(hasFound == false)
	advanceStep();
  else {
	submit();
	hasFound = false;
	advanceStep();
  }
}

function advanceStep() {
  drawStuff(numbers)
}


function drawStuff(arr){

  if(hasFound == true) return;
  background(255);
  var x, y;
  var offset = displayWidth / arr.length;
  var mid = Math.floor((left + right) / 2);
  print(mid);
  for (var i = 0; i < arr.length; ++i) {
    var value = arr[i];
    x = i * offset + offset / 2;
    y = 300;

    /*if(left <= i && i <= right){ 
      strokeWeight(1);
      fill(255);
      rect(x - 10 * length, y - 30, 20 * length, 40);
    }*/
    var length = getLength(value);
    strokeWeight(0);
    textAlign(CENTER);
    textFont('Monospace');
    textSize(32);
	if(left <= i && i <= right) fill(0)
	else fill(200);
    text(value, x, y);
    fill(0,0,255);
    if(i == left)
      text('[', x, y - 40);
    else if(i == right)
      text(']', x, y - 40);
    
    if(i == mid){
      text('???', x, y - 70);
	  strokeWeight(2);
      fill(0,0,0,0);
	  stroke(0, 0, 255);
      rect(x - 10 * length, y - 30, 20 * length, 40);
	  stroke(0);
    }
    
    if (numbers[i] == toFind) {
      fill(0, 0, 0, 0);
      strokeWeight(2);
      stroke(255, 0, 0);
      if(i == mid)
        stroke(0,255,0);
      rect(x - 10 * length, y - 30, 20 * length, 40);
      stroke(0);
    }
  
  }
  if(numbers[mid] > toFind)
    right = mid;
  if(numbers[mid] < toFind)
    left = mid + 1;
  if(numbers[mid] == toFind)
  {
    strokeWeight(0);
    fill(0,255,0);
    textSize(16);
    textAlign(LEFT);
    text("The number was found at " + mid.toString() + "!",340, 115)
    text("You can submit again!", 340 , 135);
    hasFound = true;
  }
  if(left >= right && hasFound == false){
    strokeWeight(0);
    fill(255, 0,0);
    textSize(16);
    textAlign(LEFT);
    text("The number does not exist!",340, 115)
    text("You can submit again!", 340 , 135);
    hasFound = true;
  }
    
  strokeWeight(0);
  textSize(16);
  fill(100);
  textAlign(LEFT);
  text("left = " + left.toString() + ", right = " + right.toString(), 340, 185);
  text("mid = (left + right) / 2 = " + mid.toString(), 340, 205);
    
}

function getLength(value) {
  return Math.log(value) * Math.LOG10E + 1 | 0;
}

function draw() {}
