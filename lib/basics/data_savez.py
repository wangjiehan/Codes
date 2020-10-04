import numpy as np

x = np.load('word_emb-val.npy')
y = np.load('label-val.npy')

np.savez('data_val.npz', x, y)
