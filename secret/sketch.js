function setup() {
  createCanvas(0,0);
  createDiv('<br>')
  let inp = createInput('');
  inp.style('border', 'none');
  inp.style('border-bottom', '2px solid black');
  inp.style('width', '75%');
  inp.style('height', '20px');
  inp.style('display', 'block');
  inp.style('margin-right', 'auto');
  inp.style('margin-left', 'auto');
  inp.style('text-align', 'center');
  inp.style('font-family', 'Courier New');
  inp.style('font-size', '18px');
  inp.input(myInputEvent);
  createDiv('<br>')
}

function myInputEvent() {
  if(this.value() == "vreausaticurglapticingura") {
    myDiv = createDiv('<span class="center" style="font-family: \'Courier New\'">Bine ai revenit, Ștefan!<br><br>În caz de ai uitat, aici păstrezi notițele SUPER secrete pe care le ai despre al tău fizic.<br>Mai jos vei găsi desenul explicativ, multă baftă!<br><br><a href="https://i.imgur.com/GpSZP2r.jpg" target="_blank">Desen.</a></span>');
  }
}

function draw() {
  background(0);
}
