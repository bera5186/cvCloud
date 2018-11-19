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
        
    def BitWiseOperation(self, secondImage):
        img1 = cv2.imread(self.loc)
        img2 = cv2.imread(secondImage)
        rows, cols, channels = img2.shape
        roi = img1[0:rows, 0:cols]
        img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 125, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        #img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
        #img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

        #dst = cv2.add(img1_bg, img2_fg)
        print(ret)
     
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(mask_inv, 'Ajay',(100,100), font,  4, (0,255,255), 3, cv2.LINE_AA)
     
        cv2.imshow('Mask',mask)
        cv2.imshow('Inverted mask', mask_inv)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def PerformanceMeasurement(self):
        """
        Performance Measurement and Improvement Techniques
        In image processing, since you are dealing with large number of operations per second, it is mandatory that your code
        is not only providing the correct solution, but also in the fastest manner. So in this chapter, you will learn
        • To measure the performance of your code.
        • Some tips to improve the performance of your code.
        • You will see these functions : cv2.getTickCount, cv2.getTickFrequency etc.
        """
        img = cv2.imread(self.loc)
        e1 = cv2.getTickCount()
        for i in range(5,49,2):
            img = cv2.medianBlur(img, 5)
        e2 = cv2.getTickCount()
        t = (e2-e1)/cv2.getTickFrequency()
        cv2.imshow('Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        font = cv2.FONT_HERSHEY_COMPLEX
        cam = cv2.VideoCapture(0)
        while(True):
            _, frame = cam.read()
            cv2.putText(frame, 'Ajay',(100,100), font,  4, (255,255,255), 3, cv2.LINE_AA)
            # frame = cv2.medianBlur(frame, 2)
            cv2.imshow('Frame', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()
        print('Tick Frequency: {}'.format(cv2.getTickFrequency()))
        print(t)
    
    def TrackBar(self):
        import numpy as np
        
        def nothing(x):
            pass
        # Create a black image, a window
        img = np.zeros((1080,720,3), np.uint8)
        cv2.namedWindow('image')
        # create trackbars for color change
        cv2.createTrackbar('R','image',0,255,nothing)
        cv2.createTrackbar('G','image',0,255,nothing)
        cv2.createTrackbar('B','image',0,255,nothing)
        # create switch for ON/OFF functionality
        switch = '0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, 'image',0,1,nothing)
        while(1):
            cv2.imshow('image',img)
            k = cv2.waitKey(1) & 0xFF
            if k == 27:
                break
            # get current positions of four trackbars
            r = cv2.getTrackbarPos('R','image')
            g = cv2.getTrackbarPos('G','image')
            b = cv2.getTrackbarPos('B','image')
            s = cv2.getTrackbarPos(switch,'image')
            if s == 0:
                img[:] = 0
            else:
                img[:] = [b,g,r]
        cv2.destroyAllWindows()
        


