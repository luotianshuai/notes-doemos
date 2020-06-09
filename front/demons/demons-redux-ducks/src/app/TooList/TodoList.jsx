import React, { Component } from "react"
import {connect} from 'react-redux';
import listCss from "../../assets/css/list.css"

class TodoList extends Component {
    // 取得未完成的todo数量
    getUnfinishedCount = () => {
        //this.props.todo就是从connect传入的state数据
        return this.props.todo.filter((i) => {
            return i.isComplete === false;
        }).length;
    };

    // 去完成的todo数量
    getfinishedCount = () => {
        //this.props.todo就是从connect传入的state数据
        return this.props.todo.filter((i) => {
            return i.isComplete === true;
        }).length;
    };



    render() {
        return (
            <div className={listCss.listContent}>
                <div className={listCss.title}><h2>正在进行</h2> <span>{this.getUnfinishedCount()}</span></div>
                <ul>
                    {this.props.todo.map((value,key) => {
                        if (!value.isComplete){
                            return (
                                <li key={key}> <input type={"checkbox"} checked={value.isComplete}/> {value.title}</li>
                            )
                        }
                    })}
                </ul>
                <div className={listCss.title}><h2>已完成</h2> <span>{this.getfinishedCount()}</span></div>
                <ul>
                    {this.props.todo.map((value,key) => {
                        if (value.isComplete){
                            return (
                                <li key={key}> <input type={"checkbox"} checked={value.isComplete}/> {value.title}</li>
                            )
                        }
                    })}
                </ul>
            </div>
        );
    }
}

//导出注入后的组件
export default connect((state) => ({
    ...state//此时的state就是todo:[...]数据
}))(TodoList);
