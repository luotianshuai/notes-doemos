import React, { Component } from "react"
import styled, { css } from 'styled-components';
import {connect} from 'react-redux';

import {Button, Input} from "antd";



class TodoHeader extends Component {

    render() {
        return (
            <Box>
                <div style={{width: "500px", marginTop: "10px"}}><Input placeholder={"请输入代办事项"} style={{maxWidth: "300px"}}/> <Button type={"primary"}>新增</Button></div>
            </Box>
        );
    }
}


const Box = styled.div`
    display: flex;
    justify-content:center;
    align-items: center;
`;

export default TodoHeader;
