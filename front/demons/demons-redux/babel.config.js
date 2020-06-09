const presets = [{
    "presets": [
        "@babel/env",
        "@babel/preset-react"
    ],
    "plugins": [
        // 按需加载antd配置
        ["import", {
            "libraryName": "antd",
            // "libraryDirectory": "es",
            "style": true, // `style: true` 会加载 less 文件
        }],
        "@babel/plugin-proposal-class-properties",
        "babel-plugin-styled-components",

    ]
}];

module.exports = {presets};
