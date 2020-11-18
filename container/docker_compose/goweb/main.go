package main

import (
	"context"
	"fmt"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis/v8"
)

// 声明一个全局变量，这样别的地方也可是使用
var redisClient *redis.Client

func init() {
	initRedisClient()
}

func main() {
	web := gin.Default()

	web.GET("/", func(c *gin.Context) {
		accessNum := incrValue()
		megValue := fmt.Sprintf("access numbser is :%d", accessNum)
		c.JSON(200, gin.H{"msg": megValue})
	})

	web.Run()

}

// 初始化Redis链接
func initRedisClient() error {
	redisClient = redis.NewClient(&redis.Options{
		Addr:     "redis:6379",
		Password: "",
		DB:       0,
	})

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	_, err := redisClient.Ping(ctx).Result()
	return err

}

// 递增返回
func incrValue() int64 {
	ctx := context.Background()
	hits := redisClient.Incr(ctx, "hits")
	return hits.Val()
}
