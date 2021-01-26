import torch as tch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

def torch_lm(x, y, max_iter=5000, min_loss=1e-6, lr=1e-3):
    """ Linear regression in PyTorch

    args:
        x (nxp tensor): explanatory variables
        y (nx1 tensor): target variable
    """
    in_dim = x.shape[1]
    model = nn.Linear(in_dim, 1)
    optimizer = tch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    it = 0
    loss_val = tch.tensor([10.], requires_grad=True)

    while (it < max_iter) and (loss_val > min_loss):
        y_pred = model(x)
        loss_val = criterion(y_pred, y)
        optimizer.zero_grad()
        loss_val.backward()
        optimizer.step()

        it += 1

    model.eval()

    y_hat = model(x)
    resid = y_hat - y
    rmse = tch.sqrt((resid**2).mean())

    return {"fitted_values": y_hat.detach().numpy().flatten(),
            "residuals": resid.detach().numpy().flatten(),
            "rmse": rmse.item()
            }


# x = np.linspace(0, 10, 100)
# y = 3*x + 4 + np.random.normal(0, 2, 100)
# X = tch.tensor(x).reshape(-1, 1).float()
# Y = tch.tensor(y).reshape(-1,1).float()
# fitted_mod = torch_lm(X, Y)
# print(fitted_mod)
