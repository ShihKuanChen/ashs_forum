# Ashs Forum

這是高師大附中匿名板網頁原始碼，包括前端及後端。

## 使用說明

1. 請先安裝Docker
2. 根據需要在目錄執行

```bash
# 開發階段
docker-compose up -f docker-compose.yml -f docker-compose.dev.yml

# 生產階段
docker-compose up -f docker-compose.yml -f docker-compose.prod.yml
```

3. 首次使用請使用`docker-compose exec backend bash`並在其分別輸入`flask db migrate`及`flask db upgrade`來初始化資料庫