let axios=require("axios");
let fetch = require('node-fetch');

url = 'https://api.github.com/users/github';

function getJSON(url){
    const promise = new Promise((resolve, reject) => {
        let result = fetch(url);
        console.log(result);
        resolve(result)
    });

    return promise;
}


getJSON(url).then((data) => {
    console.log(typeof data);
    console.log(data);
});
