from keras.utils import plot_model
import pydot
import keras
import pydotplus
from keras.utils.vis_utils import model_to_dot


keras.utils.vis_utils.pydot = pydot


#Predefine model 

plot_model(model,to_file='/home/deeptek4/Desktop/UXception.png',show_shapes='True')
