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

const { min , max , cos , sin , pow , round , PI } = Math;

UI = [
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
    'hexcolors'
];

function findComponents(){
    for(const element of UI)
        window[`ui_${ element }`] = byId(element);
    //
    // var
    //     ui_limit_lumadiff = byId('limit_lumadiff'),
    //     ui_saturation = byId('saturation'),
    //     ui_brightness = byId('brightness'),
    //     ui_lumalevels = byId('lumalevels'),
    //     ui_contrast = byId('contrast'),
    //     ui_lumadiff = byId('lumadiff'),
    //     ui_pattern = byId('pattern'),
    //     ui_sortby = byId('sortby'),
    //     ui_gamma = byId('gamma'),
    //     ui_mixed = byId('mixed');
    //
    // var
    //     ui_showcomponents = byId('showcomponents'),
    //     ui_showmixedcol = byId('showmixedcol'),
    //     ui_showeffcol = byId('showeffcol'),
    //     ui_showluma = byId('showluma');
    //
    //
    // var
    //     ui_saturation_val = byId('saturation_val'),
    //     ui_brightness_val = byId('brightness_val'),
    //     ui_lumadiff_val = byId('lumadiff_val'),
    //     ui_contrast_val = byId('contrast_val'),
    //     ui_gamma_val = byId('gamma_val');
    //
    // var
    //     ui_lumadiff_div = byId('lumadiff_div');
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

function hexFromComponent(c){
	const hex = ( c | 0 ).toString(16);
    return hex.padStart(2,'0');
	// return (hex.length == 1) ? '0' + hex : hex;
}

function hexFromRGB(r,g,b){
    return `#${ hexFromComponent(r) }${ hexFromComponent(g) }${ hexFromComponent(b) }`;
	// return "#" + hexFromComponent(r) + hexFromComponent(g) + hexFromComponent(b);
}



// https://css-tricks.com/converting-color-spaces-in-javascript/
function RGBfromHSL(h,s,l) {
  // Must be fractions of 1
  s /= 100;
  l /= 100;

  let c = (1 - Math.abs(2 * l - 1)) * s,
      x = c * (1 - Math.abs((h / 60) % 2 - 1)),
      m = l - c/2,
      r = 0,
      g = 0,
      b = 0;
  if (0 <= h && h < 60) {
    r = c; g = x; b = 0;
  } else if (60 <= h && h < 120) {
    r = x; g = c; b = 0;
  } else if (120 <= h && h < 180) {
    r = 0; g = c; b = x;
  } else if (180 <= h && h < 240) {
    r = 0; g = x; b = c;
  } else if (240 <= h && h < 300) {
    r = x; g = 0; b = c;
  } else if (300 <= h && h < 360) {
    r = c; g = 0; b = x;
  }
  r = Math.round((r + m) * 255);
  g = Math.round((g + m) * 255);
  b = Math.round((b + m) * 255);

  return { r: r, g: g, b: b };
}
function HSLfromRGB(r,g,b) {
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
function LabFromRGB(r, g, b) {
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

function bestMatch(rgb) {
	let cr;
	let mindist = 999;
	for (let i = 0; i < colors.length; i++) {
		c = colors[i];
		let lab1 = LabFromRGB(c.r, c.g, c.b);
		let lab2 = LabFromRGB(rgb.r, rgb.g, rgb.b);
		let dist = deltaE(lab1, lab2);
		if (dist < mindist) {
			mindist = dist;
			cr = c;
		}
	}
	return cr;
}

const saturationThreshold = 15; // lower numbers are gray

function getColorspaceMap3() {
	// put colors into gray and colored buckets
	sortedColors = []
	grays = [];
	nongrays = [];
	for (let i = 0; i < colors.length; i++) {
		let c = colors[i];
		if (c.s < saturationThreshold) {
			grays.push(c);
		} else {
			nongrays.push(c);
		}
	}

	// put colors into 7 hue buckets
	let hueBucketThresholds = [ 10, 60, 88, 160, 200, 260, 340 ];
	const hueBuckets = hueBucketThresholds.length;
	let colorsByHue = [];
	for (let hueBucket = 0; hueBucket < hueBuckets; hueBucket++) {
		colorsByHue[hueBucket] = [];
	}
	for (let i = 0; i < nongrays.length; i++) {
		for (let hueBucket = 0; hueBucket < hueBuckets; hueBucket++) {
			let c = nongrays[i];
			let good = false;
			if (hueBucket == 0 && Math.floor(c.h) > hueBucketThresholds[hueBucketThresholds.length - 1]) {
				good = true;
			}
			if (Math.floor(c.h) < hueBucketThresholds[hueBucket]) {
				good = true;
			}
			if (good) {
				colorsByHue[hueBucket].push(c);
				break;
			}
		}
	}

	// sort grays and colors
	grays = grays.sort((a,b)=>a.y-b.y);
	for (let hueBucket = 0; hueBucket < hueBuckets; hueBucket++) {
		colorsByHue[hueBucket] = colorsByHue[hueBucket].sort((a,b)=>a.y-b.y);
	}

	// init map
	colorspaceMap = [];
	for (let i = 0; i < 1000; i++) {
		colorspaceMap.push(0);
	}

	const scrx = 40;

	// draw colors at the bottom
	for (let hueBucket = 0; hueBucket < hueBuckets; hueBucket++) {
		for (let i = 0; i < colorsByHue[hueBucket].length; i++) {
			y = 24 - hueBuckets + hueBucket;
			colorspaceMap[y * scrx + i] = colorsByHue[hueBucket][i];
		}
	}

	// draw grays at the very bottom
	let l = grays.length;
	for (let i = 0; i < l; i++) {
		y = 24;
		colorspaceMap[y * scrx + i] = grays[i];
	}

	// draw colorspace diagram

	function f(x) {
		return Math.pow(x, 1.5);
	}

	let paletteheight;
	if (colors.length <= 160) {
		paletteheight = 1;
	} else if (colors.length <= 240) {
		paletteheight = 8;
	} else {
		paletteheight = 8;
	}

	let xres = 40;
	let yres = 25 - hueBuckets - 2 - paletteheight;
	for (let y = 0; y < yres; y++) {
		for (let x = 0; x < xres; x++) {
			h = x * 360 / xres;
			l = f(y / yres) * yres * 100 / yres;
			rgb = RGBfromHSL(h, 100, l);
			let c = bestMatch(rgb);
			colorspaceMap[(y + paletteheight) * scrx + x] = c;
		}
	}

	// draw colors sorted by lumadiff at the top of the screen
	for (let i = 0; i < colors_by_lumadiff.length; i++) {
		colorspaceMap[i] = colors_by_lumadiff[i];
	}

	return colorspaceMap;
}


function svgForColors(c1, c2, f, pattern) {
    let svg = '';

	let hexcolor1 = hexFromRGB(c1.r, c1.g, c1.b);
	let hexcolor2 = hexFromRGB(c2.r, c2.g, c2.b);
	switch (mixed) {
		case '0':
		case '2':
			switch (pattern) {
				case 'h':
					svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1" height="2" shape-rendering="auto" viewBox="0 -.5 1 2">'
					svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
					svg += '</svg>'
					break;
				case 'v':
					svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="1" shape-rendering="auto" viewBox="0 -.5 2 1">'
					svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M1 0h1"></path>'
					svg += '</svg>'
					break;
				case 'c':
					svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2" shape-rendering="auto" viewBox="0 -.5 2 2">'
					svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M1 0h1"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
					svg += '<path stroke="' + hexcolor1 + '" d="M1 1h1"></path>'
					svg += '</svg>'
					break;
				case 'c2':
					svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="2" shape-rendering="auto" viewBox="0 -.5 4 2">'
					svg += '<path stroke="' + hexcolor1 + '" d="M0 0h2"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M2 0h2"></path>'
					svg += '<path stroke="' + hexcolor2 + '" d="M0 1h2"></path>'
					svg += '<path stroke="' + hexcolor1 + '" d="M2 1h2"></path>'
					svg += '</svg>'
					break;
			}
			break;
		case '4':
			if (f == .25 || f == .75) {

                let hexcolora , hexcolorb;

				if (f == .75) {
					hexcolora = hexcolor1;
					hexcolorb = hexcolor2;
				} else {
					hexcolora = hexcolor2;
					hexcolorb = hexcolor1;
				}
				switch (pattern) {
					case 'v':
						svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="2" shape-rendering="auto" viewBox="0 -.5 2 2">'
						svg += '<path stroke="' + hexcolora + '" d="M0 0h1"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M1 0h1"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 1h2"></path>'
						svg += '</svg>'
						break;
					case 'v2':
						svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="2" shape-rendering="auto" viewBox="0 -.5 4 2">'
						svg += '<path stroke="' + hexcolora + '" d="M0 0h2"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M2 0h2"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 1h4"></path>'
						svg += '</svg>'
						break;
					case 'c':
						svg = '<svg xmlns="http://www.w3.org/2000/svg" width="2" height="4" shape-rendering="auto" viewBox="0 -.5 2 4">'
						svg += '<path stroke="' + hexcolora + '" d="M0 0h1"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M1 0h1"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 1h2"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M0 2h1"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M1 2h1"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 3h2"></path>'
						svg += '</svg>'
						break;
					case 'c2':
						svg = '<svg xmlns="http://www.w3.org/2000/svg" width="4" height="4" shape-rendering="auto" viewBox="0 -.5 4 4">'
						svg += '<path stroke="' + hexcolora + '" d="M0 0h2"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M2 0h2"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 1h4"></path>'
						svg += '<path stroke="' + hexcolorb + '" d="M0 2h2"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M2 2h2"></path>'
						svg += '<path stroke="' + hexcolora + '" d="M0 3h4"></path>'
						svg += '</svg>'
						break;
				}
			} else {
				svg = '<svg xmlns="http://www.w3.org/2000/svg" width="1" height="2" shape-rendering="auto" viewBox="0 -.5 1 2">'
				svg += '<path stroke="' + hexcolor1 + '" d="M0 0h1"></path>'
				svg += '<path stroke="' + hexcolor2 + '" d="M0 1h1"></path>'
				svg += '</svg>'
				break;
			}
			break;
	}
	return svg;
}

function imageFromColor(c) {
	component1 = c.component1;
	component2 = c.component2;
	if (!component1) {
		component1 = c;
		component2 = c;
	}
	svg = svgForColors(component1, component2, c.f, pattern);
	svg = svg.replace(/#/g, '%23');
	image = "url('data:image/svg+xml;utf8," + svg + "')";
	return image;
}

const bpatterns = {
	'2': {
		'h':
			 [
				0x00, 0x00, 0x00, 0x00, // 0.00
				0, 0, 0, 0,             // 0.25 (unused)
				0x00, 0xff, 0x00, 0xff, // 0.5
				0, 0, 0, 0,             // 0.75 (unused)
			],
		'v':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0, 0, 0, 0,             // 0.25 (unused)
				0x55, 0x55, 0x55, 0x55, // 0.5
				0, 0, 0, 0,             // 0.75 (unused)
			],
		'c':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0, 0, 0, 0,             // 0.25 (unused)
				0x55, 0xaa, 0x55, 0xaa, // 0.5
				0, 0, 0, 0,             // 0.75 (unused)
			],
		'c2':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0, 0, 0, 0,             // 0.25 (unused)
				0x33, 0xcc, 0x33, 0xcc, // 0.5
				0, 0, 0, 0,             // 0.75 (unused)
			],
		},
	'4': {
		'v':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0x55, 0x00, 0x55, 0x00, // 0.25
				0x00, 0xff, 0x00, 0xff, // 0.50
				0x55, 0xff, 0x55, 0xff, // 0.75
			],
		'v2':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0x33, 0x00, 0x33, 0x00, // 0.25
				0x00, 0xff, 0x00, 0xff, // 0.50
				0x33, 0xff, 0x33, 0xff, // 0.75
			],
		'c':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0x55, 0x00, 0xaa, 0x00, // 0.25
				0x00, 0xff, 0x00, 0xff, // 0.50
				0x55, 0xff, 0xaa, 0xff, // 0.75
			],
		'c2':
			[
				0x00, 0x00, 0x00, 0x00, // 0.00
				0x33, 0x00, 0xcc, 0x00, // 0.25
				0x00, 0xff, 0x00, 0xff, // 0.50
				0x33, 0xff, 0xcc, 0xff, // 0.75
			],
	}
}

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

        ui_limit_lumadiff.checked = ! is_large;

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

    const
        lumalevels = ui_lumalevels.selectedIndex ? 'mc': 'fr',
	    mixed = ui_mixed.value,
        lumadiff = parseInt(ui_lumadiff.value) * 10,
    	brightness = ui_brightness.value,
    	contrast = ui_contrast.value,
    	saturation = ui_saturation.value,
    	gamma = ui_gamma.value / 10;
    	sortby = ui_sortby.value,
    	showcomponents = ui_showcomponents.checked,
    	showeffcol = ui_showeffcol.checked,
    	showmixedcol = ui_showmixedcol.checked,
    	showluma = ui_showluma.checked,
	    pattern = ui_pattern.value;


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



        if (mixed == '0') {
    		pattern_div.style.pointerEvents = 'none';
    		pattern_div.style.opacity = '0.5';
    	} else {
    		pattern_div.style.pointerEvents = null;
    		pattern_div.style.opacity = null;
    	}

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


	if (mixed != old_mixed) {
		old_mixed = mixed;
		pattern_element = ui_pattern;
		pattern_element.value = { '0': 'h', '2': 'h', '4': 'c' }[mixed];
		pattern = pattern_element.value;
	}

	//
	// Create Link
	//
	args = {};
	args['levels'] = lumalevels == 'mc' ? '9' : '5';
	args['mixed'] = mixed;
	if (mixed != '0') {
		args['lumadiff'] = lumadiff;
	}
	args['sortby'] = sortby;
	args['pattern'] = pattern;
	if (brightness != 50) {
		args['b'] = brightness;
	}
	if (contrast != 100) {
		args['c'] = contrast;
	}
	if (saturation != 50) {
		args['s'] = saturation;
	}
	if (gamma != 2.8) {
		args['g'] = gamma.toFixed(1);
	}

	url = window.location.href;
	url = url.split('?')[0];
	url = url.split('#')[0];
	let i = 0;
	if (Object.keys(args).length) {
		for (let key in args) {
			if (i == 0) {
				url += '?'
			} else {
				url += '&'
			}
			url += key + '=' + args[key];
			i++;
		}
	}
	ui_collink.href = url;


	//
	// create Colodore palette
	//
	colors = []
	for (let i = 0; i < 16; i++) {
		let c = convert(compose(i, lumalevels, brightness, contrast, saturation), gamma);
		c.index = i;
		c.description = i;
		let hsl = HSLfromRGB(c.r, c.g, c.b);
		c.h = hsl.h;
		c.s = hsl.s;
		c.lumadiff = -1;
		colors.push(c);
	}
	basecolors = colors.slice();

	//
	// create mixed colors
	//
	if (mixed != '0') {
		let l = colors.length;
		for (let i = 0; i < l; i++) {
			let c1 = colors[i];
			for (let j = i+1; j < l; j++) {
				let c2 = colors[j];
				for (let f = .25; f <= .75; f += .25) {
					if (mixed != '4' && f != .5) {
						continue;
					}
					let cm = {}
					cm.r = (c1.r * f + c2.r * (1 - f)) | 0;
					cm.g = (c1.g * f + c2.g * (1 - f)) | 0;
					cm.b = (c1.b * f + c2.b * (1 - f)) | 0;
					cm.y = (c1.y * f + c2.y * (1 - f)) | 0;
					hsl = HSLfromRGB(cm.r, cm.g, cm.b);
					cm.h = hsl.h;
					cm.s = hsl.s;
					cm.index = colors.length;
					cm.f = f;
					cm.component1 = c1;
					cm.component2 = c2;
					cm.lumadiff = Math.abs(c1.y - c2.y);
					colors.push(cm);
				}
			}
		}

		//
		// Filter
		//
		let colors_new = []
		for (let i = 0; i < colors.length; i++) {
			if (colors[i].lumadiff < lumadiff + .001) { // float ftw!
				colors_new.push(colors[i]);
			}
		}
		colors = colors_new;
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

	if (sortby == 'lumadiff') {
		colors = colors_by_lumadiff;
	} else if (sortby == 'hue') {
		colors.sort(compare_h);
	} else if (sortby == 'luma'){
		colors.sort((a,b)=>a.y-b.y);
	}

	//
	// create cells
	//
	row0 = byId("row0");
	row0.innerHTML = '';
	row1 = byId("row1");
	row1.innerHTML = '';
	row2 = byId("row2");
	row2.innerHTML = '';
	row3 = byId("row3");
	row3.innerHTML = '';
	for (let i = 0; i < colors.length; i++) {
		if (showcomponents) {
			let td = create("td");
			td.className='colbox'
			td.id='ccol' + i;
			row0.appendChild(td);
			if (i == colors.length - 1) row0.innerHTML += '<td>C</td>';
		}
		if (showeffcol) {
			let td = create("td");
			td.className='colbox'
			td.id='col' + i;
			row1.appendChild(td);
			if (i == colors.length - 1) row1.innerHTML += '<td>E</td>';
		}
		if (showmixedcol) {
			td = create("td");
			td.className='colbox'
			td.id='mcol' + i;
			row2.appendChild(td);
			if (i == colors.length - 1) row2.innerHTML += '<td>M</td>';
		}
		if (showluma) {
			td = create("td");
			td.className='colbox'
			td.id='ycol' + i;
			row3.appendChild(td);
			if (i == colors.length - 1) row3.innerHTML += '<td>L</td>';
		}
	}

	//
	// fill cells with colors
	//
	text_hexcolors = '';
	for (let i = 0; i < colors.length; i++) {
		c = colors[i];
		hexcolor = hexFromRGB(c.r, c.g, c.b);
		if (showcomponents) {
			component1 = c.component1;
			component2 = c.component2;
			if (component1) {
				let hexcolor1 = hexFromRGB(component1.r, component1.g, component1.b);
				let hexcolor2 = hexFromRGB(component2.r, component2.g, component2.b);

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
			let image = imageFromColor(c);
			let td = byId("mcol"+i);
			td.style.backgroundImage = image;
			td.innerHTML = '<a href="#color' + i + '">&nbsp;</a>';
		}
		if (showluma) {
			y = (Math.max(c.y, 0) / 307.2 * 255) | 0;
			yhexcolor = hexFromRGB(y, y, y);
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

	//
	// Create Colorspace Diagram Screen
	//
	let colorspaceMapBASIC = getColorspaceMap3();
	let screen2 = {};
	screen2.pattern = bpattern;
	screen2.data = [];
	for (let i = 0; i < 1000; i++) {
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
	if (mixed != '0') {
		comment = 'pattern "' + pattern + '"';
	}
	text_basic = createBASICProgram(screen2, comment);
	byId("text_basic2_lower").innerHTML = text_basic;
	byId("text_basic2_upper").innerHTML = text_basic.toUpperCase();

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


	allcoltab.innerHTML = `<tr>${ headers }</tr>`;

	for (let i = 0; i < colors.length; i++) {
		let c = colors[i];
		let ci1 = '';
		let ci2 = '';
		let imagem = imageFromColor(c);
		let image1 = '';
		let image2 = '';
		if (c.component1) {
			ci1 = c.component1.index;
			ci2 = c.component2.index;
			let image1 = imageFromColor(c.component1);
			let image2 = imageFromColor(c.component2);
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

		hsl = HSLfromRGB(c.r, c.g, c.b);
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
		td.innerHTML = hexFromRGB(c.r, c.g, c.b);
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
