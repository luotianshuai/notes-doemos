// 创建redux类型
export const ADD_TODO = 'ADD_TODO';
export const TOGGLE_TODO = 'TOGGLE_TODO';
export const SET_VISIBILITY_FILTER = 'SET_VISIBILITY_FILTER';


// 可见度对象
export const VisibilityFilters = {
    SHOW_ALL: 'SHOW_ALL',
    SHOW_COMPLETED: 'SHOW_COMPLETED',
    SHOW_ACTIVE: 'SHOW_ACTIVE'
};


// 每次都手写一个action太难受了写个函数
export function addTodo(text) {
    return {type: ADD_TODO, text}
}

export function toggleTodo(index) {
    return {type: TOGGLE_TODO, index}
}

export function setVisibilityFilter(filter) {
    return {type: SET_VISIBILITY_FILTER, filter}
}

const initState = {
    visibilityFilter: VisibilityFilters.SHOW_ALL,
    todos: [
        {title: "早8点开晨会，分配今天的开发工作", completed: true},
        {title: "早9点和项目经理作开发需求讨论会", completed: false},
        {title: "晚5:30对今日代码进行review", completed: false},
    ]
};

// Redux 首次执行时，state 为 undefined，此时我们可借机设置并返回应用的初始 state
// 使用es6的默认参数来来重置state
export function todoApp(state = initState, action) {
    switch (action.type) {
        case SET_VISIBILITY_FILTER:
            return {...state, visibilityFilter: action.filter};
        case ADD_TODO:
            return {...state, todos: [state.todos, {title: action.text, completed: false}]};
        case TOGGLE_TODO:
            return {...state, todos: state.todos.map((value, index) => {
                    if (index === action.index){
                        return {...value, completed: !value.completed}
                    }else{
                        return value
                    }

            })};
        default:
            return state;
    }
}
