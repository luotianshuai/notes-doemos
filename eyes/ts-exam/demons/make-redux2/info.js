const initState = {
    name: '前端九部',
    description: '我们都是前端爱好者！'
};

export function setName(text) {
    return { type: "SET_NAME", text}
}

export function setDescription(text) {
    return { type: "SET_DESCRIPTION", text}
}

// InfoReducer，一个子reducer
// 注意：InfoReducer 接收的 state 是 state.info
export function InfoReducer(state=initState, action) {
    switch (action.type) {
        case 'SET_NAME':
            return {...state, name: action.text};
        case 'SET_DESCRIPTION':
            return {...state, description: action.text};
        default:
            return state
    }
}
