import React, { Component } from "react"
import {connect} from 'react-redux';
import headerCss from "../../assets/css/header.css"

class TodoHeader extends Component {
    //取得未完成的todo数量
    getUnfinishedCount = () => {
        //this.props.todo就是从connect传入的state数据
        return this.props.todo.filter((i) => {
            return i.isComplete === false;
        }).length;
    };

    render() {
        return (
            <div className={headerCss.header}>
                <div><h2>您有{this.getUnfinishedCount()}件事未完成</h2></div>
            </div>
        );
    }
}

//导出注入后的组件
export default connect((state) => ({
    ...state//此时的state就是todo:[...]数据
}))(TodoHeader);
