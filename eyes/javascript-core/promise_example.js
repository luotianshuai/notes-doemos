
// ES6 规定，Promise对象是一个构造函数，用来生成Promise实例
// Promise构造函数接受一个函数作为参数，该函数的两个参数分别是resolve和reject。它们是两个函数，由 JavaScript 引擎提供，不用自己部署
// 定义后就执行

function getJSON(url){
    const promise = new Promise((resolve, reject) => {

        // 定义就被执行
        console.log("promise 定义执行");

        const handler = function() {
            if (this.readyState !== 4) {
                return;
            }
            if (this.status === 200) {
                resolve(this.response);
            } else {
                reject(new Error(this.statusText));
            }
        };
        const client = new XMLHttpRequest();
        client.open("GET", url);
        client.onreadystatechange = handler;
        client.responseType = "json";
        client.setRequestHeader("Accept", "application/json");
        client.send();

    });

    return promise;
}


// 定义回调函数
// then方法接收两个函数:第一个回调函数是Promise对象的状态变为resolved时调用，第二个回调函数是Promise对象的状态变为rejected时调用
// 其中，第二个函数是可选的，不一定要提供
getJSON("https://api.github.com/users/github").then(
);

console.log('Hi!');

// 上面代码中，Promise 新建后立即执行，所以首先输出的是Promise。
// 然后，then方法指定的回调函数，将在当前脚本所有同步任务执行完才会执行，所以resolved最后输出
