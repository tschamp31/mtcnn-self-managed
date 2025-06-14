# MIT LICENSE
#
# Copyright (c) 2019-2024 Iván de Paz Centeno
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        return f.read()

setup(
    name='mtcnn',
    version='1.0.0',
    description='Multitask Cascaded Convolutional Networks for face detection and alignment (MTCNN) in Python >= 3.10 and TensorFlow >= 2.17',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/tschamp31/mtcnn-self-managed',
    license='MIT',
    packages=find_packages(exclude=['tests', 'docs']),
    install_requires=[
        'joblib>=1.4.2',
        'lz4>=4.3.3',
    ],
    extras_require={
        'tensorflow': [
            'tensorflow>=2.17.0'
        ],
        'dev': [
            'pytest>=8.3.3',
            'pytest-cov>=5.0.0',
            'mkdocs>=1.6.1',
            'mkdocs-material>=9.5.39',
            'mkdocs-jupyter>=0.25.0'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.12',
    include_package_data=True,
    package_data={
        'mtcnn': ['assets/weights/*.lz4'],
    }
)
