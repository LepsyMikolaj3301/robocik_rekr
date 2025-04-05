from setuptools import find_packages, setup

package_name = 'package_humble'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='miki2',
    maintainer_email='mikolaj.lepsy@gmail.com',
    description='Blablabla',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = package_humble.my_node:main'
        ],
    },
)
