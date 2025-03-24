# 鹿关神器：本子下载 API / Fast Jerker

刚朋友给我转了个仓库，也是把本子下载下来转换成 pdf 的，不得不说写得有点乱，我从头写了一份。花了半小时。

哦先介绍下我自己，首先**我爱鹿关**，然后我在伦敦上学，目前在从事后端开发的实习，比较喜欢后端和基础架构。

反正外国人看不懂中文，这个仓库里我可以放飞自我了，我们**鹿关**玩家就是这样！

# Config

安装依赖

    git clone {this_repo}

    pip install -r requirements.txt

记得去**config/jm_config.yml**里改 dir，不同系统不一样

# Usage

建议你 clone 下来以后自己跑 localhost，如果你有相关的服务需要下载本子，直接访问 api 就行。只需在请求里包含神秘代码就行，例如/get/114514

    fastapi run src/main.py

我自己用 ngork 暴露了我的端口，https://dickman.ngrok.app/get/114514， 所以你们也可以使用这个我部署的 api，但我一关电脑就会挂就是了。

# Process

基于 JM 的 sdk 下载本子，然后转化成 PDF，再由 FastAPI 推送。

## API document

目前只有一个 API, GET 方法。{folder_name}改成神秘代码。

    /get/{folder_name}

## Future development

- 分离代码
- 丰富下错误处理
- 接个数据库，存 KV（神秘代号-PDF 路径），处理请求的时候先看数据库里有没有。
- 添加更多 API，契合客户端需求。我知道有人会拿去做群聊机器人之类的。
