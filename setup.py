from distutils.core import setup
import os
import subprocess

"""
if os.path.exists("debian/changelog"):
    output=subprocess.check_output("parsechangelog | grep Version", shell=True)
    version = output.split(":")[1].strip()
"""

setup(name = "ros-system-workstation",
    #version = version,
    version = "0.0.1",
    description = "ROS Workstation",
    author = "I Heart Engineering",
    author_email = "code@iheartengineering.com",
    url = "http://www.iheartengineering.com",
    license = "BSD-3-clause",
    data_files=[('/usr/share/applications', ["ros-rqt_reconfigure.desktop"]),
                ('/usr/share/applications', ["ros-rqt_console.desktop"]),
                ('/usr/share/applications', ["ros-rqt_graph.desktop"]),
                ('/usr/share/applications', ["ros-rqt_image_view.desktop"]),
                ('/usr/share/applications', ["ros-rqt_launch.desktop"]),
                ('/usr/share/applications', ["ros-rqt_logger_level.desktop"]),
                ('/usr/share/applications', ["ros-rqt_msg.desktop"]),
                ('/usr/share/applications', ["ros-rqt_plot.desktop"]),
                ('/usr/share/applications', ["ros-rqt_top.desktop"]),
                ('/usr/share/applications', ["ros-gazebo.desktop"]),
                ('/usr/share/applications', ["ros-rviz.desktop"]),
                ('/usr/share/applications', ["ros-group.desktop"]),
#                ('/usr/share/applications', ["ros-network-id.desktop"]),
                ('/usr/share/applications', ["ros-roscore.desktop"]),
                ('/usr/share/applications', ["ros-roslaunch.desktop"]),
                ('/usr/share/mime-info', ["ros-roslaunch.mime"]),
                ('/usr/share/mime/packages', ["ros-roslaunch.xml"]),
                ('/usr/share/applications', ["ros-rqt_bag.desktop"]),
                ('/usr/share/mime-info', ["ros-rqt_bag.mime"]),
                ('/usr/share/mime/packages', ["ros-rqt_bag.xml"]),
                ('/usr/share/desktop-directories', ["Robotics.directory"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/application-x-ros-launch.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/application-x-ros-bag.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-rviz.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-rqt.svg"]),
                ('/usr/share/icons/hicolor/scalable/apps',["pixmaps/ros-tool.svg"]),
               ],
    long_description = """ROS Workstation Environment""" 
    #classifiers = []     
) 
