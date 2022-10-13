import matplotlib.pyplot 

def loss_fn(y, y_hat):
    square_diffs = (y_hat - y) ** 2
    mse = square_diffs.mean()
    return mse

