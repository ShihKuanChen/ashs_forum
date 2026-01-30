# ASHS Forum

這是高師大附中匿名板網頁原始碼，包括前端及後端。

## 先決條件

* 安裝`Docker`
* 向Google OAuth 2.0申請`Client ID`
* 按照`.env.example`的格式輸入環境變數並且改名為`.env`

## 快速啟動

1. 啟動容器:

```bash
# 開發階段
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up 

# 生產階段
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up 
```

2. 首次使用請在資料庫建立新的資料表:

```bash
# 先將.env的SUPER_MODE=true

docker-compose exec backend bash -c "flask db upgrade"

# 將.env的SUPER_MODE=false並重啟容器
```

## 技術

本專案使用Vue.js作為前端框架，後端使用Python Flask，使用Nginx作為前端伺服器以及後端反向代理，並使用Flask Migrate管理資料庫，資料庫使用PostgreSQL儲存網站資料並且使用Redis管理登入狀態。
