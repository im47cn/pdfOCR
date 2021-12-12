# -*- coding: utf-8 -*-
import os
import fitz
import time
from paddleocr import PaddleOCR, draw_ocr


def pdf2png_tbo(pdfPath, imgPath, zoom_x=2, zoom_y=2, rotation_angle=0):
    '''
    # 将PDF转化为图片
    pdfPath pdf文件的路径
    imgPath 图像要保存的文件夹
    zoom_x x方向的缩放系数
    zoom_y y方向的缩放系数
    rotation_angle 旋转角度
    '''

    time_start = time.time()

    # 打开PDF文件
    pdf = fitz.open(pdfPath)

    files = []

    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]

        # 删除图片
        img_list = page.get_images()
        for img in img_list:
            pdf._deleteObject(img[0])
        
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y)
        # pm = page.get_pixmap(matrix=trans, alpha=False)
        # if pm.width > 2000 or pm.height > 2000:
        #     pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)         
        # pm.save(imgPath + str(pg) + ".jpeg")

        # tbo No.
        clip1 = fitz.Rect(515, 86, 558, 100)
        pm1 = page.get_pixmap(matrix=trans, clip=clip1, alpha=False)
        file1 = imgPath + str(pg) + "-1.jpeg"
        files.append(file1)
        pm1.save(file1)

        # tbo Issues by
        clip2 = fitz.Rect(380, 105, 558, 119)
        # clip2 = fitz.Rect(37, 256, 280, 269)
        pm2 = page.get_pixmap(matrix=trans, clip=clip2, alpha=False)
        file2 = imgPath + str(pg) + "-2.jpeg"
        files.append(file2)
        pm2.save(file2)

        # tbo payment
        clip3 = fitz.Rect(450, 255, 558, 285)
        pm3 = page.get_pixmap(matrix=trans, clip=clip3, alpha=False)
        file3 = imgPath + str(pg) + "-3.jpeg"
        files.append(file3)
        pm3.save(file3)
    
    pdf.close()
    time_end = time.time()
    time_cost = time_end - time_start
    print('totally cost: {}, page: {}, each page cost: {}'.format(
        time_cost, pg + 1, time_cost / (pg + 1)))
    return files

def pdf2png_exp(pdfPath, imgPath, zoom_x=2, zoom_y=2, rotation_angle=0):
    '''
    # 将PDF转化为图片
    pdfPath pdf文件的路径
    imgPath 图像要保存的文件夹
    zoom_x x方向的缩放系数
    zoom_y y方向的缩放系数
    rotation_angle 旋转角度
    '''

    time_start = time.time()

    # 打开PDF文件
    pdf = fitz.open(pdfPath)

    files = []

    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]

        # 删除图片
        img_list = page.get_images()
        for img in img_list:
            pdf._deleteObject(img[0])
        
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y)
        # pm = page.get_pixmap(matrix=trans, alpha=False)
        # if pm.width > 2000 or pm.height > 2000:
        #     pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)         
        # pm.save(imgPath + str(pg) + ".jpeg")

        # exp No.
        clip1 = fitz.Rect(160, 180, 440, 205)
        pm1 = page.get_pixmap(matrix=trans, clip=clip1, alpha=False)
        file1 = imgPath + str(pg) + "-1.jpeg"
        files.append(file1)
        pm1.save(file1)

        # exp payment
        clip2 = fitz.Rect(460, 440, 535, 465)
        pm2 = page.get_pixmap(matrix=trans, clip=clip2, alpha=False)
        file2 = imgPath + str(pg) + "-2.jpeg"
        files.append(file2)
        pm2.save(file2)
    
    pdf.close()
    time_end = time.time()
    time_cost = time_end - time_start
    print('totally cost: {}, page: {}, each page cost: {}'.format(
        time_cost, pg + 1, time_cost / (pg + 1)))
    return files

