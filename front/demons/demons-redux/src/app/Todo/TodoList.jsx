import React, { Component } from "react"
import styled, { css } from 'styled-components';
import { toggleTodo } from "../state/TodoList"
import {connect} from 'react-redux';

import {Input, Button, List, Table} from "antd";

class TodoList extends Component {
    static defaultProps = {
        columns: [{
            title: "事项",
            dataIndex: "title",
            key: "title",
            render: (text) => <span >{text}</span>
        }]
    };

    constructor(props) {
        super(props);

        console.log(this.props.todos);
        console.log(this.props.columns)
    }


    render() {
        return (
            <div>
                <Box>
                    <div style={{marginTop: "10px", width: "1000px"}}>
                        <List
                            size="large"
                            header={<h2>事项</h2>}
                            bordered
                            dataSource={this.props.todos}
                            renderItem={
                                (item, index) => <List.Item onClick={this.props.onTodoClick.bind(this,index)}>
                                    <div css={ item.completed ? isDoneStyle : ""}>{item.title}</div>
                                </List.Item>
                            }
                        />
                    </div>
                </Box>

                <Box/>
                {this.props.completedNumber} {this.props.uncompletedNumber}
                <Box/>
            </div>
        );
    }
}


const getVisibleTodo = (todos, filter) => {
    switch (filter) {
        case 'SHOW_ALL':
            return todos;
        case 'SHOW_COMPLETED':
            return todos.filter(t => t.completed);
        case 'SHOW_ACTIVE':
            return todos.filter(t => !t.completed);
    }
};


// 每个组件从state里调用哪些数据,是在组件中声明的
// 例如TodoList组件要用state.todos 信息
// 如下
const mapStateToProps = state => {
    return {
        todos: getVisibleTodo(state.todos, state.visibilityFilter),
        completedNumber: (state.todos.filter(t => t.completed)).length,
        uncompletedNumber: state.todos.filter(t => !t.completed).length,
    };
};

const mapDispatchToProps = dispatch => {
    return {
        onTodoClick: id => {dispatch(toggleTodo(id))}
    }
};
const isDoneStyle = css`
    text-decoration: line-through
`;

const Box = styled.div`
    display: flex;
    justify-content:center;
    align-items: center;
`;

export default connect(mapStateToProps,mapDispatchToProps)(TodoList);


