import torch
import cv2


# 함수
def ml_yolov5(image): # 파라미터
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    print(image) #"2022/10/18/sdklfjsdiofklj.jpg"

    img = cv2.imread("media/"+image) # 여기 까지가 이미지 받아오는 부분
    results = model(img)

    result = results.pandas().xyxy[0].to_numpy()
    res = []
    for i in result:
        if i[4] > 0.5:
            res.append(i[6]) # 1: res = ['suitcase'] 2: res = ['suitcase','suitcase'] 3: res = ['suitcase','suitcase','suitcase']
    
    # res = [item[6] for item in result if item[4]>0.5]
    print(res)
    print(list(set(res)))

    return list(set(res))
