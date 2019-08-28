import cv2


camera = cv2.VideoCapture(0)

while True:
	ret,frame=camera.read()
	if ret==False:
		continue
	fd=cv2.CascadeClassifier("CV2.xml")
	faces=fd.detectMultiScale(frame,1.5,5)

	for face in faces:
		x,y,w,h = face
		color = (0,240,0)
		cv2.rectangle(frame,(x,y),(x+w,y+h),color,10)	

	cv2.imshow("Title",frame)
	cv2.waitKey(1)
