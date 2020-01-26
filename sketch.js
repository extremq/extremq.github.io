var numbers = [];
var toFind = -1;

function setup() {
  createCanvas(displayWidth, 400);
  background(255);
  
  input = createInput();
  input.position(20, 100);
  input.class('input-group-text');

  button = createButton('Submit');
  button.position(input.x + input.width + 30, input.y);
  button.class('btn btn-primary');
  button.mousePressed(() => {submit()});
  
  
  
  greeting = createElement('h1', 'Binary sort!');
  greeting.position(18, 5);
  
  intro = createElement('p', 'Please input at least 2 numbers (use as less digits as possible, thanks!).');
  intro.position(20,50);
  intro = createElement('p', 'I will sort the numbers for you.');
  intro.position(20, 70);
  
}


function submit(){
  var arr = split(input.value(), ' ');
  arr = arr.filter(function(str) {
    return /\S/.test(str) && (!isNaN(parseFloat(str)) && isFinite(str));
});
  var result = arr.map(function (x) { 
  return parseInt(x, 10); 
});
  
  function sortNumber(a,b){
    return a-b;
  }
  
  result.sort(sortNumber);
  
  if(result.length < 2) return;
  
  numbers = result;
  
  chooserInput = createInput();
  chooserInput.position(20, 170);
  chooserInput.class('input-group-text');
  
  chooser = createButton('Choose');
  chooser.position(chooserInput.x + chooserInput.width + 30, 170);
  chooser.class('btn btn-secondary');
  chooser.mousePressed(() => {choose(chooserInput.value())});
  
  intro = createElement('p', 'Please input what number you want to find.');
  intro.position(20,140);
  
  print(numbers);
  createNumbers(numbers);
}

function createNumbers(arr){
  background(255);
  var x,y;
  var offset = displayWidth/arr.length;
  for(var i = 0; i<arr.length; ++i){
    var value = arr[i];
    x = i*offset + offset/2;
    y = 300;

    var length = getLength(value);
    
    fill(255);
    rect(x - 10 * length, y - 30, 20 * length, 40);
        
    textAlign(CENTER);
    textFont('Monospace');
    textSize(32);
    fill(0)
    text(value, x, y);
  }

}

var advBtnCreated = false;

function choose(val){
  toFind = val;
  var offset = displayWidth/numbers.length;
  for(var i = 0; i<numbers.length; ++i){
    if(numbers[i] == val){
      x = i*offset + offset/2;
      y = 300;

      var length = getLength(val);

      fill(0,0,0,0);
      strokeWeight(2);
      stroke(255,0,0);
      rect(x - 10 * length, y - 30, 20 * length, 40);
    }
  }
  if(advBtnCreated == false){
    advBtnCreated = true;
    btn = createButton('Advance');
    btn.position(displayWidth/2 - 87/2, 330);
    btn.class('btn btn-primary');
    btn.mousePressed(advanceStep);
  }
  
}

function advanceStep(){
  
}

function getLength(value){
 return Math.log(value) * Math.LOG10E + 1 | 0;
}

function draw() {
}