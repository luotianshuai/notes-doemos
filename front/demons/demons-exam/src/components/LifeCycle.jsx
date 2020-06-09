import React, { Component } from "react";
import axios from "axios";

class LifeCycle extends Component {
    constructor(props){
        super(props);
        this.state = {
            msg: "默认值"
        };

        console.log("挂载时:01 构造函数")
    };

    static getDerivedStateFromProps(props, state) {
        console.log("挂载时:02 组件将要挂载");
        // 必须要有返回值 [返回一个state对象, 或者null表示状态不变]
        return null
    }

    componentDidMount() {
        console.log("挂在时:04 组件挂载")
    }

    // 数据更新-1 声明周期函数是否更新
    shouldComponentUpdate(nextProps, nextState, nextContext) {
        // 如果返回false 表示不更新
        return true
    }

    // 数据卸载-1
    componentWillUnmount() {
        console.log("LifeCycle要被卸载了....")
    }


    updateMsg = () => {
        this.setState({msg:"LifeCycle点击按钮后更改的数据"})
    };

    render() {
        console.log("挂载时:03 组件渲染");
        return(
            <div style={{background: "#BBFFFF"}}>
                <h2>LifeCycle组件</h2>
                <h3>HomeMsg数据:{this.props.msg}</h3>
                <h3>LifeCycleMsg数据:{this.state.msg}</h3>
                <br/>
                <button onClick={this.updateMsg}>点击更新msg数据</button>
                <hr/>
            </div>
        )
    }
}

export default LifeCycle;
