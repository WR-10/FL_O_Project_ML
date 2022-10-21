import torch
import cv2


# 함수
def ml_yolov5(image):
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    print(image) #"2022/10/18/sdklfjsdiofklj.jpg"

    img = cv2.imread("media/"+image)
    results = model(img)

    result = results.pandas().xyxy[0].to_numpy()
    res = []
    for i in result:

        print(i)
        if i[4] > 0.1:
            res.append(i[6])

    return list(set(res))
