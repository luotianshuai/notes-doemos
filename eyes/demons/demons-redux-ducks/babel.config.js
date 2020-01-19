const presets = [{
    "presets": [
        "@babel/env",
        "@babel/preset-react"
    ],
    "plugins": [
        "@babel/plugin-proposal-class-properties",
        // 按需加载antd配置
        ["import", {
            "libraryName": "antd",
            "libraryDirectory": "es",
            "style": "css" // `style: true` 会加载 less 文件
        }]
    ]
}];

module.exports = {presets};
