from setuptools import setup

package_name = 'livox_lidar_topic'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='exceedingli',
    maintainer_email='exceedingli@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
         'topic_helloworld_pub  = livox_lidar_topic.topic_helloworld_pub:main',
         'topic_helloworld_sub  = livox_lidar_topic.topic_helloworld_sub:main',
         'camera_data_pub      = livox_lidar_topic.camera_data_pub:main',
         'camera_data_sub      = livox_lidar_topic.camera_data_sub:main',
        ],
    },
)
