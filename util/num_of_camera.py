import cv2


# 获取摄像头的数量
class num_cam(object):
	"""docstring for num_cam"""
	def __init__(self):
		super(num_cam, self).__init__()
		
	def func(self):
		len_cam = 0
		for i in range(100):
			videocapture = cv2.VideoCapture(i)
			if videocapture.isOpened() == False:
				len_cam = i
				break
			videocapture.release()
		return len_cam


if __name__ == '__main__':
	test = num_cam()
	print(test.func())
