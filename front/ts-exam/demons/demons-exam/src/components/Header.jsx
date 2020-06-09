import React, { Component } from "react";
import PropTypes from "prop-types";
import HeaderCss from "../assets/css/header.css";

class Header extends Component{

    // static defaultProps = {
    //     title: '我是默认的父组件传递的:title',
    // };
    //
    // static propTypes = {
    //     name: PropTypes.string.isRequired,
    // };

    constructor(props){
        super(props);
        this.state = {
            title: "Header组件"
        }
    };

    render(){
        return(
            <div className={HeaderCss.eleHeader}>

            </div>
        )
    }
}


export default Header;
