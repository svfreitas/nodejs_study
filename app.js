
const _ = require('lodash');
const notes = require('./notes/notes.js').default;

const fs = require('fs');

var str  = 'testeeeeeeeeee';

// var address = { street : 'Rua', number : 123};
// console.log(address.number);
// var str = JSON.stringify(address);
// var str2 =  _.upperCase(str);

// const func = (x) => x+1;

// notes.listNotes();

// console.log(func(3));

const request = require('request');

var somePromise = new Promise((resolve,reject) =>{
    var obj = {name : 'Sergio', idade : 47}
   
    request({url:'https://www.google.com/'}, (error, response, body)=>{
        resolve(body);
       // console.log(response.statusCode);
       // console.log(body);
    })

})

// somePromise.then((message)=>{
//     console.log('Sucesso : ', message);
// }, (errorMessage)=>{
//     console.log('Erro : ', errorMessage);
// })

function teste2(number) {
    setTimeout( () => {
        console.log("TIMEOUT2");
    }, 500);
  };
  

function teste() {
  setTimeout( () => {
      console.log("TIMEOUT");
      teste2();
  }, 0);
};

var a = teste();
console.log("Aguardando...");



