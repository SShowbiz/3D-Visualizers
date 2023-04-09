import os
from utils import create_database, feature_extraction, feature_matching, save_output_as_txt, sparse_reconstruction, colmap_to_json
from pathlib import Path

class COLMAP:
    def __init__(self) -> None:
        pass

    def extract_cameras(self, img_path, save_path):
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        
        create_database(database_path=f"{save_path}/database.db")
        feature_extraction(
            database_path=f"{save_path}/database.db",
            image_path=img_path,
            single_camera=1,
            camera_model="OPENCV"
        )
        feature_matching(database_path=f"{save_path}/database.db")
        sparse_reconstruction(
            database_path=f"{save_path}/database.db",
            image_path=img_path,
            output_path=f"{save_path}/sparse"
        )
        save_output_as_txt(
            input_path=f"{save_path}/sparse/0",
            output_path=f"{save_path}/txt",
            output_type="TXT"
        )
        save_output_as_txt(
            input_path=f"{save_path}/sparse/0",
            output_path=f"{save_path}/txt",
            output_type="TXT"
        )
        colmap_to_json(
            recon_dir=Path(f"{save_path}/sparse/0"),
            output_path=Path(save_path),
        )