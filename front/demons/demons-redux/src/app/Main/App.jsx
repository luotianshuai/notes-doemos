import React, { Component } from "react";

import LocalTodo from "../Todo";
import {
    Redirect, Route, Switch, withRouter, NavLink
} from 'react-router-dom';

import { Layout, Menu, Icon } from "antd";
const { Header, Sider, Content } = Layout;

class App extends Component {
    state = {
        collapsed: false,
    };

    render() {
        return (
            <Layout>
                <Sider trigger={null} collapsible collapsed={this.state.collapsed}>
                    <div className="logo" />
                    <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
                        <Menu.Item key="1" title={'<NavLink to={"/local"}>测试</NavLink>'}>
                            <Icon type="ordered-list" />
                            <span>local-todo</span>
                        </Menu.Item>
                    </Menu>
                </Sider>
                <Layout css="min-height:100vh; background-color: #F5F6FA">
                    <Content>
                        <Switch>
                            <Route path={"/local"} component={LocalTodo} exact/>
                            <Redirect from="/" to="/local" />
                        </Switch>
                    </Content>
                </Layout>

            </Layout>
        );
    }
}


export default App;
