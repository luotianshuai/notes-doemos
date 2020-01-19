// action = {type:'',other:''}, action 必须有一个 type 属性
function plan(state, action) {
    switch (action.type) {
        case 'INCREMENT':
            return {
                ...state,
                count: state.count + 1
            };
        case 'DECREMENT':
            return {
                ...state,
                count: state.count - 1
            };
        default:
            return state
    }
}

// 我们把这个计划告诉 store，store.changeState 以后改变 state 要按照我的计划来改。
const createStore = function (plan, initState) {
    let state = initState;
    let listeners = [];

    // 订阅
    function subscribe(listener) {
        listeners.push(listener)
    }

    // 修改
    function changeState(action) {
        state = plan(state, action);
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

// 把 plan 传进去告诉store修改数据的时候按照 plan 操作
let store = createStore(plan, initState);

// 启用订阅
store.subscribe(() => {
    let state = store.getState();
    console.log(state.count)
});


// 自增
store.changeState({type: "INCREMENT"});
// 自减
store.changeState({type: "DECREMENT"});

// 我先随便改,但是不在计划之内,所以修改无效
store.changeState({
    count: 'abc'
});

// 到这里为止，我们已经实现了一个有计划的状态管理器
// 我们商量一下吧？我们给 plan 和 changeState 改下名字好不好？
// plan 改成 reducer，changeState 改成 dispatch

// 总结
// action 只描述了事情发生的事实并不执行操作
// reducer(plan)
//     1 接收 state 和 action 返回新的state
//     2 指定了如何响应action并发送到store
//     3 保持纯净不要在reducer做这些操作
//         3.1 修改传入参数
//         3.2 执行有副作用做操: 请求api, 路由跳转
//         3.3 调用非纯函数,如Math.random()


