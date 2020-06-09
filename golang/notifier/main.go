package main

import "context"

func main() {

}

// 定义报警接口
type Notifier interface {
	// 定义初始化报警方法
	NewAlert(ctx context.Context) (*models.Alert, error)
	SetAlert(ctx context.Context, alert *models.Alert) error
	UpdateAlertItems(ctx context.Context) error
	UpdateUserAlert(ctx context.Context) error
	InsertNotice(ctx context.Context) error
}
