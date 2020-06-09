// react是它的核心组件
// react 这个react的核心js库,在最早的时候react和react-dom是在一起的
// 从根本上说React的概念和浏览器无关,react核心包里只包含了渲染组件创建组件等众多目标之一,目的是为了不同平台公共的核心组件例如React Native
import React from "react";
// react-dom是操作dom相关的功能
// react-dome它的作用是react和dom之间的粘合剂,提供了特定dom方法,通常我们只是用ReactDOM.render,渲染一个react元素成为dom
import ReactDOM from "react-dom";

import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
