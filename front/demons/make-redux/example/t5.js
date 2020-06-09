// 多文件协作
// 多文件协作-reducer拆分与合并
// 这一小节我们来处理下 reducer 的问题。啥问题
// 我们知道 reducer 是一个计划函数，接收老的 state，按计划返回新的 state。
// 那我们项目中，有大量的 state，每个 state 都需要计划函数，如果全部写在一起会是啥样子呢
// 所有的计划写在一个 reducer 函数里面，会导致 reducer 函数及其庞大复杂。
// 按经验来说，我们肯定会按组件维度来拆分出很多个 reducer 函数，然后通过一个函数来把他们合并起来

let state = {
    counter: {
        count: 0
    },
    info: {
        name: 'redux学习',
        description: '我们都是前端爱好者！'
    }
};

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

    // 分发
    function dispatch(action) {
        state = reducer(state, action);
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
        changeState,
        dispatch,
        getState
    }

};


// counterReducer, 一个子reducer
// 注意：counterReducer 接收的 state 是 state.counter
function counterReducer(state, action) {
    switch (action.type) {
        case 'INCREMENT':
            return {
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

// InfoReducer，一个子reducer
// 注意：InfoReducer 接收的 state 是 state.info
function InfoReducer(state, action) {
    switch (action.type) {
        case 'SET_NAME':
            return {
                ...state,
                name: action.name
            };
        case 'SET_DESCRIPTION':
            return {
                ...state,
                description: action.description
            };
        default:
            return state
    }
}

function combineReducers(reducers) {
    // reducerKeys = ['counter', 'info']
    const reducerKeys = Object.keys(reducers);

    // 返回新的reducer函数
    return function (state = {}, action) {
        // 生成新的state
        const newState = {};

        // 遍历执行所有的reducers,整合成为一个新的state
        for (let i = 0; i < reducerKeys.length; i++){
            const key = reducerKeys[i];
            const reducer = reducers[key];

            // 之前的 key 的state
            const oldState= state[key];
            // 执行 分reduce 获取新的state
            newState[key] = reducer(oldState, action)
        }

        return newState
    }
}


const reducer = combineReducers({
    counter: counterReducer,
    info: InfoReducer
});

console.log("MD:", reducer);



let initState = {
    counter: {
        count: 0
    },
    info: {
        name: '前端九部',
        description: '我们都是前端爱好者！'
    }
};

// 创建 store 传入reducer 和 初始状态
let store = createStore(reducer, initState);
console.log("ca:", store);

// 订阅
store.subscribe(() => {
    let state = store.getState();
    console.log(state.counter.count, state.info.name, state.info.description);
});

// store.dispatch({
//     type: 'INCREMENT'
// });

