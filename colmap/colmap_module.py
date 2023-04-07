import os
from utils import create_database, feature_extraction, feature_matching, save_output_as_txt, sparse_reconstruction


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

# def main(args):
#     # Initial or undistorted images
#     image_path = "preprocessed/scene" if args.initial else "preprocessed/undistorted_scene"
#     data_folder = "colmap/data" if args.initial else "colmap/data_undistort"

#     os.makedirs(data_folder, exist_ok=True)

#     # Create Database
#     create_database(database_path=f"{data_folder}/database.db")

#     # Feature Extraction
#     feature_extraction(
#         database_path=f"{data_folder}/database.db",
#         image_path=image_path,
#         single_camera=1,
#         camera_model="OPENCV"
#     )

#     # Feature Matching
#     feature_matching(database_path=f"{data_folder}/database.db")

#     # # Sparse Reconstruction
#     # sparse_reconstruction(
#     #     database_path=f"{data_folder}/database.db",
#     #     image_path=image_path,
#     #     output_path=f"{data_folder}/sparse"
#     # )

#     # # Save output as txt file
#     # save_output_as_txt(
#     #     input_path=f"{data_folder}/sparse/0",
#     #     output_path=f"{data_folder}/txt",
#     #     output_type="TXT"
#     # )

# if __name__ == "__main__":
#     if not (args.initial or args.undistorted):
#         args.initial = True

#     main(args)