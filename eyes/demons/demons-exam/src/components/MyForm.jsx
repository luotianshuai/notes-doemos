import React, { Component } from "react";

class MyForm extends Component {

    constructor(props){
        super(props);
        this.state = {
            msg: "React其他表单",
            name: "",
            sex: "1",
            info: "",
            city: "",
            cityList: ["北京", "上海", "广州"],
            hobby: [{title: "吃饭", checked: true}, {title: "睡觉", checked: false}, {title: "打豆豆", checked: true}]
        };
    };

    handelName = (event) => {
        this.setState({name: event.target.value})
    };

    // radio 单个值
    handelSex = (event) => {
        this.setState({sex: event.target.value});
    };

    // select 单个值
    handelCity = (event) => {
        this.setState({city: event.target.value})
    };

    // checkbox 多个值
    handelHobby = (key) => {
        console.log("key:", key);

        let changeHobby = this.state.hobby;
        changeHobby[key].checked = !changeHobby[key].checked;

        this.setState({hobby: changeHobby})
    };

    // textarea 单个值
    handelInfo = (event) => {
        this.setState({info: event.target.value})
    };

    handelSubmit = (event) => {
        // 组织submit提交事件
        event.preventDefault();
        console.log("name:", this.state.name, "\n");
        console.log("sex:", this.state.sex, "\n");
        console.log("city:", this.state.city, "\n");
        console.log("hobby", this.state.hobby, "\n");
        console.log("info", this.state.info, "\n");
    };

    render() {
        return(
            <div>
                <h2>React 其他表单</h2>
                <form onSubmit={this.handelSubmit}>
                    {/*默认的input*/}
                    Name:<input type="text" value={this.state.name} onChange={this.handelName}/><br/>
                    {/*radio*/}
                    Sex:
                        男:<input type="radio" value="1" checked={this.state.sex === "1"} onChange={this.handelSex}/>
                        女:<input type="radio" value="2" checked={this.state.sex === "2"} onChange={this.handelSex}/><br/>
                    {/*select*/}
                    <select value={this.state.city} onChange={this.handelCity} multiple={false}>
                        {this.state.cityList.map((value,key)=>{
                            return <option key={key}>{value}</option>
                        })}
                    </select>
                    <br/>
                    爱好:
                    {this.state.hobby.map((value,key)=>{
                        return <span key={key}>
                            {value.title} <input type="checkbox" checked={value.checked} onChange={this.handelHobby.bind(this,key)}/>
                        </span>
                    })}<br/>

                    <textarea value={this.state.info} onChange={this.handelInfo}/><br/>
                    <input type="submit" defaultValue="提交"/>
                </form>
            </div>
        )
    };
}

export default MyForm;
