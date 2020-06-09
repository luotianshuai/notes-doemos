import React, { Component } from "react";
import Url from "url";

class ProductDetail extends Component {
    constructor(props){
        super(props);
        this.state = {}
    }

    componentDidMount() {
        // get传值在props.location.search里能获取到
        // 这里获取的字符串: ?pid=1
        // 下面举个例子通过一个模块去解析它或者自己写一个
        console.log("Get传值输出:",this.props.location.search);
        // 解析后的url参数
        let queryRet = Url.parse(this.props.location.search,true);
        console.log("Get传值输出:",queryRet)
    }

    render() {
        return(
            <div>
                <h2>这里是商品详情页</h2>
            </div>
        )
    }
}

export default ProductDetail;
