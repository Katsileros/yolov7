from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='yolo-v7',
    packages=find_packages(),
    version='1.0',
    description='yolo-v7 framework from WongKinYiu',
    url=' https://github.com/WongKinYiu/yolov7.git',
    author='WongKinYiu',
    license='GNU GENERAL PUBLIC LICENSE',
    install_requires=required
)
