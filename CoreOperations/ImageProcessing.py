import cv2
import numpy as np

class Colorspace:
    """
        Learn to change images between different color spaces.
        Plus learn to track a colored object in a video.
    """
    def __init__(self, loc):
        self.loc = loc
    
    def ChangeColorSpace(self):
        """
        @param self: object instance
        """
        # Two functions cv2.cvtColor() and cv2.inRange()
        img = cv2.imread(self.loc)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        cv2.imshow('Frame', img)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()

    def ObjectTracking(self):
        """
            The user can set different values of lower and upper bound
            in cv2.inRange() function from slider.

        """
        url = 'https://10.1.202.66:8080/video'
        cam = cv2.VideoCapture(0)
        cv2.namedWindow('Frame')
        
        def nothing():
            pass

        cv2.createTrackbar('R1','Frame',0,255,nothing)
        cv2.createTrackbar('G1','Frame',0,255,nothing)
        cv2.createTrackbar('B1','Frame',0,255,nothing)
        
        
        cv2.createTrackbar('R2','Frame',0,255,nothing)
        cv2.createTrackbar('G2','Frame',0,255,nothing)
        cv2.createTrackbar('B2','Frame',0,255,nothing)
        
        switch = '0 : OFF \n1 : ON'
        cv2.createTrackbar(switch, 'Frame',0,1,nothing)
        lower_blue = np.array([150,56,10])
        upper_blue = np.array([255,16,70])
        
        while True:
            _, frame = cam.read()
            
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_blue, upper_blue)
            res = cv2.bitwise_and(frame, frame, mask=mask)
            blur = cv2.GaussianBlur(res,(5,5),0)
            # ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
            cv2.imshow('Frame', blur)
            cv2.imshow('HSV', hsv)
            r1 = cv2.getTrackbarPos('R1','Frame')
            g1 = cv2.getTrackbarPos('G1','Frame')
            b1 = cv2.getTrackbarPos('B1','Frame')
            r2 = cv2.getTrackbarPos('R2','Frame')
            g2 = cv2.getTrackbarPos('G2','Frame')
            b2 = cv2.getTrackbarPos('B2','Frame')
            s = cv2.getTrackbarPos(switch,'Frame')
            result = blur
            cv2.imshow('Result', result)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            lower_blue[0] = r1
            lower_blue[1] = g1
            lower_blue[2] = b1

            upper_blue[0] = r2
            upper_blue[1] = g2
            upper_blue[2] = b2

        cam.release()
        cv2.destroyAllWindows()