# HandwritingRecognition

Handwritten text recognition to convert texts to its electronic format is common
nowadays by using machine learning techniques. For this project we have used the two most
common approaches of neural networks to recognize handwritten alphanumeric (digits and
letters) characters. Where we experiment and see which performs better in terms of the
recognition accuracy and architecture’s complexity. We have used multilayer perceptron neural
network (MLP) and convolutional neural network (CNN) for supervised learning. We train and
test our models with the EMNIST (Extended-MNIST) dataset; which contains digits, uppercase
and lowercase alphabet letters. The experiments show that CNNs with an error rate 12.36%
performance better than the MLP network in terms of accuracy and confidence rate as the CNN
has accuracy of about 4% higher than MLP. However, due to the lack of context both neural
networks face misclassification for letters with others of similar shape but have different casing
(uppercase versus lowercase).
