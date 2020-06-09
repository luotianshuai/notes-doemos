const imgTest = require("../static/img/1.gif");

module.exports = function () {
    const el = document.createElement("img");
    el.src=imgTest;
    return el;
};
