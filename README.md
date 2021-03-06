# 基于PaddleNLP的web端文本纠错系统

## 一.项目介绍：

  本次项目分享来源于最近参加的【飞桨校园AI Day】AI Workshop活动，团队名：SoPlaying，选择项目命题为“**文档纠错程序**”。其课题主要要求为：训练文档纠错数据集，并开发部署程序，实现上传word文件输出纠错结果。

  目前主要实现了基于PaddleNLP的文本纠错模型训练以及前后端分离式的web端部署，支持输入文本或上传word文档，显示纠错后文本结果与保存。技术栈：后端：PaddleNLP +FastAPI；前端：Vue+Element UI。

  通过本项目的学习你也将能够收获一套简易通用的模型web端部署方案，从而在后续完整项目开发或软件开发比赛中更加游刃有余。
  
  最后特别感谢课题导师坑姐（深渊上的坑）的创意课题提供与指导！

## 二.项目意义：

  中文文本纠错（CSC）任务是一项NLP基础任务，其输入是一个可能含有语法错误的中文句子，输出是一个正确的中文句子。其目的是提高语言正确性的同时有效减少人工校验成本。对于政务公文、新闻出版等行业来说文本纠错更是内容安全的首当其冲的一面，重要程度不言而喻。在通用领域中，中文文本纠错问题是从互联网起始时就一直在解决的问题。如何覆盖各种不同的错误类型，如何应对不同场景下的文本差异，对于文本纠错来说都是一项很有挑战性的工作。同时，文本纠错技术有着广泛的应用场景，值得我们长期投入时间和精力进行研究与打磨。

  在避免文本错误上，人工智能比人类更具优势，它能够记住大量的数据，且不会被糟心事影响情绪，不仅能基于客观现实执行任务，还能够比人类更好地评估和权衡相关因素，比人类更快、更准确地识别。基于深度学习方案搭建更精确的智能文本纠错模型，设计一款针对以中文为母语的用户所使用的优质“文本纠错”系统，自动对输入文本进行纠错，可以更好地让政府机构工作人员、媒体人、文字撰稿人、编辑、律师等职业从繁杂的文字“找茬”任务中脱离出来，有效降低内容风险。

## 三.总技术路线：

  1. 基于PaddleNLP的ERNIE模型在SIGHAN数据集完成中文文本纠错模型的训练。

  2. 基于FastAPI完成模型部署，开放为后端Restful API接口服务，并通过Postman对接口逻辑和功能进行测试。

  3. 基于Vue+ElementUI搭建高可扩展的文本纠错系统web界面，并通过网络请求对接后端API接口实现前后端联调。

![文本纠错技术路线](https://gitee.com/hchhtc123/picture/raw/master/typora/%E6%96%87%E6%9C%AC%E7%BA%A0%E9%94%99%E6%8A%80%E6%9C%AF%E8%B7%AF%E7%BA%BF.png)

## 四.项目演示：

**项目演示视频：** https://www.bilibili.com/video/BV1qF411L779/

**文本纠错演示：**

![文本纠错演示](https://gitee.com/hchhtc123/picture/raw/master/typora/%E6%96%87%E6%9C%AC%E7%BA%A0%E9%94%99%E6%BC%94%E7%A4%BA.png)

**文档纠错演示：**

![文档纠错演示](https://gitee.com/hchhtc123/picture/raw/master/typora/%E6%96%87%E6%A1%A3%E7%BA%A0%E9%94%99%E6%BC%94%E7%A4%BA.png)

## 五.项目结构说明：

  1. backend文件夹为后端API服务模块，其中best_model文件夹存放基于PaddleNLP训练好的文本纠错模型参数。main.py为后端API服务主程序。

  2. frontend文件夹为文本纠错系统web前端界面模块，/src/router/index.js定义界面路由；/src/views下存放搭建的新页面。

  3. 项目说明文档.txt：对整个项目环境配置进行了详细地介绍，项目必看！

## 六.学习资料：

  1. FastAPI官方文档：https://fastapi.tiangolo.com/zh/
  2. Postman使用教程：https://mp.weixin.qq.com/s/IoseF-2Ma8mH2gdQLn1rUA
  3. Vue官方文档：https://v3.cn.vuejs.org/
  4. ElementUI文档：https://v3.cn.vuejs.org/
  5. vue-admin-template：https://github.com/PanJiaChen/vue-admin-template

## 七.作者联系：

   项目运行过程中遇到问题欢迎向项目提issue也可以qq联系1075558916，注意提供完整报错信息和截图便于定位和解决问题！
