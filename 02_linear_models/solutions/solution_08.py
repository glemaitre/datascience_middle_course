def absolute_loss(y_true, y_pred):
    loss = np.abs(y_true - y_pred)
    return loss
