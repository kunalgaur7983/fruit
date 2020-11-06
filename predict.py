#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import numpy as np
from keras.models import load_model
from keras.preprocessing import image

class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictionfruit(self):
        # load model
        model = load_model('model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 1:
            prediction = ' fresh apple'
            return [{ "image" : prediction}]
        elif result[0][1]:
            prediction = 'Fresh banana'
            return [{ "image" : prediction}]
        elif result[0][2]:
            prediction = " fresh orange"
        elif result[0][3]:
            prediction = 'Rotten Apple'
            return [{"image": prediction}]
        elif result[0][4]:
            prediction = " Rotten Banana"
            return [{"image": prediction}]
        else :
            prediction="Rotten Orange"
            return [{"image": prediction}]


