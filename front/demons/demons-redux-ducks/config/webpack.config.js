const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {


    // webpack的入口文件 = 从哪里开始解析
    entry: path.resolve(__dirname, "../src/app/Main/index.jsx"),
    output: {
        // 打包后文件存放的目录
        path: path.resolve(__dirname, "../build"),
        // 打包后的文件名,动态发版
        filename: '[name].[hash].js',
        chunkFilename: '[name].[chunkhash].js',
        publicPath: '/'
    },
    // DevServer配置
    devtool: 'source-map',
    devServer: {
        hot: true,
        compress: true,
        port: 9000,
        open: true,
        historyApiFallback: true,
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                use: {loader: "babel-loader"},
                // 直接解释就是，数组内填入什么后缀，引入该后缀时可以文件名可以不带后缀
                resolve: {
                    extensions: [".js", ".jsx"]
                },
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

            },
            {
                test: /\.(png|jpg|gif)$/,
                use: [{
                    loader: 'url-loader',
                    options: {
                        limit: 8192
                    }
                }]
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
