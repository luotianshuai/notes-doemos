import { createStore, combineReducers } from "./redux"
import { funcIncrement, funcDecrement,counterReducer } from "./count"
import { setName, setDescription,InfoReducer } from "./info"


const reducer = combineReducers({
    counter: counterReducer,
    info: InfoReducer
});

// 创建 store 传入reducer 和 初始状态
let store = createStore(reducer);


// 订阅
store.subscribe(() => {
    let state = store.getState();
    console.log(state.counter.count, state.info.name, state.info.description);
});

store.dispatch(funcIncrement());
store.dispatch(funcDecrement());
store.dispatch(setName("新的name: 信心"));
store.dispatch(setDescription("新的setDescription: 坚持 坚定"));
