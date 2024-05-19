from fastapi import FastAPI
import cv2

app  = FastAPI()

@app.post('/reduce_img')
async def reduce_img():
    # 读取图像
    image = cv2.imread('WechatIMG155.jpg')

    # 手动标记水印区域（可以使用图像编辑工具创建一个掩码）
    mask = cv2.imread('mask.png', 0)  # mask.png 是二值图像，水印区域为白色，其余部分为黑色

    # 使用 Telea 算法进行 inpainting
    result = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    # 保存去水印后的图像
    cv2.imwrite('image_without_watermark.jpg', result)

    # 显示结果
    cv2.imshow('Original', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    # 读取图像
    # image = cv2.imread('WechatIMG155.jpg')

    # # 转换为灰度图像
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # # 二值化（假设水印较亮）
    # _, mask = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # # 进行形态学操作去除噪声（可选）
    # kernel = np.ones((3,3),np.uint8)
    # mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations = 2)

    # # 保存掩码
    # cv2.imwrite('mask.png', mask)

    return ["hhh"]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3333)