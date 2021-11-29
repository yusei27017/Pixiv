#  pixiv (非官方) python自動圖片下載 API

python + scrapy + splash + docker，可以透過 API 來完成自動下載。


## 使用說明
安裝 python 和 pip3(for debian, ubuntu)
```shell
sudo apt install python3
sudo apt install python3-pip
```
安裝 scrapy, requests, splash 
```shell
sudo pip3 install scrapy
sudo pip3 install requests
sudo pip3 install scrapy_splash
```
docker 官方安裝腳本
```shell
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
```

## 安裝完成後 docker pull splash 並啟動
```shell
sudo docker pull scrapinghub/splash
```
以及啟動splash
```shell
sudo docker run -itd -p 8050:8050 --rm scrapinghub/splash
```

## 開始scrapy
更改設定 php session id
cd 至 專案資料夾
```shell
scrapy crawl pixiv
```

## 聲明
 此代碼緊供技術交流研討之用途。若有不正確或可改善之處歡迎聯絡。

