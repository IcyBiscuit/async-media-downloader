# 基于异步框架的文件下载服务

基于`aiohttp`, `aiofiles`, `asyncio`, 开发的网络媒体文件爬取插件，可配合CoolQ机器人实现群推送

## 使用方法

请使用**Python3.5.3**及以上的版本

建议使用虚拟环境

Linux, macOS操作系统

进入项目根目录运行以下命令创建并激活虚拟环境，详细教程可查看[官方文档](https://docs.python.org/zh-cn/3.7/library/venv.html)

```bash
python3 -m venv ./
source bin/activate
```

Windows cmd

```cmd
c:\> python3 -m venv ./
c:\> \Scripts\activate.bat
```

Powershell

```powershell
PS C:\> python3 -m venv ./
PS C:\> \Scripts\Activate.ps1
```

创建完成后运行`pip install -r requirement.txt`安装项目依赖

Linux, macOS操作系统可以基于Gunicorn运行, 终端运行`startup.sh`即可， 默认监听本地`127.0.0.1`, `8422`端口。可自行修改`startup.sh`进行配置。

Windows操作系统需直接运行`app.py`文件

### 配置文件

配置文件位于`src/configs/appConfig.py`

配置项|配置内容|备注
:---:|---|---
`filePathPrefix`|下载文件路径前缀|建议使用绝对路径|
`logPath`|日志文件存放目录|
`fileDirs`|下载的文件分类子目录|一般无需修改

### API

以下均为表单请求

API路径|请求参数|参数值|返回响应
:---:|---|---|---
`/downloadImage`|url|图片文件的url|文件存放的绝对路径
`/downloadGif`|url|gif文件的url|同上
`/downloadAudio`|url|语音文件的url|同上

响应体示例，响应为JSON格式：

```json
{
    "path": "/path/to/your/file"
}
```

若发生错误，则响应返回错误信息：

```json
{
    "msg": "error message"
}
```