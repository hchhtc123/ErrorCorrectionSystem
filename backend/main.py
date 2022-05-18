"""
    基于FastAPI的后端文本纠错API接口服务
    先加载文本纠错模型预热再启动后端接口服务
"""

from fastapi import FastAPI, HTTPException, File, UploadFile
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from paddlenlp.transformers import ErnieTokenizer
from paddlenlp.data import Vocab
from predict import Predictor
from sutil import cut_sent
import uvicorn

# 加载训练好的文本纠错模型去完成纠错任务
tokenizer = ErnieTokenizer.from_pretrained("ernie-1.0")
pinyin_vocab = Vocab.load_vocabulary("./best_model/pinyin_vocab.txt", unk_token='[UNK]', pad_token='[PAD]')
# 配置加载模型参数地址
predictor = Predictor('./best_model/static_graph_params.pdmodel', './best_model/static_graph_params.pdiparams', 
                          'cpu', 128, tokenizer, pinyin_vocab)

# 文本纠错预热：因为第一次预测需加载模型耗时较久故启动时先预热下
# 要进行纠错的文本demo
samples = [
    '遇到逆竟时，我们必须勇于面对，而且要愈挫愈勇，这样我们才能朝著成功之路前进。',
    '人生就是如此，经过磨练才能让自己更加拙壮，才能使自己更加乐观。',
]

print("文本纠错模型加载预热！")
# 文本纠错
results = predictor.predict(samples, batch_size=2)
# 输出纠错结果
for source, target in zip(samples, results):
    print("要纠错的文本为:", source)
    print("纠错后的文本为:", target)

# 创建一个 FastAPI「实例」，名字为app
app = FastAPI()

# 设置允许跨域请求，解决跨域问题
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 定义请求体数据类型：text
class Document(BaseModel):
    text: str

# 定义路径操作装饰器：POST方法 + API接口路径
@app.post("/v1/errorCorrect/", status_code=200)
# 定义路径操作函数，当接口被访问将调用该函数
async def ErrorCorrection(document: Document):
    try:
        # 获取要进行纠错的文本内容
        text = document.text
        # 精细分句处理以更好处理长文本
        data = cut_sent(text)
        result = predictor.predict(data, batch_size=2)
        # 拼接分句后结果
        correctionResult = ''
        for temp in result:
            if temp is not '':
                correctionResult += temp;
                correctionResult += '\n';
        # correctionResult = "\n".join(result)
        # 接口结果返回
        results = {"message": "success", "originalText": document.text, "correctionResults": correctionResult}
        return results
    # 异常捕获
    except Exception as e:
        print("异常信息：", e)
        raise HTTPException(status_code=500, detail="请求失败，服务器端异常！")

# 启动创建的实例app，设置启动ip和端口号
uvicorn.run(app, host="127.0.0.1", port=8000)
