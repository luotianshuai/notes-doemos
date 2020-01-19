import React, { Component } from "react";
import axios from "axios";
import detailCss from "../assets/css/detail.css"

import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

class Detail extends Component{
    constructor(props){
        super(props);
        this.state = {
            detail: {},
            domain: "http://a.itying.com/"
        }
    }

    getData = (pid) =>{
        let listUrl = `${this.state.domain}api/productcontent?id=${pid}`;
        axios.get(listUrl).then((response) => {
            this.setState({detail: response.data.result[0]});
            // console.log("请求数据结果:",response.data.result[0].title)
        }).catch((error) => {
            console.log(error)
        });

    };


    componentDidMount() {
        // console.log("详情页父组件props信息:",this.props);
        let pid = this.props.match.params.pid;
        this.getData(pid)
    }


    render() {
        return(
            <div className={detailCss.detail}>
                <div className={detailCss.back}><Link to='/'>返回</Link></div>
                <div className={detailCss.box}>
                    <div className={detailCss.pic}>
                        <img src={`${this.state.domain}${this.state.detail.img_url}`} alt={this.state.detail.title}/>
                    </div>
                    <h2 className={detailCss.title}>{this.state.detail.title}</h2>
                    <div className={detailCss.content}>
                        {this.state.detail.content}
                    </div>
                </div>
            </div>
        )
    }
}

export default Detail;
