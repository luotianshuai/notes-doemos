import React, { Component } from "react";
import {Provider} from 'react-redux';
// import store from "./store";
import TodoHeader from "../TooList/TodoHeader";
import TodoList from "../TooList/TodoList";

import appCss from "../../assets/css/app.css";

class App extends Component {
    render() {
        return(
            // 被Provider包裹的所有组件都可合法的取到store<Provider store={store}>
            <Provider>
                <div className={appCss.app}>
                    {/*<TodoHeader/>*/}
                    <TodoList/>
                    {/*<TodoFooter/>*/}
                </div>
            </Provider>
        )
    }
}

export default App;
