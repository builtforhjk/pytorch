import matplotlib.pyplot as plt
import numpy as np
import torch


def draw_barh(tensor, labels, title, height=0.8, show_text=False):
    '''input should be torch.tensor with shape(1), means vector'''
    
    to_numpy = tensor.data.numpy()
    plt.figure()
    plt.title(title)
    plt.barh(bottom=range(to_numpy.size), width=to_numpy, height=height)
    plt.yticks(torch.arange(0, to_numpy.size, 1), labels)
    if show_text:
        # todo
        pass
    plt.show()
    