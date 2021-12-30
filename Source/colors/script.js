// TODO:
// * add VIC and TED
// * emulate checkerboard pattern artifact

window.onload = init;




// START
// https://www.pepto.de/projects/colorvic/
// START


function byId(...args){
    return document.getElementById(...args);
}

function create(...args){
    return document.createElement(...args);
}

const { abs , min , max , cos , sin , pow , floor , round , PI } = Math;

const UI = [
    'limit_lumadiff',
    'saturation',
    'brightness',
    'lumalevels',
    'contrast',
    'lumadiff',
    'pattern',
    'sortby',
    'gamma',
    'mixed',

    'showcomponents',
    'showmixedcol',
    'showeffcol',
    'showluma',

    'saturation_val',
    'brightness_val',
    'lumadiff_val',
    'contrast_val',
    'gamma_val',

    'lumadiff_div',
    'collink',
    'numcol',
    'allcoltab',
    'hexcolors',
    'i_text_basic',

    'text_basic2_lower',
    'text_basic2_upper',

    'row0',
    'row1',
    'row2',
    'row3'
];

/*
 *  Generate vars for UI elements
 */

function findComponents(){
    for(const element of UI)
        window[`ui_${ element }`] = byId(element);
}

/*
 *  HTML Calls
 */

function preset(mixed,lumadiff){
	ui_lumalevels.selectedIndex = 1; // new VIC-II
	ui_mixed.value = mixed;
	ui_lumadiff.value = lumadiff / 10;
	refresh();
}

function toggleCase(idA,idB){

    const [ styleA , styleB ] = [ byId(idA).style , byId(idB).style ];

    const style = (styleA.display === '')
        ? [ 'none' , '' ]
        : [ '' , 'none' ] ;

    [ styleA.display , styleB.display ] = style;
}

function copyElement(idA,idB){

    const text = ui_i_text_basic;

    const
        elementA = byId(idA),
        elementB = byId(idB);

    text.value = (elementA.style.display === '')
        ? elementA.innerHTML
        : elementB.innerHTML;

    text.style = '';
    text.select();
    document.execCommand('copy');
    text.style.display = 'none';
}


const lumadiff_limit1 = 5;
const lumadiff_limit2 = 31;

let levels = { mc: [ 0 ], fr: [ 0 ] };            // Black (luma switched off)

with ( levels )
{
    // most common

    mc[ 0x6 ] = mc[ 0x9 ] =  8;                   // Blue,    Brown
    mc[ 0xb ] = mc[ 0x2 ] = 10;                   // Dk.Grey, Red
    mc[ 0x4 ] = mc[ 0x8 ] = 12;                   // Purple,  Orange
    mc[ 0xc ] = mc[ 0xe ] = 15;                   // Md.Grey, Lt.Blue
    mc[ 0x5 ] = mc[ 0xa ] = 16;                   // Green,   Lt.Red
    mc[ 0xf ] = mc[ 0x3 ] = 20;                   // Lt.Grey, Cyan
    mc[ 0x7 ] = mc[ 0xd ] = 24;                   // Yellow,  Lt.Green
    mc[ 0x1 ]             = 32;                   // White

    // first revision

    fr[ 0x2 ] = fr[ 0x6 ] = fr[ 0x9 ] = fr[ 0xb ]                         = 8 * 1;
    fr[ 0x4 ] = fr[ 0x5 ] = fr[ 0x8 ] = fr[ 0xa ] = fr[ 0xc ] = fr[ 0xe ] = 8 * 2;
    fr[ 0x3 ] = fr[ 0x7 ] = fr[ 0xd ] = fr[ 0xf ]                         = 8 * 3;
    fr[ 0x1 ]                                                             = 8 * 4;
}


let angles = [];

angles[ 0x4 ]                 = 2;                // Purple
angles[ 0x2 ] = angles[ 0xa ] = 4;                // Red
angles[ 0x8 ]                 = 5;                // Orange
angles[ 0x9 ]                 = 6;                // Brown
angles[ 0x7 ]                 = 7;                // Yellow
angles[ 0x5 ] = angles[ 0xd ] = 2 + 8;            // Green
angles[ 0x3 ]                 = 4 + 8;            // Cyan
angles[ 0x6 ] = angles[ 0xe ] = 7 + 8;            // Blue


function compose( index , revision , brightness , contrast , saturation ){

    const
        level = levels[revision][index],
        angle = angles[index];


    //  Constants

    const
        sector = 360 / 16,
        origin = sector / 2,
        radian = PI / 180,
        screen = 1 / 5;

    //  Normalize

    saturation *= 1 - screen;
    brightness -= 50;
    contrast /= 100;

    //  Construct

    const components = { u : 0 , v : 0 }; // monochrome (chroma switched off)


    if(angle){
        const alpha = radian * (origin + angle * sector);

        components.u = cos(alpha) * saturation;
        components.v = sin(alpha) * saturation;
    }

    components.y = 8 * level + brightness;

    for(const component in components)
        components[component] *= contrast + screen;

    return components;
}


