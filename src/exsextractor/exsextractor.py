"""Excel String Extractor"""

# exsextractor.py


# from utils import test_utils  # !DEV
# from .utils import test_utils  # !DIST
from .args import parse_args


def test():
    print(parse_args())


def main():
    args = parse_args()
    input_files = args.input 