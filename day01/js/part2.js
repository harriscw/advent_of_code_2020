//Read Data
var fs  = require("fs");
var array = fs.readFileSync("input.txt").toString().split('\n');
//console.log(array);

for (i = 0; i < array.length; i++) {
	for (j = 0; j < array.length; j++) {
		for (k = 0; k < array.length; k++) {
			if(parseInt(array[i])+parseInt(array[j])+parseInt(array[k])==2020){
				console.log(parseInt(array[i])*parseInt(array[j])*parseInt(array[k]))
				break;
			}
		}			
		}
	}