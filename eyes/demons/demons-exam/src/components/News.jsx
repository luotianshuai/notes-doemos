import React, { Component } from "react";
import Content from "./Content";
import { Link } from "react-router-dom";



class News extends Component{
    constructor(props){
        super(props);

        this.state ={
            list: [
                {pid: 1, title: "新闻详情1"},
                {pid: 2, title: "新闻详情2"},
                {pid: 3, title: "新闻详情3"},
                {pid: 4, title: "新闻详情4"},
                {pid: 5, title: "新闻详情5"},
                {pid: 6, title: "新闻详情6"},
            ]
        };
    };

    render() {
        return(
            <div>
                <hr/>
                <h2>这是新闻组件</h2>

                <ul>
                    {this.state.list.map((value,key) => {
                        return (
                            <li key={key}>
                                <Link to={`/content/${value.pid}`} >{value.title}</Link>
                            </li>
                        )
                    })}
                </ul>
            </div>
        )
    }

}

export default News;
