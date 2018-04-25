
Simple Facial Recognition
This is a simple facial recognition project

for use, you will need to change the file directories as can be seen on the code.

#Dependencies
opencv==3.2.0
python==3.5
matplotlib


ISSUE: SCALE FACTOR
Scale factor is used to specify how much of the image size is reduced at each scale. It is easy to identify an image with a single face. But once the image has multiple faces, and some of the faces are in a sense farther away from other faces, it becomes a bit ticklish for this algorithm to recognise such faces. Figure one shows an iconic figure, Elon Musk. With a scale factor of 1.5, it was possible to detect the face.
But for group pictures, where faces are displaced away from other ones, scale factor needs to be modified to detect such faces. Examples are included below:



 
Figure 1 recognition of Icon face with scale factor

 
Figure 2 when the scale factor is 1.05

 
Figure 3 when the scale factor is 1.01





 
Figure 4 when scale factor is 1.005

Future work:
In this project, results are displaced on the console. In future, we will like to present the result in a GUI. We also like to create a web based detection, possibly create an application that can make detect faces in real time. 


