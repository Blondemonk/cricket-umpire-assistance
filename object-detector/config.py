'''
Set the config variable.
'''

# import configparser as cp
import ConfigParser as cp
import json
import os

assert os.path.exists(os.path.join(os.getcwd(), 'data/config/config.cfg'))

config = cp.ConfigParser()
config.read(os.path.join(os.getcwd(), 'data/config/config.cfg'))

min_wdw_sz = json.loads(config.get("hog","min_wdw_sz"))
step_size = json.loads(config.get("hog", "step_size"))
orientations = config.getint("hog", "orientations")
pixels_per_cell = json.loads(config.get("hog", "pixels_per_cell"))
cells_per_block = json.loads(config.get("hog", "cells_per_block"))
visualize = config.getboolean("hog", "visualize")
normalize = config.getboolean("hog", "normalize")
pos_feat_ph = config.get("paths", "pos_feat_ph")
neg_feat_ph = config.get("paths", "neg_feat_ph")
model_path = config.get("paths", "model_path")
threshold = config.getfloat("nms", "threshold")
