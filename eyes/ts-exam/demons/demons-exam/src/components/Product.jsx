import React, { Component } from "react";
import {Link} from "react-router-dom";


class Product extends Component{
    constructor(props){
        super(props);

        this.state ={
            list: [
                {pid: 1, title: "我是商品1"},
                {pid: 2, title: "我是商品2"},
                {pid: 3, title: "我是商品3"},
                {pid: 4, title: "我是商品4"},
                {pid: 5, title: "我是商品5"},
                {pid: 6, title: "我是商品6"},
            ]
        };
    };

    render() {
        return(
            <div>
                <hr/>
                <h2>这是商品组件</h2>
                <ul>
                    {this.state.list.map((value,key) => {
                        return (
                            <li key={key}>
                                <Link to={`/productDetail/?pid=${value.pid}`} >{value.title}</Link>
                            </li>
                        )
                    })}
                </ul>
            </div>
        )
    }

}

export default Product;
