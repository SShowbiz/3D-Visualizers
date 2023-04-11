import numpy as np

def quaternion2rotation_matrix(qw, qx, qy, qz):
    R = np.zeros((3, 3), dtype=np.float64)

    R[0, 0] = 1 - 2 * qy ** 2 - 2 * qz ** 2
    R[0, 1] = 2 * qx * qy - 2 * qz * qw
    R[0, 2] = 2 * qx * qz + 2 * qy * qw
    R[1, 0] = 2 * qx * qy + 2 * qz * qw
    R[1, 1] = 1 - 2 * qx ** 2 - 2 * qz ** 2
    R[1, 2] = 2 * qy * qz - 2 * qx * qw
    R[2, 0] = 2 * qx * qz - 2 * qy * qw
    R[2, 1] = 2 * qy * qz + 2 * qx * qw
    R[2, 2] = 1 - 2 * qx ** 2 - 2 * qy ** 2

    return R

def flength_offset2intrinsic_matrix(fx, fy, px, py):
    K = np.array([[fx, 0, px], [0, fy, py], [0, 0, 1]], dtype=np.float32)
    
    return K

def translation2translation_matrix(tx, ty, tz):
    t = np.array([[tx], [ty], [tz]], dtype=np.float32)

    return t