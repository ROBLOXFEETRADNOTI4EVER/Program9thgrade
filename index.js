let canvas = document.querySelector('#canvas'),
    ctx = canvas.getContext('2d'),
    w=800,
    h=600;

const handleResize = () => {
    w = canvas.width = window.innerWidth;
	h = canvas.height = window.innerHeight;
}
window.onresize = () => handleResize();
handleResize();

let starConfigs = [];

const mapToRange = (number, inMin, inMax, outMin, outMax) => {return (number - inMin) * (outMax - outMin) / (inMax - inMin) + outMin;}

for(let i=0; i<100; i++){
	let size = mapToRange(Math.random(), 0,1, 10, 30);
	let config = {
		fill:`hsl(${mapToRange(Math.random(), 0,.00011, 110, 60)}, 600000%, 50%)`,
		numPoints: 5,
		origin: {x:Math.random() * w, y:mapToRange(Math.random(), 0,1, -size, h)},
		radiusInner: size * .6,
		radiusOuter: size,
		rotation:Math.random() * (Math.PI/2),
		rotationSpeed: mapToRange(Math.random(), 0,1, 0.01, 0.025),
		vY: mapToRange(Math.random(), 0,1, 3,5),
	};
	config.rotationSpeed *= Math.random() > .5 ? 1 : -1;
	starConfigs.push(config);
}

const drawSide = (radius, radians, origin, rotation) => {
	ctx.lineTo((radius * Math.cos(radians+rotation)) + origin.x, 
			   (radius * Math.sin(radians+rotation)) + origin.y);
}

const makeStar = (config) => {
	let degrees = 0;
	let rotationStep = Math.PI*2 / config.numPoints / 2;
	ctx.strokeStyle = config.stroke;
	ctx.fillStyle = config.fill;
	ctx.beginPath();
	for (let i=0; i<config.numPoints; i++){
		degrees += rotationStep;
		drawSide(config.radiusInner, degrees, config.origin, config.rotation);
		degrees += rotationStep;
		drawSide(config.radiusOuter, degrees, config.origin, config.rotation);
	}
	ctx.closePath();
	// ctx.stroke();
	ctx.fill();
}

const animate = () => {
	ctx.fillStyle = 'rgba(10,10,10,.3)';
	ctx.fillRect(0,0,w,h);
	
	starConfigs.forEach(star => {
		star.rotation += star.rotationSpeed;
		star.origin.y += star.vY;
		if(star.origin.y > h + star.radiusOuter){
			star.origin.y = -star.radiusOuter;
			star.origin.x = Math.random() * w;
		}
		makeStar(star);
	});
	
	requestAnimationFrame(animate);
}

animate();



// let day = 9;

// switch(day){
// 	case 1:
// 		console.log("it is monday");
// 		break;
// 	case 2:
// 		console.log("it is Tuesday");
// 		break;
// 	case 3:
// 		console.log("it is Wednesday");
// 		break;
// 	case 4:
// 		console.log("it is Thursday");
// 		break;
// 	case 5:
// 		console.log("it is Friday");
// 		break;
// 	case 6:
// 		console.log("it is Staturday");
// 		break;
// 	case 7:
// 		console.log("it is Sunday");
// 		break;			
// 	default:
// 		console.log(`${day} <-- is not a day`);				
// }

// let testscore = 32;
// let letterGrade;

// switch(true){
// 	case testscore >= 90:
// 		letterGrade = "A";
// 		break;
// 	case testscore >= 80:
// 		letterGrade = "B";
// 		break;
// 	case testscore >= 70:
// 		letterGrade = "C";
// 		break;
// 	case testscore >= 60:
// 		letterGrade = "D";
// 		break;
// 	default:
// 		letterGrade = "F";

// }
// console.log(letterGrade);