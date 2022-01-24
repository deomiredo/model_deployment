import cv2



image = cv2.imread("Dataset/Seledri/001.jpg")   # membaca image
# print(image)

# cv2.imshow('Dataset/Seledri/001', image)      # menampilkan image
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

# print(image.shape)                            # ukuran image

# (b, g, r) = image[20, 100]                    # mengakses nilai di pixel x=100, y=20
# print("blue = ",b)
# print("green = ",g)
# print("red = ",r)

# im_crop = image[100:660, 100:380]             # crop image
# cv2.imshow('crop',im_crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(im_crop.shape)

cp_image = image.copy()                         # mengcopy image
# print(cp_image.shape)

# cp_image[300:350, 170:300] = (100, 255, 240)    # mengubah nilai pixel
# cv2.imshow('cp_image',cp_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# im_resized = cv2.resize(image, (400,400))       # resize image # ignore aspect ratio
# cv2_imshow(im_resized)

# r = 400/image.shape[1]                          # resize image (mempertahankan aspect ratio)
# dim = (400,int(image.shape[0]*r))
# im_resized = cv2.resize(image, dim)
# cv2_imshow(im_resized)

# (h, w) = image.shape[:2]                        # Rotating an image
# center = (w/2, h/2)
# M = cv2.getRotationMatrix2D(center, 180, 1.0)
# rotated = cv2.warpAffine(image, M, (w,h))
# cv2_imshow(rotated)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite("rotate.png", rotated)                 # menyimpan image

import numpy as np                                # adjust image contrast
# im_adjusted = cv2.addWeighted(im_resized, 1.5, np.zeros(im_resized.shape, im_resized.dtype), 0, -100)

# cv2.imshow('Original Image',im_resized)
# cv2.imshow('Adjusted Image',im_adjusted)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# im_edges = cv2.Canny(image, 100, 200)          # detect edges

# cv2.imshow('Original Image',image)
# cv2.imshow('Detected Edges',im_edges)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite("edge.png", im_edges)


# im_gray = cv2.cvtColor(im_resized, cv2.COLOR_BGR2GRAY) # convert image to grayscale
# cv2.imshow('Original Image',im_resized)
# cv2.imshow('Grayscale Image',im_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# get all files in a folder

import glob
imdir = 'Dataset/Seledri/'
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

images = [cv2.imread(file) for file in files]

# adjust contrast to all of them nd save to different location
i = 1
for img in images:
    im_edges = cv2.Canny(img, 100, 200)
    # im_adjusted = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, -100)
    im_name = "Dataset/Seledri_Edge/" + str(i) + ".jpg"
    cv2.imwrite(im_name, im_edges)
    i+=1