let fs = require('fs');
let thunkify = require('thunkify');
let readFile = thunkify(fs.readFile);

let gen = function* (){
    let r1 = yield readFile('1.txt');  // 第一个 next 卡这里了 返回一个:{ value: [Function], done: false }

    // console.log(typeof r1);  undefined  // yield表达式本身没有返回值，或者说总是返回undefined
    // 如果想从恢复状态,获取r1的值需要在调用next方法传值替换掉,恢复状态后的r1的值
    // 这里想输出结果在第二次调用的时候需要把 一个next 的value返回

    console.log(r1.toString());
    let r2 = yield readFile('2.txt');
    console.log(r2.toString());
};

// method1
let g = gen();
// next方法当被调用的时候,返回一个对象这个对象的value是当前yield表达式的值
let r1 = g.next();
console.log(r1); // { value: [Function], done: false }  Function 需要一个callback


// method 2  Thunk 函数是自动执行 Generator 函数的一种方法。

function run(fn) {
    let gen = fn();


    // 这个为什么要传data? 作为上个阶段异步任务的返回结果，被函数体内的变量r1接收
    // Generator 函数从暂停状态到恢复运行，它的上下文状态（context）是不变的。
    // 通过next方法的参数，就有办法在 Generator 函数开始运行之后，继续向函数体内部注入值。
    // 也就是说，可以在 Generator 函数运行的不同阶段，从外部向内部注入不同的值，从而调整函数行为。
    function next(err, data) {
        let result = gen.next(data);
        // 每次判断是否完成完成返回
        if (result.done) return;
        result.value(next);
    }

    // 递归调用-就实现了每次判断是否完成,如果没有完成继续调用自己
    next();
}


run(gen);
