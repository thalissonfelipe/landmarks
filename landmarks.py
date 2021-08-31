import os
import argparse


class Extractor:

    def __init__(self, root_dir, output_filename, point):
        self.root_dir = root_dir
        self.output_filename = output_filename
        self.point = point

    def extract(self):
        with open(self.output_filename, 'w') as f:
            directories = os.listdir(self.root_dir)

            for directory in directories:
                directory = os.path.join(self.root_dir, directory)

                if os.path.isdir(directory):
                    files = os.listdir(directory)

                    for file in files:
                        filename = file.split('.')[0] + '.pcd'
                        if file.endswith('lm3'):
                            path = os.path.join(directory, file)
                            points = self.extract_points_from_file(path)
                            if self.point in points:
                                f.write('{}: {}\n'.format(filename, points[self.point]))
                            else:
                                f.write('{}: {}\n'.format(filename, 'null'))

    def extract_points_from_file(self, path):
        with open(path, 'r') as f:
            f.readline() # ignore first line
            f.readline() # ignore second line

            n = int(f.readline().split(' ')[0])
            points = {}

            while n > 0:
                name = f.readline().strip()
                xyz = f.readline().strip()

                points[name] = xyz

                n = n - 1

        return points


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('root_dir', help='Path where the database and .lm3 files are located.')
    parser.add_argument('output_filename', help='Output filename.')
    parser.add_argument('point', help='The landmark you are looking for.')

    args = parser.parse_args()
    extractor = Extractor(args.root_dir, args.output_filename, args.point)
    extractor.extract()
