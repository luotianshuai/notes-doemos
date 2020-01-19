import React, { Component } from "react";
import axios from "axios";
import fetchJsonp from "fetch-jsonp"

class Ashow extends Component{
    constructor(props){
        super(props);
        this.state = {}
    }


    getData = () => {
        // axios不支持跨域所以我们后台接口要设置允许跨域
        // 域名/端口/协议不同就跨域
        const url = "http://127.0.0.1:8080/show";
        axios.get(url).then((response) =>{
            console.log("url show response:",response);
            this.setState({msg: response.data.msg})
        }).catch((error) => {
            console.log("url show error:",error)
        })
    };

    getDataP = () => {
        const url = "http://127.0.0.1:8080/shows";
        fetchJsonp(url).then(function(response) {
            return response.json()
        }).then((json) => {
            console.log('parsed json', json);
            this.setState({msg2: json.msg})
        }).catch((error) => {
            console.log('parsing failed', error)
        })
    };
    

    render(){
        return(
            <div>
                <h2>获取数据组件</h2>
                <h3>获取的数据是:{this.state.msg}</h3>
                <button onClick={this.getData}>获取数据</button>
                <hr/>
                <h2>jsonp获取数据组件</h2>
                <h3>jsonp获取的数据是:{this.state.msg2}</h3>
                <button onClick={this.getDataP}>获取数据jsonp</button>
            </div>
        )
    }
}

export default Ashow;
