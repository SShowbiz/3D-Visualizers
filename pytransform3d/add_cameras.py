import numpy as np
import matplotlib.pyplot as plt
import pytransform3d.camera as pc
import pytransform3d.transformations as pt
from utils import flength_offset2intrinsic_matrix, quaternion2rotation_matrix, translation2translation_matrix


txt_path = "/home/sshowbiz/Desktop/VCLab/NeRF-Stylization/face_segment/txt" # PUT your txt folder path generated by COLMAP
intrinsic_path = f"{txt_path}/cameras.txt"
extrinsic_path = f"{txt_path}/images.txt"

with open(intrinsic_path, "r") as i, open(extrinsic_path, "r") as e:
    iline = i.readline()
    while iline.startswith("#"):
        iline = i.readline()
    _, __, width, height, fx, fy, px, py, *_ = iline.split(' ')
    intrinsic = flength_offset2intrinsic_matrix(fx=float(fx), fy=float(fy), px=float(px), py=float(py)).astype('float64')
    sensor_size = np.array([width, height]).astype('float64')
    extrinsics = []
    eline = e.readline()
    while eline != "":
        if eline.endswith('.png\n'):
            _, qw, qx, qy, qz, tx, ty, tz, __, name = eline.split(' ')
            R_world2cv = quaternion2rotation_matrix(qw=float(qw), qx=float(qx), qy=float(qy), qz=float(qz))
            R = R_world2cv.T

            T_world2cv = translation2translation_matrix(tx=tx, ty=ty, tz=tz)
            location = -R_cv2world @ T_world2cv
            extrinsic = np.vstack((np.hstack((R, location)), np.array([0, 0, 0, 1])))
            extrinsics.append(extrinsic)

        eline = e.readline()

    for extrinsic in extrinsics:
        virtual_image_distance = 0.3
        ax = pt.plot_transform(A2B=extrinsic, s=0)
        ax.set_xbound(lower=-4, upper=4)
        ax.set_ybound(lower=4, upper=-4)
        ax.set_zbound(lower=-2, upper=6)
        pc.plot_camera(
            ax, cam2world=extrinsic, M=intrinsic, sensor_size=sensor_size,
            virtual_image_distance=virtual_image_distance)
        
    plt.show()