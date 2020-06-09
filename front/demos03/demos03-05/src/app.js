import React, { Component } from "react";
import styles from "./css/main.css"
import dogImage from "./image/dog.jpg"
class App extends Component {

    render() {
        return (
            <div >
                <div className={styles.h1_bk}><h1>Hello World</h1></div>
                <div> <img src={dogImage}/></div>
            </div>

        )
    }
}

export default App;
