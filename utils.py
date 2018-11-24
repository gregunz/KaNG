import numpy as np


def crowdai_score(
    true_labels, pred_labels,
    I=1_000, F=6_000_000, P=0.01
):
    assert set(np.unique(true_labels)) <= {0, 1}
    assert set(np.unique(pred_labels)) <= {0, 1}
    assert true_labels.shape == pred_labels.shape

    N = pred_labels.sum()  # detected #suspicious clients
    M = sum((t == 1 and p == 0)
            for t, p in zip(true_labels, pred_labels))  # missed #suspicious clients

    return - (I * N + F * P * M)
