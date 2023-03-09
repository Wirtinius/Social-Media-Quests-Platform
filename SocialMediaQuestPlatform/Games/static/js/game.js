const canvas = document.getElementById('canvas1');
// ctx - context; to get 2d rendering context, call getContext() on the canvas element 
const ctx = canvas.getContext('2d');
const CANVAS_WIDTH = canvas.width = 600;
const CANVAS_HEIGHT = canvas.height = 600;

const playerImage = new Image();
playerImage.src = 'media/shadow_dog.png';
function animate(){
    // clearRect() method is for state the position; first two args are coordinates(starting points) and another two -
    // - are for endpoints 
    ctx.clearRect(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT);
    // fillRect() method is for moving; (x, y, width, height)
    ctx.fillRect(100, 50, 100, 100);
    // before the repaint it calls itself again; just as the loop
    requestAnimationFrame(animate);
};
animate();
