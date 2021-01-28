import torch as tch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

def tch_logistic(x, y, max_iter=5000, lr=1e-3):
    """ Binary logistic regression in PyTorch

    args:
        x (nxp tensor): explanatory variables
        y (nx1 tensor): binary response variable

    """
    in_dim = x.shape[1]
    model = nn.Linear(in_dim, 1)
    optim = tch.optim.Adam(model.parameters(), lr=lr)
    loss_fn = nn.BCELoss()

    for i in range(max_iter):
        y_pred = tch.sigmoid(model(x))
        loss = loss_fn(y_pred, y)
        optim.zero_grad()
        loss.backward()
        optim.step()

    model.eval()

    y_hat = tch.sigmoid(model(x).detach())
    pred = tch.where(y_hat < 0.5, 0, 1)
    accuracy = (pred == y).sum() / len(y)

    print("Accuracy: ", accuracy.item())

    return

x = 10 + 90.*tch.rand(100).reshape(-1,1)
bx = -10 + 0.3*x
p = 1. / (1. + tch.exp(-bx))
y = tch.bernoulli(p)
tch_logistic(x,y)
