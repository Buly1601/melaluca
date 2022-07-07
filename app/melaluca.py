import tensorflow as tf
import numpy as np
import pandas as pd
import os

# For melaluca, we have 39 different labels
# use list to convert from int to string
LABEL_LIST = ["Apple_scab"
,"Apple_black_rot"
,"Apple_cedar_apple_rust"
,"Apple_healthy"
,"Background_without_leaves"
,"Blueberry_healthy"
,"Cherry_powdery_mildew"
,"Cherry_healthy"
,"Corn_gray_leaf_spot"
,"Corn_common_rust"
,"Corn_northern_leaf_blight"
,"Corn_healthy"
,"Grape_black_rot"
,"Grape_black_measles"
,"Grape_leaf_blight"
,"Grape_healthy"
,"Orange_haunglongbing"
,"Peach_bacterial_spot"
,"Peach_healthy"
,"Pepper_bacterial_spot"
,"Pepper_healthy"
,"Potato_early_blight"
,"Potato_healthy"
,"Potato_late_blight"
,"Raspberry_healthy"
,"Soybean_healthy"
,"Squash_powdery_mildew"
,"Strawberry_healthy"
,"Strawberry_leaf_scorch"
,"Tomato_bacterial_spot"
,"Tomato_early_blight"
,"Tomato_healthy"
,"Tomato_late_blight"
,"Tomato_leaf_mold"
,"Tomato_septoria_leaf_spot"
,"Tomato_spider_mites_two_spotted_spider_mite"
,"Tomato_target_spot"
,"Tomato_mosaic_virus"
,"Tomato_yellow_leaf_curl_virus"]

LABEL_MAP = {1: 'Apple_scab', 2: 'Apple_black_rot', 
            3: 'Apple_cedar_apple_rust', 4: 'Apple_healthy',
            5: 'Background_without_leaves', 6: 'Blueberry_healthy',
            7: 'Cherry_powdery_mildew', 8: 'Cherry_healthy',
            9: 'Corn_gray_leaf_spot', 10: 'Corn_common_rust',
            11: 'Corn_northern_leaf_blight', 12: 'Corn_healthy',
            13: 'Grape_black_rot', 14: 'Grape_black_measles',
            15: 'Grape_leaf_blight', 16: 'Grape_healthy',
            17: 'Orange_haunglongbing', 18: 'Peach_bacterial_spot',
            19: 'Peach_healthy', 20: 'Pepper_bacterial_spot', 21: 'Pepper_healthy',
            22: 'Potato_early_blight', 23: 'Potato_healthy',
            24: 'Potato_late_blight', 25: 'Raspberry_healthy',
            26: 'Soybean_healthy', 27: 'Squash_powdery_mildew',
            28: 'Strawberry_healthy', 29: 'Strawberry_leaf_scorch',
            30: 'Tomato_bacterial_spot', 31: 'Tomato_early_blight',
            32: 'Tomato_healthy', 33: 'Tomato_late_blight', 34: 'Tomato_leaf_mold',
            35: 'Tomato_septoria_leaf_spot', 36: 'Tomato_spider_mites_two_spotted_spider_mite',
            37: 'Tomato_target_spot', 38: 'Tomato_mosaic_virus', 39: 'Tomato_yellow_leaf_curl_virus'}

def download_and_prepare():
    """
    Download pretrained model from colab.
    Maleluca v1.0
    Returns prepared model to predict on.
    """
    return 


def predict(img, model=download_and_prepare()):
    """
    Takes in image and predicts from.
    Returns prediction as np and string.
    """
    return 



