const initState = {
    count: 0
};

// action只描述有事情要发生这一事实
// 饭店点菜的菜单
const INCREMENT = "INCREMENT";
const DECREMENT = "DECREMENT";

export function funcIncrement() {
    return {type: INCREMENT}
}

export function funcDecrement() {
    return {type: DECREMENT}
}


// counterReducer, 一个子reducer
// 纯函数
// 做饭的厨子根据菜名,做指定的菜
export function counterReducer(state=initState, action) {
    switch (action.type) {
        case INCREMENT:
            return {count: state.count + 1};
        case DECREMENT:
            return {count: state.count - 1};
        default:
            return state
    }
}
