from setuptools import find_packages, setup

package_name = 'yolo_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'ultralytics', 'rosnumpy'],
    zip_safe=True,
    maintainer='vaj',
    maintainer_email='vaj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'yolo_main = yolo_node.yolo_node:main',
		'yolo_gpt = yolo_node.yolo_gpt:main',
		'yolo_claude = yolo_node.yolo_claude:main',
		'yolo_copylot = yolo_node.yolo_copylot:main'
        ],
    },
)
