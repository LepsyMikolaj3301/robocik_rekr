from setuptools import find_packages, setup

package_name = 'zad_rekr_game'

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
    maintainer_email='miki2@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'keystroke_talker = zad_rekr_game.publisher_get_keystroke:main',
                'game_listener = zad_rekr_game.subscriber_game:main',
        ],
    },
)
