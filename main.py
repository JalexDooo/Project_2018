import face_recognition as fr
from database.dataset import get_file
from util.num_of_camera import num_cam
from generalcode.multiprocessing_face_recognition.multiprocessing_func import multiprocessing_face_recognition
from config import opt

def face_recognition(number_of_cpu):
	path = './database/face_recognition_database'
	face_database = get_file(path)
	image_list, label_list = face_database.func()

	known_faces = []
	for i in range(len(image_list)):
		tmp = fr.load_image_file(image_list[i])
		known_faces.append(list(fr.face_encodings(tmp)[0]))

	num_camera = num_cam().func()
	num_cam_list = []
	for i in range(num_camera):
		num_cam_list.append(i)

	print(num_cam_list)
	main_face = multiprocessing_face_recognition(number_of_cpu, num_cam_list, label_list, known_faces)



if __name__ == '__main__':
	face_recognition = face_recognition(opt.number_of_cpu)