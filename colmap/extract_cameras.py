import argparse
from colmap_module import COLMAP

parser = argparse.ArgumentParser(description="extract cameras from images")
parser.add_argument("--img_path", help="image path for camera parameter extraction")
parser.add_argument("--save_path", help="save path for camera parameter files")
parser.add_argument("--gpu", action="store_true", help="save path for camera parameter files")
args = parser.parse_args()

if __name__ == "__main__":
    colmap = COLMAP()
    colmap.extract_cameras(img_path=args.img_path, save_path=args.save_path)

