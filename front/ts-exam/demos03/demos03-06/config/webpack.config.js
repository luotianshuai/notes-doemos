const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
    // webpack的入口文件 = 从哪里开始解析
    entry: path.resolve(__dirname, "../src/index.js"),
    output: {
        // 打包后文件存放的目录
        path: path.resolve(__dirname, "../build"),
        // 打包后的文件名,动态发版
        filename: '[name].[hash].js',
        chunkFilename: '[name].[chunkhash].js'
    },
    // DevServer配置
    devServer: {
        compress: true,
        port: 9000,
        open: true,
    },
    module: {
        rules: [
            {
                test: /(\.jsx|\.js)$/,
                use: {loader: "babel-loader"},
                exclude: "/node_module/"
            },
            {
                test: /\.css$/,
                // loader 的加载顺序是从右往左
                use: [{
                    loader: "style-loader"
                }, {
                    loader: "css-loader",
                    options: {
                        modules: {
                            localIdentName: "[name]__[local]___[hash:base64:5]",
                        }
                    }
                }],

            }
        ]
    },
    plugins: [
        new HtmlWebpackPlugin({
            filename: 'index.html',
            template: path.join(__dirname, '../public/index.html')
        })
    ],
};
