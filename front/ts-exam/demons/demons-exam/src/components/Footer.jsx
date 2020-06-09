import React, { Component } from "react";

class Footer extends Component{
    constructor(props){
        super(props);
        this.state = {
            title: "我是底部组件的title"
        };
    }

    run = () => {
        alert("我是底部组件的方法")
    };

    render(){
        return(
            <div>
                <h2>这是底部组件</h2>
            </div>
        )
    }
}

export default Footer;
