import os



class Parser:
    def __init__(self, root_dir, output_dir, save_txt=False, points_name=None):
        self.root_dir = root_dir
        self.output_dir = output_dir
        self.points_name = points_name
        self.save_txt = save_txt

    def parse(self):
        directories = os.listdir(self.root_dir)

        for directory in directories:
            folder = directory
            directory = os.path.join(self.root_dir, directory)

            if os.path.isdir(directory):
                files = os.listdir(directory)

                for file in files:
                    file = os.path.join(directory, file)

                    if os.path.isfile(file):
                        if file.endswith('lm3'):
                            points = self._extract_points_from_file(file)
                            self._generate_pcd(points, folder, file)

    def _extract_points_from_file(self, file):
        with open(file, 'r') as f:
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

    def _generate_pcd(self, points, folder, file):
        filename = file.split('/')[-1].split('.')[0] + '.pcd'
        folder = os.path.join(self.output_dir, folder)

        try:
            os.makedirs(folder)
        except OSError:
            pass

        path = os.path.join(folder, filename)

        txt = path[:-3] + 'txt'
        txtFile = open(txt, 'wb')

        with open(path, 'wb') as f:
            if self.points_name is None:
                self._write_header(f, len(points.items()))

                for k, v in points.items():
                    f.write('{}\n'.format(v))
                    txtFile.write('{} - {}\n'.format(k, v))

            else:
                self._write_header(f, len(self.points_name))

                for k, v in points.items():
                    if k in self.points_name:
                        f.write('{}\n'.format(v))

                        if self.save_txt:
                            txtFile.write('{} - {}\n'.format(k, v))

        txtFile.close()

    def _write_header(self, f, n):
        f.write('# .PCD v0.7 - Point Cloud Data file format\n')
        f.write('VERSION 0.7\n')
        f.write('FIELDS x y z\n')
        f.write('SIZE 4 4 4\n')
        f.write('TYPE F F F\n')
        f.write('COUNT 1 1 1\n')
        f.write('WIDTH 1\n')
        f.write('HEIGHT {}\n'.format(n))
        f.write('VIEWPOINT 0 0 0 1 0 0 0\n')
        f.write('POINTS {}\n'.format(n))
        f.write('DATA ascii\n')


if __name__ == '__main__':
    root_dir = '/media/thalisson/Seagate Expansion Drive/BD Faces/Bosphorus'
    output_dir = './landmarks'
    points_name = ['Inner left eye corner']

    parser = Parser(root_dir, output_dir, points_name=points_name)
    parser.parse()