def pdf2png_agoda(pdfPath, imgPath, zoom_x=2, zoom_y=2, rotation_angle=0):
    '''
    # 将PDF转化为图片
    pdfPath pdf文件的路径
    imgPath 图像要保存的文件夹
    zoom_x x方向的缩放系数
    zoom_y y方向的缩放系数
    rotation_angle 旋转角度
    '''

    time_start = time.time()

    # 打开PDF文件
    pdf = fitz.open(pdfPath)

    files = []

    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]

        # 删除图片
        img_list = page.get_images()
        for img in img_list:
            pdf._deleteObject(img[0])
        
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        if pm.width > 2000 or pm.height > 2000:
            pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)         
        pm.save(imgPath + str(pg) + ".jpeg")

        # agoda No.
        clip1 = fitz.Rect(160, 180, 440, 205)
        pm1 = page.get_pixmap(matrix=trans, clip=clip1, alpha=False)
        file1 = imgPath + str(pg) + "-1.jpeg"
        files.append(file1)
        pm1.save(file1)

        # agoda payment
        clip2 = fitz.Rect(460, 440, 535, 465)
        pm2 = page.get_pixmap(matrix=trans, clip=clip2, alpha=False)
        file2 = imgPath + str(pg) + "-2.jpeg"
        files.append(file2)
        pm2.save(file2)
    
    pdf.close()
    time_end = time.time()
    time_cost = time_end - time_start
    print('totally cost: {}, page: {}, each page cost: {}'.format(
        time_cost, pg + 1, time_cost / (pg + 1)))
    return files

def pdf2png_agoda2(pdfPath, imgPath, zoom_x=2, zoom_y=2, rotation_angle=0):
    '''
    # 将PDF转化为图片
    pdfPath pdf文件的路径
    imgPath 图像要保存的文件夹
    zoom_x x方向的缩放系数
    zoom_y y方向的缩放系数
    rotation_angle 旋转角度
    '''

    time_start = time.time()

    # 打开PDF文件
    pdf = fitz.open(pdfPath)

    files = []

    # 逐页读取PDF
    for pg in range(0, pdf.pageCount):
        page = pdf[pg]

        # 删除图片
        img_list = page.get_images()
        for img in img_list:
            pdf._deleteObject(img[0])
        
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y)
        # pm = page.get_pixmap(matrix=trans, alpha=False)
        # if pm.width > 2000 or pm.height > 2000:
        #     pm = page.get_pixmap(matrix=fitz.Matrix(1, 1), alpha=False)         
        # pm.save(imgPath + str(pg) + ".jpeg")

        # agoda No.
        clip1 = fitz.Rect(140, 95, 200, 110)
        pm1 = page.get_pixmap(matrix=trans, clip=clip1, alpha=False)
        file1 = imgPath + str(pg) + "-1.jpeg"
        files.append(file1)
        pm1.save(file1)

        # agoda payment
        clip2 = fitz.Rect(205, 436, 290, 446)
        pm2 = page.get_pixmap(matrix=trans, clip=clip2, alpha=False)
        file2 = imgPath + str(pg) + "-2.jpeg"
        files.append(file2)
        pm2.save(file2)
    
    pdf.close()
    time_end = time.time()
    time_cost = time_end - time_start
    print('totally cost: {}, page: {}, each page cost: {}'.format(
        time_cost, pg + 1, time_cost / (pg + 1)))
    return files

if __name__ == '__main__':
    ocr = PaddleOCR(
        # det_model_dir='./PaddleOCR/output/ch_db_mv3_inference/inference',
        use_angle_cls=False,
        use_gpu=False,
        language_type='en')

    pdfFolder = '../agoda2'
    for p in os.listdir(pdfFolder):
        if p[-4:] == '.pdf':
            pdfPath = pdfFolder + '/' + p
            imgPath = p[:-4]
            # imgPath = pdfFolder+'/'+os.path.basename(p)[:-4]+'/'
            # os.mkdir(imgPath)
            files = pdf2png_agoda2(pdfPath, imgPath)

            for file in files:
                result = ocr.ocr(file, cls=False)
                print(result[0][1])

