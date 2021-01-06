"""
****************************************************************
#Author: wennyramadha
#This is the implementation of Median Filter
****************************************************************
"""
import cv2


def filtering(image): #median filter
        img_filter = image[:]
        for j in range(len(image)):
            for i in range(j):
                img_filter[j, i] = image[j, i]
        members = [image[0, 0]] * 9
        for j in range(1, image.shape[0] - 1):
            for i in range(1, image.shape[1] - 1):
                members[0] = image[j - 1, i - 1]
                members[1] = image[j, i - 1]
                members[2] = image[j + 1, i - 1]
                members[3] = image[j - 1, i]
                members[4] = image[j, i]
                members[5] = image[j + 1, i]
                members[6] = image[j - 1, i + 1]
                members[7] = image[j, i + 1]
                members[8] = image[j + 1, i + 1]

                members.sort()
                img_filter[j, i] = members[4]
            # cv2.imshow("filter", img_filter)
        return img_filter

if __name__ == '__main__':
    img=cv2.imread("S5000L00.png")
    gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    cv2.imshow("original image", img)
    img_filter=filtering(gray)
    cv2.imshow("filtered image", img_filter)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



