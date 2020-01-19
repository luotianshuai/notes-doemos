import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

import Home from "./components/Home";
import News from "./components/News";
import TodoList from "./components/TodoList"
import Content from "./components/Content";
import Product from "./components/Product";
import ProductDetail from "./components/ProductDetail";

import appCss from "./assets/css/app.css"

class App extends Component {
    render() {
        return(
            <Router>
                <div>
                    <header className={appCss.headerStyle}>
                        <Link to="/">Home</Link>
                        <Link to="/todo">TodoList</Link>
                        <Link to="/news">News</Link>
                        <Link to="/product">Product</Link>
                    </header>
                    <hr/>

                    <Switch>
                        <Route exact path="/" component={Home} />
                        <Route path="/todo" component={TodoList} />
                        <Route path="/news" component={News} />
                        <Route path="/product" component={Product} />
                        <Route path="/content/:pid" component={Content} />
                        {/* get传值 路由不边不需要:xxx*/}
                        <Route path="/productDetail" component={ProductDetail} />
                    </Switch>
                </div>
            </Router>
        )
    }
}

export default App;
