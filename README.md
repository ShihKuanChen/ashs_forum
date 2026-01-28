# Ashs Forum

這是高師大附中匿名板網頁原始碼，包括前端及後端。

## 使用說明

1. 請先安裝Docker
2. 啟動容器:

```bash
# 開發階段
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up 

# 生產階段
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up 
```

3. 首次使用請初始化資料庫:

```bash
docker-compose exec backend bash

flask db migrate
flask db upgrade
```
