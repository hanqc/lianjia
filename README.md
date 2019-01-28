# 基于Scrapy框架的爬虫，爬取链家网西安市房源信息，并用高德api在地图上可视化显示

- 支持python3

- 工程里面已经有爬取后的rent.csv文件，可以删除，然后执行命令scrapy crawl fangjia -o rent.csv -t csv生成csv文件

- 爬取完成后，执行命令python -m http.server 9090,然后打开http://localhost:9090/,点击打开demo.html，导入上面生成的rent.csv文件即可。

#### 这个项目有很多可以改进的部分，比如房源信息的选取过于简单，房间的面积也应该纳入考虑。比如可以做成在地图上显示具体的房源信息，每个标记都只标记唯一的房源。比如房源信息为什么要存文件呢，也可以存数据库里。(可改为使用mongoDB)
