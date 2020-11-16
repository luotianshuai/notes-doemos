package main

import (
	"fmt"

	"github.com/go-redis/redis"
)

func main() {
	redisdb := redis.NewClient(&redis.Options{
		Addr:     "192.168.1.110:6379",
		Password: "",
		DB:       0,
	})

	pong, err := redisdb.Ping().Result()
	if err != nil {
		fmt.Printf("can not connection redis.....")
		panic(err)
	}

	fmt.Print(pong)

}
