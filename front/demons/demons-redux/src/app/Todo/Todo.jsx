import React, { Component } from "react";
import styled, { css } from 'styled-components';
import TodoList from "./TodoList";
import TodoHeader from "./TodoHeader"


class Index extends Component {
    render() {
        return(
            <div>
                <TodoHeader/>
                <TodoList/>
            </div>
        )
    }
}


export default Index;
