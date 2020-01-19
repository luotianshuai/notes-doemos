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

// 我们来使用这个状态管理器管理多个状态 counter 和 info 试试

let initState = {
    counter: {
        count: 0
    },
    info: {
        name: '',
        description: ''
    }
};

let store = createStore(initState);

// 订阅info
store.subscribe(() => {
   let state = store.getState();
   console.log(`${state.info.name}: ${state.info.description}`)
});

// 订阅count
store.subscribe(() => {
    let state = store.getState();
    console.log(state.counter.count)
});

// 修改info
store.changeState({...store.getState(),info: {name: "前端学习", description: "redux实现"}});

store.changeState({...store.getState(),counter: {count: 1000}});




