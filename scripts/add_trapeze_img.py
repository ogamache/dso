import cv2
from matplotlib.pyplot import contour
import numpy as np
import glob
from tqdm import tqdm

path_to_images = "../../../data/campus_march23th_2022/images/2022-03-23-09-47-05/et_auto/"
path_save_transformed_images = "../../../data/campus_march23th_2022/images/2022-03-23-09-47-05/et_auto_trapeze/"

contours = np.array([[0,1216],[645,608],[1290,608],[1936,1216]])
for image in tqdm(glob.glob(f"{path_to_images}/*.png")):
    filename = image.split("/")[-1]
    img = cv2.imread(image)
    cv2.fillPoly(img, pts=[contours], color=(240,240,240))
    cv2.imwrite(f"{path_save_transformed_images}/{filename}", img)
