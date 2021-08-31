# Landmarks Analysis - (TCC)

Repository containing algoritms to extract fiducial points from Bosphorus database and jupyter notebooks with some analysis about these points.

## Dependencies

- Python 3
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Jupyter Notebook

To install all dependencies, run:

```
pip3 install -r requirements.txt
```

## How to use (`main.py`)

The purpose of this algorithm is to extract the fiducial points that are marked in the bosphorus .lm3 files and then creating new .pcd files from them.

To run this algorithm, it is necessary to pass three mandatory parameters:

**root_dir**: path where all Bosphorus .lm3 files are located.

**output_dir**: directory where the fiducial points will be saved.

**points**: list of points you want to extract from .lm3 files. "Nose tip" and "Outer left eyebrow" are some examples.

#### Example

```
python3 main.py /path/to/bosphorus/database landmarks "Nose tip" "Outer left eyebrow" "Outer right eyebrow"
```

## How to use (`landmarks.py`)

The purpose of this algorithm is to save the name of the clouds and their respective fiducial points (one at a time). 

To run this algorithm, it is necessary to pass three mandatory parameters:

**root_dir**: path where all Bosphorus .lm3 files are located.

**output_filename**: directory where the points will be saved.

**point**: landmark you are looking for.

#### Example

```
python3 landmarks.py /path/to/bosphorus/database left_eye.txt "Nose tip"
```

Output Example:

left-eye.txt

```
bs000_CAU_A22A25_0.pcd: -25.335 -23.994 48.096
bs000_CAU_A26A12lw_0.pcd: -23.834 -24.735 48.571
```
