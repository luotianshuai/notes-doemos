import React, { Component } from "react"
import styled, { css } from 'styled-components';
import {connect} from 'react-redux';

import {Button, Input} from "antd";



class TodoFooter extends Component {

    render() {
        return (
            <Box>
                <div style={{width: "500px", marginTop: "10px"}}> </div>
            </Box>
        );
    }
}


const Box = styled.div`
    display: flex;
    justify-content:center;
    align-items: center;
`;

export default TodoFooter;
