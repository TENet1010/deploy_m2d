import numpy as np
from generator import Generator
import myconfig
import torch
from PIL import Image

def gen_night2day(image_arr,Night2day = False):
    modelG = torch.load('Gen_day2night.pth')
    if Night2day:
        modelG = torch.load('Night2day.pth')
    gen = Generator(3, 64)
    gen.load_state_dict(modelG)
    image_arr = myconfig.MYTRANSFORMS_night(image_arr)
    result = gen(image_arr.reshape(1,3,256,256))
    result = result.detach().numpy()[0,:,:,:]
    print(result.shape)
    image = np.moveaxis(result,0,-1)  * 0.5 + 0.5
    return image