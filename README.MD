# 基于 PaddleOCR 的 pdf 识别

## 思路

1. pdf 转图片，删除图像元素来减少干扰
2. 裁剪图片加速识别
3. OCR 识别

## 环境配置

```shell
python -m pip uninstall pymupdf
python -m pip uninstall fitz
python -m pip install pymupdf -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

M1 芯片需要安装（问题依然很多）：

```shell
brew install mupdf swig freetype
python -m pip uninstall pymupdf
python -m pip uninstall fitz
python -m pip install https://github.com/pymupdf/PyMuPDF/archive/master.tar.gz
```

## 使用方法

```shell
paddleocr --image_dir ./ocr-server/2RKAR0收据0-2.jpeg --use_angle_cls false --use_gpu false --lang en --det false
```
