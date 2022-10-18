# import torch
# import cv2


# def ml_yolov5(image):
#     model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True) # 여기다가 학습시킨 콜랩을 넣는 것임 우리는 이거를 해야함! 이거 뭔데? 나도 몰라 ㅎㅎ 학습된 결과물임!!!!!!!!! 라이브러리 
#     # 사진 경로

#     print(image)
#     img = cv2.imread(image)
    # results = model(img)
    # results.save()

    # result = results.pandas().xyxy[0].to_numpy()
    # print(result)
    # result = [item for item in result if item[6]=='person']


    # for 문 돌려서 학습시킨다??

    # 분류는 어케함?? 개빡치네 ㅎㅎ
    # 여기서는 웹에서 데이터를 받고 코랩에서 학습시킨걸 던지고 나온 결과를 받아서 외부로 전송하는거니까 yolo 쓰는거는 콜랩이랑 다르다 분리해서 생각해야함!
    # tmp_img = cv2.imread('Untitled.jpeg')
    # print(tmp_img.shape)
    # cropped = tmp_img[int(result[0][1]):int(result[0][3]), int(result[0][0]):int(result[0][2])]
    # print(cropped.shape)
    # cv2.imwrite('result2.png', cropped)
    # cv2.rectangle(tmp_img, (int(results.xyxy[0][0][0].item()), int(results.xyxy[0][0][1].item())), (int(results.xyxy[0][0][2].item()), int(results.xyxy[0][0][3].item())), (255,255,255))
    # cv2.imwrite('result.png', tmp_img)

    # return 0

# 인식한거 잘라주기 
 # 경로  
