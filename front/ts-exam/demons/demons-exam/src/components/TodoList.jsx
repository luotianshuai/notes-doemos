import React, { Component } from "react";
import storage from "../module/storage"

class TodoList extends Component{
    constructor(props){
        super(props);
        this.state = {
            works: [
            ]
        };
        this.myInputRef = React.createRef();

    };

    // 监控用户添加Todo的input
    addWork = (event) => {
        if(event.keyCode === 13){
            let title = this.myInputRef.current.value;
            let tempWork = this.state.works;
            tempWork.push({title: title, checked: false});
            this.setState({works: tempWork});
            this.myInputRef.current.value = "";

            // 执行缓存数据,使用localStorage,需要注意的是:localStorage的值只能是字符串
            // localStorage.setItem("works",JSON.stringify(tempWork));
            // 使用自定义模块
            storage.set("works", tempWork)
        }
    };

    changeCheckBox = (key) => {
        let tempWork = this.state.works;
        tempWork[key].checked = !tempWork[key].checked;
        this.setState({works: tempWork});

        // 执行缓存数据,使用localStorage,需要注意的是:localStorage的值只能是字符串
        // localStorage.setItem("works",JSON.stringify(tempWork));
        // 使用自定义模块
        storage.set("works", tempWork)
    };

    delWork = (key) => {
        let tempWork = this.state.works;
        tempWork.splice(key,1);
        this.setState({works: tempWork});
        // 执行缓存数据,使用localStorage,需要注意的是:localStorage的值只能是字符串
        // localStorage.setItem("works",JSON.stringify(tempWork));
        // 使用自定义模块
        storage.set("works", tempWork)
    };

    componentDidMount() {
        // let historyWork = JSON.parse(localStorage.getItem("works"));
        // 使用自定义模块
        let historyWork = storage.get("works");
        if (historyWork){
            this.setState({works: historyWork})
        }
    };


    render() {
        return (
            <div>
                <div><h2>TodoList<input ref={this.myInputRef} onKeyUp={this.addWork}/></h2></div>
                <h2>代办事项</h2>
                <hr/>
                <ul>
                    {
                        this.state.works.map((value,key)=>{
                            if(!value.checked){
                                return <li key={key}>
                                    <input type="checkbox" checked={value.checked} onChange={this.changeCheckBox.bind(this,key)}/>{value.title} <button onClick={this.delWork.bind(this,key)}>删除</button>
                                </li>
                            }

                        })
                    }
                </ul>
                <hr/>
                <ul>
                    {
                        this.state.works.map((value,key)=>{
                            if(value.checked){
                                return <li key={key}>
                                    <input type="checkbox" checked={value.checked} onChange={this.changeCheckBox.bind(this,key)}/>{value.title} <button onClick={this.delWork.bind(this,key)}>删除</button>
                                </li>
                            }

                        })
                    }
                </ul>
            </div>
        );
    };
}

export default TodoList;
