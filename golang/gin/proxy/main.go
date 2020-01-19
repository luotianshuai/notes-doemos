package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"net/http/httputil"
	"net/url"
)

func main() {
	router := gin.Default()

	// LoggerWithFormatter 中间件会将日志写入 gin.DefaultWriter
	// By default gin.DefaultWriter = os.Stdout
	router.Use(gin.LoggerWithFormatter(func(param gin.LogFormatterParams) string {

		// 你的自定义格式
		return fmt.Sprintf("[Sogou-Observer,clientip=%s,time:[%s],method=%s,path=%s,protocol=%s,status=%d,cost=%d,agent=\"%s\",error=\"%s\",Owner=OP]\n",
			param.ClientIP,
			param.TimeStamp.Format("2006-01-02 15:04:05"),
			param.Method,
			param.Path,
			param.Request.Proto,
			param.StatusCode,
			param.Latency.Nanoseconds() / 1000000,
			param.Request.UserAgent(),
			param.ErrorMessage,
		)
	}))
	router.Use(gin.Recovery())

	// http://localhost:8081/education/_search to http://localhost:80/
	router.GET("/education/_search", ReverseProxy("http://127.0.0.1:80/"))
	router.Run(":8081") // listen and serve on 0.0.0.0:80
}

func ReverseProxy(target string) gin.HandlerFunc {
	destUrl, _ := url.Parse(target)
	proxy := httputil.NewSingleHostReverseProxy(destUrl)
	return func(c *gin.Context) {
		proxy.ServeHTTP(c.Writer, c.Request)
	}
}