function convert( components , source ){

    const { y , u , v } = components;

    //  Matrix Transformation

    const color = {
        r : y + 1.140 * v ,
        g : y - 0.396 * u - 0.581 * v ,
        b : y + 2.029 * u
    };

    // color.r = components.y                        + 1.140 * components.v;
    // color.g = components.y - 0.396 * components.u - 0.581 * components.v;
    // color.b = components.y + 2.029 * components.u;

    //  Gamma Correction

    const target = 1 / 2.2;                            // sRGB

    for( channel in color ){

        let value = color[channel];

        value = max(min(color[channel],255 ),0);
        value = (255 ** (1 - source)) * (value ** source);
        value = (255 ** (1 - target)) * (value ** target);

        color[channel] = round(value);
    }

    // color.y = components.y;
    // color.u = components.u;
    // color.v = components.v;

    return { ...color , ...components };
}

// END
// https://www.pepto.de/projects/colorvic/
// END


// https://stackoverflow.com/questions/5623838

function CToHex(component){
    return ( component | 0 )
        .toString(16)
        .padStart(2,'0');
}

function RGBToHex({ r , g , b }){
    return `#${ CToHex(r) }${ CToHex(g) }${ CToHex(b) }`;
}



// https://css-tricks.com/converting-color-spaces-in-javascript/

function HSLToRGB(h,s,l){

  // Must be fractions of 1

    s /= 100;
    l /= 100;

    const
        c = (1 - abs(2 * l - 1)) * s,
        x = c * (1 - abs((h / 60) % 2 - 1)),
        m = l - c / 2;

    let [ r , b , g ] = [ 0 , 0 , 0 ];


    const between = (lower,upper) =>
        lower <= h && h < upper;

    switch(true){
    case between(0,60):
        r = c;
        g = x;
        break;
    case between(60,120):
        g = c;
        r = x;
        break;
    case between(120,180):
        g = c;
        b = x;
        break;
    case between(180,240):
        b = c;
        g = x;
        break;
    case between(240,300):
        b = c;
        r = x;
        break;
    case between(300,360):
        r = c;
        b = x;
        break;
    }


    r = round((r + m) * 255);
    g = round((g + m) * 255);
    b = round((b + m) * 255);

    return { r , g , b };
}

function HSLfromRGB({ r , g , b }) {
  r /= 255;
  g /= 255;
  b /= 255;

  let cmin = Math.min(r,g,b),
      cmax = Math.max(r,g,b),
      delta = cmax - cmin,
      h = 0,
      s = 0,
      l = 0;
  if (delta == 0)
    h = 0;
  else if (cmax == r)
    h = ((g - b) / delta) % 6;
  else if (cmax == g)
    h = (b - r) / delta + 2;
  else
    h = (r - g) / delta + 4;

  h = Math.round(h * 60);

  if (h < 0)
      h += 360;

  l = (cmax + cmin) / 2;

  s = delta == 0 ? 0 : delta / (1 - Math.abs(2 * l - 1));

  s = +(s * 100).toFixed(1);
  l = +(l * 100).toFixed(1);

  return { h: h, s: s, l: l };
}

// https://github.com/antimatter15/rgb-lab
// MIT-licensed

function RGBToLab({ r , g , b }){

  r /= 255;
  g /= 255;
  b /= 255;
  let x, y, z;

  r = (r > 0.04045) ? Math.pow((r + 0.055) / 1.055, 2.4) : r / 12.92;
  g = (g > 0.04045) ? Math.pow((g + 0.055) / 1.055, 2.4) : g / 12.92;
  b = (b > 0.04045) ? Math.pow((b + 0.055) / 1.055, 2.4) : b / 12.92;

  x = (r * 0.4124 + g * 0.3576 + b * 0.1805) / 0.95047;
  y = (r * 0.2126 + g * 0.7152 + b * 0.0722) / 1.00000;
  z = (r * 0.0193 + g * 0.1192 + b * 0.9505) / 1.08883;

  x = (x > 0.008856) ? Math.pow(x, 1/3) : (7.787 * x) + 16/116;
  y = (y > 0.008856) ? Math.pow(y, 1/3) : (7.787 * y) + 16/116;
  z = (z > 0.008856) ? Math.pow(z, 1/3) : (7.787 * z) + 16/116;

  return {l: (116 * y) - 16, a: 500 * (x - y), b: 200 * (y - z)};
}

// calculate the perceptual distance between colors in CIELAB
// https://github.com/antimatter15/rgb-lab
// https://github.com/THEjoezack/ColorMine/blob/master/ColorMine/ColorSpaces/Comparisons/Cie94Comparison.cs

function deltaE(labA, labB){
  let deltaL = labA.l - labB.l;
  let deltaA = labA.a - labB.a;
  let deltaB = labA.b - labB.b;
  let c1 = Math.sqrt(labA.a * labA.a + labA.b * labA.b);
  let c2 = Math.sqrt(labB.a * labB.a + labB.b * labB.b);
  let deltaC = c1 - c2;
  let deltaH = deltaA * deltaA + deltaB * deltaB - deltaC * deltaC;
  deltaH = deltaH < 0 ? 0 : Math.sqrt(deltaH);
  let sc = 1.0 + 0.045 * c1;
  let sh = 1.0 + 0.015 * c1;
  let deltaLKlsl = deltaL / (1.0);
  let deltaCkcsc = deltaC / (sc);
  let deltaHkhsh = deltaH / (sh);
  let i = deltaLKlsl * deltaLKlsl + deltaCkcsc * deltaCkcsc + deltaHkhsh * deltaHkhsh;
  return i < 0 ? 0 : Math.sqrt(i);
}

