import React, { Component } from "react";
import LifeCycle from "./LifeCycle"

class Home extends Component{
    constructor(props){
        super(props);
        this.state = {
            msg: "Home组件传递给LifeCycle的默认消息",
            lifeCycleFlag: true
        };
    };

    updateMsg = () => {
        this.setState({msg: "Home 点击修改按钮后的值"})
    };

    flagLifeCycle = () => {
        this.setState({lifeCycleFlag: !this.state.lifeCycleFlag})
    };

    render() {
        return (

            <div style={{background: "#FFF68F"}}>
                <h2>这是首页组件</h2>
                <button onClick={this.updateMsg}>点击修改父组件的msg,触发子组件的update看下流程</button>
                <br/>
                <button onClick={this.flagLifeCycle}>挂载和写在LifeCycle组件</button>
                <hr/>
                {this.state.lifeCycleFlag ? <LifeCycle msg={this.state.msg} />:""}
                <hr/>
            </div>
        );
    }
}

export default Home;
