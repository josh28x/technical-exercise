from setuptools import find_packages, setup
import os 
from glob import glob 

package_name = 'so_arm_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('so_arm_description', 'launch', '*.launch.py'))), # addition to tell ROS2 build system to include all added .launch.py files from launch directory when instlaling the so_arm_description package
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='joshua',
    maintainer_email='joshua.programming.java@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
