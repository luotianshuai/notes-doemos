const path = require('path');

module.exports = {
    // webpack的入口文件 = 从哪里开始解析
    entry: path.resolve(__dirname, "../src/index.js"),
    output: {
        // 打包后文件存放的目录
        path: path.resolve(__dirname, "../build"),
        // 打包后的文件名
        filename: "index.js"
    },
    // DevServer配置
    devServer: {
        contentBase: path.resolve(__dirname, "../build"),
        compress: true,
        port: 9000,
        open: true,
    },
    module: {
        rules: [
            {
                // 匹配需要翻译的文件
                test: /\.(png|jpe?g|gif|svg)(\?.*)?$/,
                // 使用哪个loader去翻译
                loader: 'file-loader'
            }
        ]
    }
};
