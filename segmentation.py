from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('yolov5s.pt')
results = model.predict('images/cat-frezze.jpeg',stream=True, retina_masks=True)
for result in results:
    mask = result.masks.cpu().numpy()
    masks = mask.masks.astype(bool)
    ori_img = result.orig_img
    for m in masks:
        new = np.zeros_like(ori_img, dtype=np.uint8)
        new[m] = ori_img[m]
        cv2.imshow('p', new)
        if cv2.waitKey(0) == ord('q'):
            break