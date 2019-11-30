import math
import cv2
import numpy as np
from skimage.measure import compare_ssim


class Filtration:
    def __init__(self):
        self.__list_contours = None
        self.__image = None
        self.__height = None
        self.__width = None

    def set_params(self, list_contours, image):
        self.__list_contours = list_contours
        self.__image = image
        self.__height = image.shape[0]
        self.__width = image.shape[1]

    def filtrating(self):
        list_rectangles = []
        list_subimages_with_contours = []
        for contour in self.__list_contours:
            found_rectangle = self.__find_rectangle(contour)
            list_rectangles.append(found_rectangle)
            list_subimages_with_contours.append(self.__createROI(found_rectangle[0], found_rectangle[1],self.__image))
        biggest_rectangle = self.__find_biggest_rectangle(list_rectangles)
        #CODE BELOW NOT EXACTLY IT WORKS
        # list_scaled_images = self.__scale_images_to_size(list_subimages_with_contours, biggest_rectangle[1, 0],
        #                                                  biggest_rectangle[1, 1])
        # matrix_compared_mse_ssim = self.__create_matrix_compared(list_scaled_images)
        print(biggest_rectangle)

    def __find_rectangle(self, contours: np.array) -> np.array:
        size_list = len(contours)
        sorted_ascending_array_by_x = sorted(contours, key=lambda k: [k[1], k[0]])
        sorted_ascending_array_by_y = sorted(contours, key=lambda k: [k[0], k[1]])
        max_y = sorted_ascending_array_by_y[size_list - 1][1]
        max_x = sorted_ascending_array_by_x[size_list - 1][0]
        min_x = sorted_ascending_array_by_x[0][0]
        min_y = sorted_ascending_array_by_y[0][1]
        # { contures = [
        #               [ left_up_X, left_up_Y ] [ left_down_X , left_down_Y ]
        #              ]
        # IMAGE MATRIX  0 ---------MAX_X
        #               |
        #              MAX_Y

        corners = np.array([
            [min_x, min_y], [max_x, max_y]
        ])
        return corners

    #   TWORZY POD OBRAZZ OBRAZU
    def __createROI(self, left_up_corner: np.array, right_down_corner: np.array, white_black_image):
        return self.__image[left_up_corner[0]:right_down_corner[0], left_up_corner[1]:right_down_corner[1]]

    def __find_biggest_rectangle(self, list_rectangles: list) -> np.array:
        list_diagonals = []
        for rectangle in list_rectangles:
            left_up_x = rectangle[0, 0]
            left_up_y = rectangle[0, 1]
            right_down_x = rectangle[1, 0]
            right_down_y = rectangle[1, 1]
            list_diagonals.append(self.__count_distance_between_two_points(left_up_x, left_up_y, right_down_x,
                                                                           right_down_y))
        max_rectangle = 0
        current_diagonal = list_diagonals[0]
        index = 0
        for diagonal in list_diagonals:
            if(diagonal > current_diagonal):
                current_diagonal = diagonal
                max_rectangle = index
            index = index +1
        return list_rectangles[max_rectangle]

    def __count_distance_between_two_points(self, x1, y1, x2, y2):
        return math.sqrt((x1 - x2) * (x1 * x2) + (y1 - y2) * (y1 - y2))

    def __scale_images_to_size(self, list_images, width, height) -> np.array:
        dim = (width, height)
        list_reseized_images = []
        for unreised_image in list_images:
            list_reseized_images.append(cv2.resize(unreised_image, dim, interpolation=cv2.INTER_AREA))
        return list_reseized_images

    def __mse(self, imageA, imageB):
        # the 'Mean Squared Error' between the two images is the
        # sum of the squared difference between the two images;
        # NOTE: the two images must have the same dimension

        # return the MSE, the lower the error, the more "similar"
        # the two images are
        return np.square(np.subtract(imageA,imageB)).mean()

    def __compare_images(self, image_a, image_b):
        # compute the mean squared error and structural similarity
        # index for the images
        m = self.__mse(image_a, image_b)
        (score, diff) = compare_ssim(image_a, image_b, full=True)
        s = (diff * 255).astype("uint8")

        return np.array([m, s])

        # # setup the figure
        # fig = plt.figure(title)
        # plt.suptitle("MSE: %.2f, SSIM: %.2f" % (m, s))
        #
        # # show first image
        # ax = fig.add_subplot(1, 2, 1)
        # plt.imshow(image_a, cmap=plt.cm.gray)
        # plt.axis("off")
        #
        # # show the second image
        # ax = fig.add_subplot(1, 2, 2)
        # plt.imshow(image_b, cmap=plt.cm.gray)
        # plt.axis("off")
        #
        # # show the images
        # plt.show()

    def __create_matrix_compared(self, list_post_scaled_images):
        size_list = len(list_post_scaled_images[0])
        matrix_compared_by_mse = np.zeros((size_list, size_list))
        matrix_compared_by_ssim = np.zeros((size_list, size_list))
        for outer_index in range(0, size_list - 1):
            for inner_index in range(0, size_list - 1):
                mse_ssim_matrix = self.__compare_images(list_post_scaled_images[outer_index],
                                                        list_post_scaled_images[inner_index])
                matrix_compared_by_mse[outer_index, inner_index] = mse_ssim_matrix[0]
                matrix_compared_by_ssim[outer_index, inner_index] = mse_ssim_matrix[1]

        return np.array([matrix_compared_by_mse, matrix_compared_by_ssim])
