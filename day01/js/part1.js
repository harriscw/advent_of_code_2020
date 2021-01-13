//Read Data
var fs  = require("fs");
var array = fs.readFileSync("input.txt").toString().split('\n');
//console.log(array);

for (i = 0; i < array.length; i++) {
	for (j = 0; j < array.length; j++) {
		if(parseInt(array[i])+parseInt(array[j])==2020){
			//throw new Error(parseInt(array[i])*parseInt(array[j]));
			console.log(parseInt(array[i])*parseInt(array[j]))
			break;
		}		
		}
	}