function drawScreen(screen) {
	let xres = 40;
	let yres = 25;
	let canvas = byId('colspace_diagram');
	canvas.width = xres * 8;
	canvas.height = yres * 8;
	let context = canvas.getContext('2d');
	let imgData = context.getImageData(0, 0, canvas.width, canvas.height);
	let oo = 0;
	for (let y = 0; y < yres; y++) {
		for (let x = 0; x < xres; x++) {
			let a = screen.data[oo++];
			let b = screen.data[oo++];
			let c1 = basecolors[a >> 4];
			let c2 = basecolors[a & 0xf];
			for (let x1 = 0; x1 < 8; x1++) {
				for (let y1 = 0; y1 < 8; y1++) {
					let fx = x * 8 + x1;
					let fy = y * 8 + y1;
					let condition = ((screen.pattern[(b << 2) | (y1 & 3)]) >> (7 - x1)) & 1;
					let o = 4 * (fy * (xres * 8) + fx)
					imgData.data[o] = condition ? c1.r : c2.r;
					imgData.data[o + 1] = condition ? c1.g : c2.g;
					imgData.data[o + 2] = condition ? c1.b : c2.b;
					imgData.data[o + 3] = 255;
				}
			}
		}
	}
	context.putImageData(imgData, 0, 0);
}

function bestMatch(rgb){

	let
        bestDistance = Number.MAX_SAFE_INTEGER,
        closest;

    colors.forEach((color) => {

        const
            labA = RGBToLab(color),
            labB = RGBToLab(rgb),
            distance = deltaE(labA,labB);

        if(distance < bestDistance){
            bestDistance = distance;
            closest = color;
        }
    });

	return closest;
}

const saturationThreshold = 15; // lower numbers are gray

function getColorspaceMap3(){

	// put colors into gray and colored buckets

    sortedColors = []
	grays = [];
	nongrays = [];

    for(const color of colors)
        if(color.s < saturationThreshold)
            grays.push(color);
        else
            nongrays.push(color);

	// put colors into 7 hue buckets

	let hueBucketThresholds = [ 10 , 60 , 88 , 160 , 200 , 260 , 340 ];

	const hueBuckets = hueBucketThresholds.length;

    let colorsByHue = Array(hueBuckets).fill([]);

    // for(let i = 0;i < hueBuckets;i++)
		// colorsByHue[i] = [];

	for(let g = 0;g < nongrays.length;g++)
		for(let b = 0;b < hueBuckets;b++){

            const color = nongrays[g];

            let good = false;

            const { h } = color;

			if(b == 0 && floor(h) > hueBucketThresholds[hueBucketThresholds.length - 1])
				good = true;

			if(floor(h) < hueBucketThresholds[b])
				good = true;

			if(good){
				colorsByHue[b].push(color);
				break;
			}
		}

	// sort grays and colors

    const colorsByY = ({ y : a },{ y : b }) => a - b;

	grays = grays.sort(colorsByY);

    colorsByHue = colorsByHue.map((bucket) => {
        return bucket.sort(colorsByY);
    });

	// init map

	colorspaceMap = Array(1000).fill(0);

	const scrx = 40;


	// draw colors at the bottom

    for(let b = 0;b < hueBuckets;b++){

        const colors = colorsByHue[b];

    	for(let c = 0;c < colors.length;c++){
			y = 24 - hueBuckets + b;
			colorspaceMap[y * scrx + c] = colors[c];
		}
    }


	// draw grays at the very bottom

    y = 24;

    for(let g = 0;g < grays.length;g++)
		colorspaceMap[y * scrx + g] = grays[g];


	// draw colorspace diagram


	const paletteheight = (colors.length <= 160)
        ? 1
        : 8 ;

	const
        xres = 40,
	    yres = 25 - hueBuckets - 2 - paletteheight;

	for(let y = 0;y < yres;y++){

        const f = pow(y / yres,1.5);
        const Y = (y + paletteheight) * scrx;


		for(let x = 0;x < xres;x++){

			const
                h = x * 360 / xres,
			    l = f * yres * 100 / yres;

            rgb = HSLToRGB(h,100,l);

			colorspaceMap[Y + x] = bestMatch(rgb);
		}
    }


	// draw colors sorted by lumadiff at the top of the screen

    for(let i = 0;i < colors_by_lumadiff.length;i++)
		colorspaceMap[i] = colors_by_lumadiff[i];

	return colorspaceMap;
}


