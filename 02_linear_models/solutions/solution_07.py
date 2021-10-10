def huber_loss(y_true, y_pred, *, epsilon):
    mask_greater_epsilon = np.abs(y_true - y_pred) > epsilon
    loss = np.zeros_like(y_pred)
    loss[mask_greater_epsilon] = np.abs(y_true - y_pred)[mask_greater_epsilon]
    loss[~mask_greater_epsilon] = se_loss(y_true, y_pred)[~mask_greater_epsilon]
    return loss
