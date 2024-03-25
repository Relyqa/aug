import argparse


def argumentos():
    """Parse execution arguments.
    """
    parser = argparse.ArgumentParser(description='YOLOv8 training parameters')
    parser.add_argument('--base_model', type=str, help='yolov8 base model ')
    args = parser.parse_args()
    return args


def main(base_model):
    print("Inicio")
    print(base_model)
    print("Final")
    return f"Inicio {base_model} final del archivo"


if __name__ == '__main__':
    args = argumentos()
    main(args.base_model)
