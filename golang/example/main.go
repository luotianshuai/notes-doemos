package main

import (
	"os"

	"github.com/gin-gonic/gin"
)

// 初始化路由
var (
	engine = gin.Default()
)

func main() {
	// 允许使用跨域请求  全局中间件
	engine.Use(Cors())

	engine.GET("/show", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"msg": "Gin后端接口数据",
		})
	})

	engine.GET("/shows", func(c *gin.Context) {
		c.JSONP(200, gin.H{
			"msg": "Gin后端接口数据-JSONP",
		})
	})

	// 启动路由 设定端口
	runErr := engine.Run(":8080")
	if runErr != nil {
		os.Exit(1)
	}

}

// Cors 跨域中间件
func Cors() gin.HandlerFunc {
	// TODO 优化Gin跨域中间件
	return func(c *gin.Context) {
		//method := c.Request.Method
		c.Header("Access-Control-Allow-Origin", "*")
		c.Header("Access-Control-Allow-Headers", "Content-Type,AccessToken,X-CSRF-Token, Authorization, Token")
		c.Header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
		c.Header("Access-Control-Expose-Headers", "Content-Length, Access-Control-Allow-Origin, Access-Control-Allow-Headers, Content-Type")
		c.Header("Access-Control-Allow-Credentials", "true")
		//放行所有OPTIONS方法
		//if method == "Get" {
		//	c.AbortWithStatus(http.StatusNoContent)
		//}
		// 处理请求
		c.Next()
	}
}
