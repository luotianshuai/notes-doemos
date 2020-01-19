// 现在有两个新的问题摆在我们面前
//
// 这个状态管理器只能管理 count，不通用
// 公共的代码要封装起来
// 我们尝试来解决这个问题，把公共的代码封装起来

const createStore = function (initState) {
    let state = initState;
    let listeners = [];

    // 订阅
    function subscribe(listener) {
        listeners.push(listener)
    }

    // 修改
    function changeState(newState) {
        state = newState;
        // 通知
        for (let i = 0; i < listeners.length; i++){
            const listener = listeners[i];
            listener()
        }
    }

    // 获取
    function getState() {
        return state
    }

    return {
        subscribe,
        changeState,
        getState
    }

};


let initState = {
    count: 0
};

let store = createStore(initState);

store.subscribe(() => {
    let state = store.getState();
    console.log(state.count);
});
// 自增
store.changeState({
    count: store.getState().count + 1
});
// 自减
store.changeState({
    count: store.getState().count - 1
});
// 随便改
store.changeState({
    count: 'abc'
});

// 你一定发现了问题，count 被改成了字符串 abc，因为我们对 count 的修改没有任何约束，任何地方，任何人都可以修改
// 我们需要约束，不允许计划外的 count 修改，我们只允许 count 自增和自减两种改变方式
// 那我们分两步来解决这个问题
//    1 制定一个 state 修改计划，告诉 store，我的修改计划是什么
//    2 修改 store.changeState 方法，告诉它修改 state 的时候，按照我们的计划修改

// 我们来设置一个 plan 函数，接收现在的 state，和一个 action，返回经过改变后的新的 state

