# ASHS Forum

這是高師大附中匿名板網頁原始碼，包括前端及後端。

## 先決條件

* 安裝`Docker`
* 向Google OAuth 2.0申請`Client ID`
* 按照`.env.example`的格式輸入環境變數並且改名為`.env`

## 使用說明

1. 啟動容器:

```bash
# 開發階段
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up 

# 生產階段
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up 
```

2. 首次使用請在資料庫建立新的資料表:

```bash
docker-compose exec backend bash

flask db migrate
flask db upgrade
```
