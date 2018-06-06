
const _ = require('lodash');
const fs = require('fs');

var str  = 'teste';

var address = { street : 'Rua', number : 123};
console.log(address.number);
var str = JSON.stringify(address);
var str2 =  _.upperCase(str);

const func = (x) => {
    
   return  x+1;
}

console.log(func(2));



