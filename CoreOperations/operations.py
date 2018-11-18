# Libraries Required
import cv2
import numpy as np


class BasicOperationsOnImages:
    """
    Learn to:
        • Access pixel values and modify them
        • Access image properties
        • Setting Region of Image (ROI)
        • Splitting and Merging images
        Almost all the operations in this section is mainly related to Numpy
        rather than OpenCV. A good knowledge
        of Numpy is required to write better optimized code with OpenCV.
    """
    """
        This class has all the basic operation functions to apply on images.
        1. MODIFY : modify pixels in images
        2. ROI : Region of image
        3. GetProperty : Get all the properties of images
        4. Border : Draws a border on image
    """
    __function__ = ['Modify', 'RegionOfImage', 'Border', 'GetProperty']
    def __init__(self, loc):
        self.loc = loc

    def Modify(self):
        """
        @param -> loc: Location of image
        """
        img = cv2.imread(self.loc)
        cv2.resize(img, (600, 600))

        # Modifying some pixels
        img[10:200, 10:500] = [54, 23, 56]
        # cv2.resize(img,(500,500))
        # cv2.imshow('image', img)
        # key = cv2.waitKey(0)
        
    def RegionOfImage(self):
        """
            You can do manipulation to images.
        """

        img = cv2.imread(self.loc)
        region = img[:, :, 0]      # We have selected the region from 250:300 to 250:300
        # img[250:300, 250:300] = [255,255,255]   # Replacing 
        # img[350:400, 550:600] = region
        
        cv2.imshow('Image', region)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def GetProperty(self):
        """
            Prints the properties of image like its shape and size
            rtype: list
        """
        img = cv2.imread(self.loc)
        prop = []
        prop.append(img.shape)
        prop.append(img.size)
        prop.append(img.dtype)
        return prop

    def Border(self):
        """
            Border can be made on images.
            @ cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
            @ borderType : ['cv2.BORDER_CONSTANT','cv2.BORDER_REFLECT','cv2.BORDER_REFLECT_101','cv2.BORDER_WRAP']
        """
        img = cv2.imread(self.loc)
        img = cv2.copyMakeBorder(img,10,10,10,10, cv2.BORDER_WRAP)
        cv2.imshow('Image', img)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()


class ArithmeticOperation:
    """
        • Learn several arithmetic operations on images like addition, subtraction, bitwise operations etc.
        • You will learn these functions : cv2.add(), cv2.addWeighted() etc.
    """
    
    def __init__(self, loc):
        self.loc = loc
    
    def image(self):
        return cv2.imread(self.loc)

    def imageAdd(self, secondImage):
        """
            NOTE: The size of images must be same. For that we can 
            apply some transformations.
            Used function: cv2.addWeighted(src1, val1, src2, val2, gamma)
        """
        img1 = cv2.imread(self.loc)
        img1 = img1[0:200, 0:300]
        img2 = cv2.imread(secondImage)
        img2 = img2[0:200, 0:300]
        result = cv2.addWeighted(img1, 0.7, img2, 0.2,0)
        cv2.imshow('Result', result)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()
