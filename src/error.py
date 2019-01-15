import numpy as np


def measure_penalty_error(embeddings, centers, radii, edge_map, nodes):
    edge_count = embeddings.shape[0]
    error = 0.
    for i in range(edge_count):
        edge = edge_map[i]
        n_u = edge[0]
        n_v = edge[1]
        n_u_ind = np.where(nodes == n_u)
        n_v_ind = np.where(nodes == n_v)
        X_uv = embeddings[i]
        c_u = centers[n_u_ind]
        c_v = centers[n_v_ind]
        r_u = radii[n_u_ind]
        r_v = radii[n_v_ind]
        if np.linalg.norm(X_uv - c_u) > r_u:
            error += np.linalg.norm(X_uv - c_u) ** 2 - r_u ** 2
        if np.linalg.norm(X_uv - c_v) > r_v:
            error += np.linalg.norm(X_uv - c_v) ** 2 - r_v ** 2

    return error