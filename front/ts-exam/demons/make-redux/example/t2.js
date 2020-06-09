// 当然上面的有一个很明显的问题：修改 count 之后，使用 count 的地方不能收到通知。我们可以使用发布-订阅模式来解决这个问题
let state = {
    count: 1
};

// 发布订阅实践
let listeners = [];

function subscribe(listener) {
    listeners.push(listener);
}

// 当 count 改变的时候我们要通知所有的订阅者

function changeCount(count) {
    state.count = count;

    for (let i =0; i < listeners.length ; i++) {
        const listener = listeners[i];
        listener();
    }
}

// 订阅一下
subscribe(() => {console.log(state.count)});


// 我们来修改下 state，当然我们不能直接去改 state 了，我们要通过 changeCount 来修改
changeCount(2);
changeCount(3);
changeCount(4);

// 现在有两个新的问题摆在我们面前
//
// 这个状态管理器只能管理 count，不通用
// 公共的代码要封装起来
// 我们尝试来解决这个问题，把公共的代码封装起来
