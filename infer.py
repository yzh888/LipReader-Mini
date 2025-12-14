import cv2

# 载入模型
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# 读取图片
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 识别
faces = face_cascade.detectMultiScale(gray, 1.2, 4)

# 画框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 保存结果
cv2.imwrite("result.jpg", img)

print("检测完成！结果已保存到 result.jpg")