function svgForColors(colorA,colorB,f,pattern){

    let
        hexA = RGBToHex(colorA),
        hexB = RGBToHex(colorB);

    const path = (color,path) =>
        `<path stroke = '${ color }' d = '${ path }'></path>`;

    const svg = (width,height,viewbox,strokes) =>
        `<svg
            xmlns = 'http://www.w3.org/2000/svg'
            shape-rendering = 'auto'
            viewBox = '${ viewbox }'
            height = '${ height }'
            width = '${ width }'
        >${ strokes.join('') }</svg>`;

    // console.log(mixed,pattern)

	switch(mixed){
	case '0':
	case '2':
		switch(pattern){
		case 'h':
            return svg(1,2,'0 -.5 1 2',[
                path(hexA,'M0 0h1'),
                path(hexB,'M0 1h1')
            ]);
			// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1" height="2" shape-rendering="auto" viewBox="0 -.5 1 2">'
			// svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
			// svg += '</svg>'
			// return svg;
		case 'v':
            return svg(2,1,'0 -.5 2 1',[
                path(hexA,'M0 0h1'),
                path(hexB,'M0 0h1')
            ]);
			// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="1" shape-rendering="auto" viewBox="0 -.5 2 1">'
			// svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M1 0h1"></path>'
			// svg += '</svg>'
			// return svg;
		case 'c':
            return svg(2,2,'0 -.5 2 2',[
                path(hexA,'M0 0h1'),
                path(hexB,'M1 0h1'),
                path(hexB,'M0 1h1'),
                path(hexA,'M1 1h1')
            ]);
			// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2" shape-rendering="auto" viewBox="0 -.5 2 2">'
			// svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M1 0h1"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
			// svg += '<path stroke="' + hexcolor1 + '" d="M1 1h1"></path>'
			// svg += '</svg>'
			// return svg;
		case 'c2':
            return svg(4,2,'0 -.5 4 2',[
                path(hexA,'M0 0h2'),
                path(hexB,'M2 0h2'),
                path(hexB,'M0 1h2'),
                path(hexA,'M2 1h2')
            ]);
			// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="2" shape-rendering="auto" viewBox="0 -.5 4 2">'
			// svg += '<path stroke="' + hexcolor1 + '" d="M0 0h2"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M2 0h2"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M0 1h2"></path>'
			// svg += '<path stroke="' + hexcolor1 + '" d="M2 1h2"></path>'
			// svg += '</svg>'
			// return svg;
        default:
            return '';
		}
	case '4':
		if(f == .25 || f == .75){

            if(f != .75)
                [ hexA , hexB ] = [ hexB , hexA ];

			switch(pattern){
			case 'v':
                return svg(2,2,'0 -.5 2 2',[
                    path(hexA,'M0 0h1'),
                    path(hexB,'M1 0h1'),
                    path(hexA,'M0 1h2')
                ]);
				// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2" shape-rendering="auto" viewBox="0 -.5 2 2">'
				// svg += '<path stroke="' + hexcolora + '" d="M0 0h1"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M1 0h1"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 1h2"></path>'
				// svg += '</svg>'
				// return svg;
			case 'v2':
                return svg(4,2,'0 -.5 4 2',[
                    path(hexA,'M0 0h2'),
                    path(hexB,'M2 0h2'),
                    path(hexA,'M0 1h4')
                ]);
				// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="2" shape-rendering="auto" viewBox="0 -.5 4 2">'
				// svg += '<path stroke="' + hexcolora + '" d="M0 0h2"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M2 0h2"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 1h4"></path>'
				// svg += '</svg>'
				// return svg;
			case 'c':
                return svg(2,4,'0 -.5 2 4',[
                    path(hexA,'M0 0h1'),
                    path(hexB,'M1 0h1'),
                    path(hexA,'M0 1h2'),
                    path(hexB,'M0 2h1'),
                    path(hexA,'M1 2h1'),
                    path(hexA,'M0 3h2')
                ]);
				// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="4" shape-rendering="auto" viewBox="0 -.5 2 4">'
				// svg += '<path stroke="' + hexcolora + '" d="M0 0h1"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M1 0h1"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 1h2"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M0 2h1"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M1 2h1"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 3h2"></path>'
				// svg += '</svg>'
				// return svg;
			case 'c2':
                return svg(4,4,'0 -.5 4 4',[
                    path(hexA,'M0 0h2'),
                    path(hexB,'M2 0h2'),
                    path(hexA,'M0 1h4'),
                    path(hexB,'M0 2h2'),
                    path(hexA,'M2 2h2'),
                    path(hexA,'M0 3h4')
                ]);
				// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="4" shape-rendering="auto" viewBox="0 -.5 4 4">'
				// svg += '<path stroke="' + hexcolora + '" d="M0 0h2"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M2 0h2"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 1h4"></path>'
				// svg += '<path stroke="' + hexcolorb + '" d="M0 2h2"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M2 2h2"></path>'
				// svg += '<path stroke="' + hexcolora + '" d="M0 3h4"></path>'
				// svg += '</svg>'
				// return svg;
			}
		} else {
            return svg(1,2,'0 -.5 1 2',[
                path(hexA,'M0 0h1'),
                path(hexB,'M0 1h1')
            ]);
			// const svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1" height="2" shape-rendering="auto" viewBox="0 -.5 1 2">'
			// svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
			// svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
			// svg += '</svg>'
			// return svg;
		}

        return '';
    default:
        return '';
	}
}

function imageFromColor(c,pattern){

	component1 = c.component1;
	component2 = c.component2;

    if(!component1){
		component1 = c;
		component2 = c;
	}

	svg = encodeURIComponent(svgForColors(component1,component2,c.f,pattern));
	   // .replace(/#/g,'%23');

    image = `url("data:image/svg+xml;utf8,${ svg }")`;
	return image;
}

