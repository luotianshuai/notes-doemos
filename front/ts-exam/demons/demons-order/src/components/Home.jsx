import React, { Component } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

import homeCss from "../assets/css/home.css";

class Home extends Component{
    constructor(props){
        super(props);
        this.state = {
            list: [],
            domain: "http://a.itying.com/"
        }
    }

    getData = () =>{
        let listUrl = "http://a.itying.com/api/productlist";
        axios.get(listUrl).then((response) => {
            this.setState({list: response.data.result})
        }).catch((error) => {
            console.log(error)
        });

    };


    componentDidMount() {
        this.getData();

    }

    render() {
        return(
            <div className={homeCss.home}>
                {this.state.list.map((value,key) => {
                    return(
                        <div key={key} className={homeCss.box}>
                            <div><h3>{value.title}</h3></div>
                            <ul >
                                {value.list.map((v,k) => {
                                    return(
                                        <li key={k} >
                                            <Link to={`/detail/${v._id}`}>
                                                <div>
                                                    <img src={`${this.state.domain}${v.img_url}`}/>
                                                    <p className={homeCss.desc}>{v.title}</p>
                                                    <p className={homeCss.price}>{v.price}元</p>
                                                </div>
                                            </Link>
                                        </li>
                                    )
                                })}
                            </ul>
                        </div>
                    )
                })}

            </div>
        )
    }
}

export default Home;
