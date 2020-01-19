// 多文件协作
// 多文件协作-reducer拆分与合并
// 这一小节我们来处理下 reducer 的问题。啥问题
// 我们知道 reducer 是一个计划函数，接收老的 state，按计划返回新的 state。
// 那我们项目中，有大量的 state，每个 state 都需要计划函数，如果全部写在一起会是啥样子呢
// 所有的计划写在一个 reducer 函数里面，会导致 reducer 函数及其庞大复杂。
// 按经验来说，我们肯定会按组件维度来拆分出很多个 reducer 函数，然后通过一个函数来把他们合并起来
// 我们把这个计划告诉 store，store.changeState 以后改变 state 要按照我的计划来改。


// 创建redux对象
export const createStore = function (plan, initState) {
    let state = initState;
    let listeners = [];

    // 订阅
    function subscribe(listener) {
        listeners.push(listener)
    }

    // 分发
    function dispatch(action) {
        state = plan(state, action);
        for (let i = 0; i < listeners.length; i++) {
            const listener = listeners[i];
            listener();
        }
    }

    // 获取
    function getState() {
        return state
    }

    return {
        subscribe,
        dispatch,
        getState
    }

};

// 合并多个reducers的函数
export function combineReducers(reducers) {
    // reducerKeys = ['counter', 'info']
    const reducerKeys = Object.keys(reducers);

    console.log("函数式编程1:", reducerKeys);

    // 返回新的reducer函数
    return function (state = {}, action) {
        // 生成新的state
        const newState = {};

        // 遍历执行所有的reducers
        for (let i = 0; i < reducerKeys.length; i++){
            const key = reducerKeys[i];
            // 定位到指定的reducer
            const reducer = reducers[key];

            // 之前的 key 的state
            const oldState= state[key];

            // 传action,如果这个reducers有这个action返回修改后的状态,当然如果没有匹配到相应的case就返回未修改的状态
            newState[key] = reducer(oldState, action)
        }

        return newState
    }
}