const bpatterns = {
	'2' : {
		'h' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0, 0, 0, 0,             // 0.25 (unused)
			0x00, 0xff, 0x00, 0xff, // 0.5
			0, 0, 0, 0,             // 0.75 (unused)
		],
		'v' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0, 0, 0, 0,             // 0.25 (unused)
			0x55, 0x55, 0x55, 0x55, // 0.5
			0, 0, 0, 0,             // 0.75 (unused)
		],
		'c' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0, 0, 0, 0,             // 0.25 (unused)
			0x55, 0xaa, 0x55, 0xaa, // 0.5
			0, 0, 0, 0,             // 0.75 (unused)
		],
		'c2' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0, 0, 0, 0,             // 0.25 (unused)
			0x33, 0xcc, 0x33, 0xcc, // 0.5
			0, 0, 0, 0,             // 0.75 (unused)
		],
	},
	'4' : {
		'v' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0x55, 0x00, 0x55, 0x00, // 0.25
			0x00, 0xff, 0x00, 0xff, // 0.50
			0x55, 0xff, 0x55, 0xff, // 0.75
		],
		'v2' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0x33, 0x00, 0x33, 0x00, // 0.25
			0x00, 0xff, 0x00, 0xff, // 0.50
			0x33, 0xff, 0x33, 0xff, // 0.75
		],
		'c' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0x55, 0x00, 0xaa, 0x00, // 0.25
			0x00, 0xff, 0x00, 0xff, // 0.50
			0x55, 0xff, 0xaa, 0xff, // 0.75
		],
		'c2' : [
			0x00, 0x00, 0x00, 0x00, // 0.00
			0x33, 0x00, 0xcc, 0x00, // 0.25
			0x00, 0xff, 0x00, 0xff, // 0.50
			0x33, 0xff, 0xcc, 0xff, // 0.75
		],
	}
};

function createBASICProgram(screen, comment) {
	let text = '0 rem ' + colors.length + ' colors';
	if (mixed == '2') {
		text += ', 50% mixed';
	} else if (mixed == '4') {
		text += ', 25/50/75% mixed';
	}
	text += '\n';

	text += '1 rem ' + comment + '\n';
	text += '2 rem\n';

	let line = '';
	let lineno = 100;
	let start_of_line = true;
	for (let i = 0; i < screen.data.length; i++) {
		if (!start_of_line) {
			line += ',';
			start_of_line = false;
		}
		start_of_line = false;
		let a = screen.data[i];
		if (a) {
			line += '' + a;
		}
		if (line.length > 65) {
			text += '' + lineno + ' data' + line + '\n';
			lineno += 1;
			line = '';
			start_of_line = true;
		}
	}
	text += '' + lineno + ' data' + line + '\n';

	text += '200 v=53248:g=8192+16384:s=1024+16384' + '\n';

	let bpattern = screen.pattern;

	text += '210 a(0)=' + bpattern[0] + ':b(0)=' + bpattern[1] + ':c(0)=' + bpattern[2] + ':d(0)=' + bpattern[3] + '' + '\n';
	text += '220 a(1)=' + bpattern[4] + ':b(1)=' + bpattern[5] + ':c(1)=' + bpattern[6] + ':d(1)=' + bpattern[7] + '' + '\n';
	text += '230 a(2)=' + bpattern[8] + ':b(2)=' + bpattern[9] + ':c(2)=' + bpattern[10] + ':d(2)=' + bpattern[11] + '' + '\n';
	text += '240 a(3)=' + bpattern[12] + ':b(3)=' + bpattern[13] + ':c(3)=' + bpattern[14] + ':d(3)=' + bpattern[15] + '' + '\n';

	text += '300 poke56576,peek(56576)and254' + '\n';
	text += '310 pokev+32,0' + '\n';
	text += '320 pokev+17,peek(v+17)or(11*16)' + '\n';
	text += '330 pokev+22,peek(v+22)and(255-16)' + '\n';
	text += '340 pokev+24,peek(v+24)or8' + '\n';

	text += '400 fori=0to' + (screen.data.length / 2 - 1) + ':readx:ready:pokes+i,x' + '\n';
	text += '410 forj=g+i*8tog+i*8+7step4' + '\n';
	text += '420 pokej,a(y):pokej+1,b(y):pokej+2,c(y):pokej+3,d(y):next' + '\n';
	text += '430 next' + '\n';

	text += '440 fori=ito999:pokes+i,0:next' + '\n';

	text += '640 goto640' + '\n';

	text += 'run' + '\n';
	text += '\n';
	return text;
}



let colors;
let colors_by_lumadiff;

function init(){

    findComponents();
	reset();
    useURLData();
	refresh();
}

function useURLData(){

    const { search } = window.location;
    const urlParams = new URLSearchParams(search);

    if(urlParams.has('levels'))
        switch(urlParams.get('levels')){
        case '5':
            ui_lumalevels.selectedIndex = 0;
            break;
        case '7':
        default:
            ui_lumalevels.selectedIndex = 1;
            break;
        }

    if(urlParams.has('mixed')){
        const mixed = urlParams.get('mixed');
        ui_mixed.value = mixed;
        // prevent detecting as user-initiated mode switch
        old_mixed = mixed;
    }

    if(urlParams.has('lumadiff')){

        const
            lumaDelta = urlParams.get('lumadiff') / 10,
            isLarge = lumaDelta > lumadiff_limit1;

        ui_limit_lumadiff.checked = ! isLarge;

        ui_lumadiff.value = lumaDelta;
        ui_lumadiff.max = (isLarge)
            ? lumadiff_limit2
            : lumadiff_limit1;
    }

    if(urlParams.has('b'))
        ui_brightness.value = urlParams.get('b');

    if(urlParams.has('c'))
        ui_contrast.value = urlParams.get('c');

    if(urlParams.has('s'))
        ui_saturation.value = urlParams.get('s');

    if(urlParams.has('g'))
        ui_gamma.value = urlParams.get('g') * 10;

    if(urlParams.has('sortby'))
        ui_sortby.value = urlParams.get('sortby');

    if(urlParams.has('pattern'))
        ui_pattern.value = urlParams.get('pattern');
}

