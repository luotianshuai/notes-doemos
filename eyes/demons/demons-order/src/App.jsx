import React, { Component } from "react";
import { BrowserRouter as Router, Route, Link, Switch } from "react-router-dom";

// Component
import Home from "./components/Home";
import Detail from "./components/Detail";


class App extends Component {
    render() {
        return(
            <Router>
                <div>
                    {/*<h2>无人点餐demons</h2>*/}
                    {/*<header>*/}
                    {/*    <Link to="/">Home</Link>*/}
                    {/*    <Link to="/detail">Detail</Link>*/}
                    {/*</header>*/}
                    {/*<hr/>*/}

                    {/*路由部分会被替换*/}

                    <Switch>
                        <Route exact path="/" component={Home} />
                        <Route path="/detail/:pid" component={Detail} />
                    </Switch>
                </div>
            </Router>
        )
    }
}

export default App;
