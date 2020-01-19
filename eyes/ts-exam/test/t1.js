const axios = require('axios');

axios.get("https://github.com/luotianshuai/react-doemos/blob/master/package-lock.json").then(
    function (response) {
        console.log(response)
    }
).catch(
    function (error) {
        console.log(error)
    }
);