let old_mixed;

function refresh(){

    /*
     *  Limit luma delta
     */

    const doLimit = ui_limit_lumadiff.checked;

    ui_lumadiff.max = (doLimit)
        ? lumadiff_limit1
        : lumadiff_limit2;

    if(doLimit)
        ui_lumadiff.value = min(ui_lumadiff.value,lumadiff_limit1);

    let
        lumalevels = ui_lumalevels.selectedIndex ? 'mc': 'fr',
        lumadiff = parseInt(ui_lumadiff.value) * 10,
        gamma = ui_gamma.value / 10;

    let
        brightness = ui_brightness.value,
        saturation = ui_saturation.value,
        contrast = ui_contrast.value,
        pattern = ui_pattern.value;
    	sortby = ui_sortby.value;
        mixed = ui_mixed.value;

    let
    	showcomponents = ui_showcomponents.checked,
        showmixedcol = ui_showmixedcol.checked,
    	showeffcol = ui_showeffcol.checked,
    	showluma = ui_showluma.checked;


    /*
     *  Copy slider value to text fields
     */

    ui_brightness_val.innerText = brightness;
    ui_saturation_val.innerText = saturation;
    ui_lumadiff_val.innerText = lumadiff;
	ui_contrast_val.innerText = contrast;
	ui_gamma_val.innerText = gamma;


    /*
     *  Enable / Disable luma threshold slider
     */

    {
        let
            pointerEvents,
            opacity,
            toggle,
            invert;

        switch(mixed){
        case '0':
            pointerEvents = 'none';
            opacity = '0.5';
            ui_lumadiff.value = 0;
            break;
        case '2':
            toggle = true;
            break;
        case '4':
            toggle = true;
            invert = true;
            break;
        }

        const { style : luma } = ui_lumadiff_div;
        const { style : pattern } = pattern_div;

        luma.pointerEvents = pattern.pointerEvents = pointerEvents;
        luma.opacity = pattern.opacity = opacity;

        if(toggle){
            const { options } = pattern_element;
            options[0].disabled =   invert;
    		options[2].disabled = ! invert;
        }
    }


	if(mixed != old_mixed){
		old_mixed = mixed;
		pattern_element = ui_pattern;

        pattern_element.value = {
            '0' : 'h' ,
            '2' : 'h' ,
            '4' : 'c'
        }[mixed];

        pattern = pattern_element.value;
	}


    /*
     *  Create Link
     */

    const levels = (lumalevels == 'mc')
        ? '9'
        : '5';

	const args = { levels , mixed , sortby , pattern };

    switch(false){
    case (mixed == '0'):
        args.lumadiff = lumadiff;
        break;
    case (brightness == 50):
        args.b = brightness;
        break;
    case (contrast == 100):
        args.c = contrast;
        break;
    case (gamma == 2.8):
        args.g = gamma.toFixed(1);
        break;
    }

    // if(mixed != '0')
    //     args['lumadiff'] = lumadiff;
    //
	// if(brightness != 50)
	// 	args['b'] = brightness;
    //
    // if(contrast != 100)
	// 	args['c'] = contrast;
    //
	// if(saturation != 50)
	// 	args['s'] = saturation;
    //
	// if(gamma != 2.8)
	// 	args['g'] = gamma.toFixed(1);

    let { href } = window.location;

    href = href
        .split('?')[0]
        .split('#')[0];

    let seperator = '?';

    for(let propery in args){
        href += `${ seperator }${ propery }=${ args[propery] }`;
        seperator = '&';
    }

    ui_collink.href = href;
    //
	// url = window.location.href;
	// url = url.split('?')[0];
	// url = url.split('#')[0];
	// let i = 0;
	// if (Object.keys(args).length) {
	// 	for (let key in args) {
	// 		if (i == 0) {
	// 			url += '?'
	// 		} else {
	// 			url += '&'
	// 		}
	// 		url += key + '=' + args[key];
	// 		i++;
	// 	}
	// }
	// ui_collink.href = url;


    /*
     *  Create Colodore Palette
     */

	colors = [];

	for(let i = 0;i < 16;i++){

		const color = convert(compose(i,lumalevels,brightness,contrast,saturation),gamma);
		const { h , s } = HSLfromRGB(color);

		colors.push({
            ...color ,
            description : i ,
            lumadiff : -1,
            index : i ,
            h , s
        });
	}

	basecolors = colors.slice();


    /*
     *  Create Mixed Colors
     */

	if(mixed != '0'){

        function mixColors(colorA,colorB,f){

            const
                r = (colorA.r * f + colorB.r * (1 - f)) | 0 ,
                g = (colorA.g * f + colorB.g * (1 - f)) | 0 ,
                b = (colorA.b * f + colorB.b * (1 - f)) | 0 ,
                y = (colorA.y * f + colorB.y * (1 - f)) | 0 ;

            const { h , s } = HSLfromRGB({ r , g , b });

            colors.push({
                r , g , b ,
                y , h , s , f ,
                component1 : colorA ,
                component2 : colorB ,
                lumadiff : abs(colorA.y - colorB.y) ,
                index : colors.length
            });
        }

        const { length } = colors;

        for(let i = 0;i < length;i++){

            let a = colors[i];

            for(let j = i + 1;j < length;j++){

            	let b = colors[j];

				for(let f = .25;f <= .75;f += .25){

					if(mixed != '4' && f != .5)
						continue;

                    mixColors(a,b,f);
				}
			}
		}


        /*
         *  Filter
         */

        colors = colors.filter((color) => {
            return color.lumadiff < lumadiff + .001;
        });
	}


	//
	// Sort
	//
	function compare_h(a, b) {
		if (a.h <= 0 && b.h <= 0) {
			// both gray? then sort by Y
			return a.y - b.y;
		}
		if (a.h <= 0) {
			return -1;
		}
		if (b.h <= 0) {
			return 1;
		}
		return a.h - b.h;
	}
	function compare_lumadiff_index(a, b) {
		if (!a.component1 && !b.component1) {
			// both primary colors
			return a.index - b.index;
		}
		if (!a.component1) {
			// first is a primary color
			return -1;
		}
		if (!b.component1) {
			// second is a primary color
			return 1;
		}
		let cmp = a.lumadiff - b.lumadiff;
		if (cmp != 0) {
			return cmp;
		} else {
			cmp = a.component1.index - b.component1.index;
			if (cmp != 0) {
				return cmp;
			} else {
				cmp = a.component2.index - b.component2.index;
				if (cmp != 0) {
					return cmp;
				} else {
					cmp = a.f - b.f;
					return cmp;
				}
			}
		}
	}

	colors_by_lumadiff = colors.slice();
	colors_by_lumadiff.sort(compare_lumadiff_index);
	console.log(colors_by_lumadiff);
	console.log(colors);

    switch(sortby){
    case 'lumadiff':
        colors = colors_by_lumadiff;
        break;
    case 'hue':
        colors = colors.sort(compare_h);
        break;
    case 'luma':
        colors = colors.sort(({ y : a },{ y : b }) => a - b);
        break;
    }


    /*
     *  Create Cells
     */

	row0 = ui_row0;
	row0.innerText = '';

	row1 = ui_row1;
	row1.innerText = '';

    row2 = ui_row2;
	row2.innerText = '';

    row3 = ui_row3;
	row3.innerText = '';


    const types = [];

    if(showcomponents)
        types.push([ row0 , 'ccol' , 'C' ]);

    if(showeffcol)
        types.push([ row1 ,  'col' , 'E' ]);

    if(showmixedcol)
        types.push([ row2 , 'mcol' , 'M' ]);

    if(showluma)
        types.push([ row3 , 'ycol' , 'L' ]);


    if(colors.length > 1){

        const { length } = colors;

        for(const [ row , column , value ] of types){

            colors.forEach((color,i) => {

                const cell = create('td');
    			cell.className = 'colbox'
    			cell.id = `${ column }${ i }`;

    			row.appendChild(cell);

            });

            row.innerHTML += `<td>${ value }</td>`;
        }
    }

    //
    // for (let i = 0; i < colors.length; i++) {
	// 	if (showcomponents) {
	// 		let td = create("td");
	// 		td.className='colbox'
	// 		td.id='ccol' + i;
	// 		row0.appendChild(td);
	// 		if (i == colors.length - 1) row0.innerHTML += '<td>C</td>';
	// 	}
	// 	if (showeffcol) {
	// 		let td = create("td");
	// 		td.className='colbox'
	// 		td.id='col' + i;
	// 		row1.appendChild(td);
	// 		if (i == colors.length - 1) row1.innerHTML += '<td>E</td>';
	// 	}
	// 	if (showmixedcol) {
	// 		td = create("td");
	// 		td.className='colbox'
	// 		td.id='mcol' + i;
	// 		row2.appendChild(td);
	// 		if (i == colors.length - 1) row2.innerHTML += '<td>M</td>';
	// 	}
	// 	if (showluma) {
	// 		td = create("td");
	// 		td.className='colbox'
	// 		td.id='ycol' + i;
	// 		row3.appendChild(td);
	// 		if (i == colors.length - 1) row3.innerHTML += '<td>L</td>';
	// 	}
	// }

	//
	// fill cells with colors
	//
	text_hexcolors = '';
	for (let i = 0; i < colors.length; i++) {
		c = colors[i];
		hexcolor = RGBToHex(c);
		if (showcomponents) {
			component1 = c.component1;
			component2 = c.component2;
			if (component1) {
				let hexcolor1 = RGBToHex(component1);
				let hexcolor2 = RGBToHex(component2);

				html = '<table><tr>';

                let style1,style2;

				switch (c.f) {
					case .25:
						style1 = 'thincolbox25';
						style2 = 'thincolbox75';
						break;
					case .5:
						style1 = 'thincolbox50';
						style2 = 'thincolbox50';
						break;
					case .75:
						style1 = 'thincolbox75';
						style2 = 'thincolbox25';
						break;
				}
				html += '<td class="' + style1 + '" style="background-color: ' + hexcolor1 + '"></td>'
				html += '<td class="' + style2 + '" style="background-color: ' + hexcolor2 + '"></td>'
				html += '</tr></table>';
				byId("ccol"+i).innerHTML = html;
			}
		}
		if (showeffcol) {
			byId("col"+i).style = 'background-color: ' + hexcolor;
		}
		if (showmixedcol) {
			let image = imageFromColor(c,pattern);
			let td = byId("mcol"+i);
			td.style.backgroundImage = image;
			td.innerHTML = '<a href="#color' + i + '">&nbsp;</a>';
		}
		if (showluma) {
			y = (Math.max(c.y, 0) / 307.2 * 255) | 0;
			yhexcolor = RGBToHex({ r : y , g : y , b : y });
			byId("ycol"+i).style = 'background-color: ' + yhexcolor;
		}

		// hex colors
		text_hexcolors += hexcolor + '\n';
	}

	let bpattern;
	if (mixed == '0') {
		bpattern = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	} else {
		bpattern = bpatterns[mixed][pattern];
	}


    /*
     *  Create Colorspace Diagram
     */

	let colorspaceMapBASIC = getColorspaceMap3();

	let screen2 = {
        pattern : bpattern ,
        data : []
    };

    console.log(colorspaceMapBASIC)

	for(let i = 0; i < 1000; i++) {
		let c = colorspaceMapBASIC[i];
		let f = c.f;

        let c1 , c2;

		if (c.component1) {
			c1 = c.component1;
			c2 = c.component2;
			// always put the brighter color in (y % 2) = 0 rows
			if (c1.y < c2.y) {
				c1 = c.component2;
				c2 = c.component1;
				f = 1 - f;
			}
		} else {
			c1 = c;
			c2 = c;
		}
		screen2.data.push(c1.index << 4 | c2.index);
		switch (f) {
			case .25: screen2.data.push(1); break;
			case .5:  screen2.data.push(2); break;
			case .75: screen2.data.push(3); break;
			default:  screen2.data.push(0); break;
		}
	}

	//
	// Create Colorspace Diagram BASIC Demo
	//

	comment = '';

    if(mixed != '0')
		comment = 'pattern "' + pattern + '"';

    text_basic = createBASICProgram(screen2, comment);
    ui_text_basic2_lower.innerHTML = text_basic;
	ui_text_basic2_upper.innerHTML = text_basic.toUpperCase();

	//
	// fill hex text field
	//
	ui_hexcolors.innerHTML = text_hexcolors;

	//
	// number of colors
	//
	ui_numcol.innerHTML = colors.length;

	//
	// colorspace diagram
	//
	let colorspaceMaps = [];

	drawScreen(screen2);


	//
	// all colors table
	//
	allcoltab = ui_allcoltab;

    const headers = [
        '#' , 'mix' , 'index 1' , 'index 2' , 'f' ,
        'c1' , 'c2' , 'luma diff' , 'Y' , 'U' , 'V' ,
        'H' , 'S' , 'L' , 'R' , 'G' , 'B' , 'hex'
    ].map((header) => `<th>${ header }</th>`);


	allcoltab.innerHTML = `<tr>${ headers.join('') }</tr>`;

	for (let i = 0; i < colors.length; i++) {
		let c = colors[i];
		let ci1 = '';
		let ci2 = '';
		let imagem = imageFromColor(c,pattern);
		let image1 = '';
		let image2 = '';
		if (c.component1) {
			ci1 = c.component1.index;
			ci2 = c.component2.index;
			let image1 = imageFromColor(c.component1,pattern);
			let image2 = imageFromColor(c.component2,pattern);
		}

		let tr = create("tr");
		tr.id = 'color' + i;
		allcoltab.appendChild(tr);
		let td;


		td = create("td");
		td.innerHTML = c.index;
		tr.appendChild(td);

		td = create("td");
		td.className='colbox'
		td.style.backgroundImage = imagem;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = ci1;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = ci2;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = c.f ? c.f : '';
		tr.appendChild(td);

		td = create("td");
		td.className='colbox'
		td.style.backgroundImage = image1;
		tr.appendChild(td);

		td = create("td");
		td.className='colbox'
		td.style.backgroundImage = image2;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = c.lumadiff >= 0 ? c.lumadiff.toFixed(1) : '';
		tr.appendChild(td);

		td = create("td");
		y = c.y;
		td.innerHTML = y.toFixed(1);
		if (y < 128) {
			td.style.color = 'white';
		}
		if (y > 255) {
			y = 255;
		}
		td.style.backgroundColor = 'rgb(' + y + ',' + y + ',' + y + ')';
		tr.appendChild(td);

		td = create("td");
		if (!c.component1) {
			td.innerHTML = c.u.toFixed(1);
		}
		tr.appendChild(td);

		td = create("td");
		if (!c.component1) {
			td.innerHTML = c.v.toFixed(1);
		}
		tr.appendChild(td);

		hsl = HSLfromRGB(c);
		td = create("td");
		td.innerHTML = hsl.h;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = hsl.s;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = hsl.l;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = c.r;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = c.g;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = c.b;
		tr.appendChild(td);

		td = create("td");
		td.innerHTML = RGBToHex(c);
		tr.appendChild(td);
	}
}

function reset(){
	byId('brightness').value = 50;
	byId('contrast').value = 100;
	byId('saturation').value = 50;
	byId('gamma').value = 28; // PAL: 2.8
	refresh();
}
