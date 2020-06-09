import React, { Component } from "react";

class Content extends Component {
    constructor(props){
        super(props);
        this.state = {}
    }

    componentDidMount() {
        // 输出下props.match.params获取传值
        console.log("Content输出:",this.props.match.params)
    }

    render() {
        return(
            <div>
                <h2>这是Content组件</h2>
            </div>
        )
    }
}

export default Content;
