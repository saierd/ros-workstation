from distutils.core import setup

install_pr2 = False

files_to_install = [('/usr/share/applications', ["desktop-files/ros-rqt_console.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_graph.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_image_view.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_logger_level.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_msg.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_plot.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-rviz.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-roscore.desktop"]),
                    ('/usr/share/applications', ["desktop-files/ros-roslaunch.desktop"]),
                    ('/usr/share/mime-info', ["mime-types/ros-roslaunch.mime"]),
                    ('/usr/share/mime/packages', ["mime-types/ros-roslaunch.xml"]),
                    ('/usr/share/applications', ["desktop-files/ros-rqt_bag.desktop"]),
                    ('/usr/share/mime-info', ["mime-types/ros-rqt_bag.mime"]),
                    ('/usr/share/mime/packages', ["mime-types/ros-rqt_bag.xml"]),
                    ('/usr/share/desktop-directories', ["Robotics.directory"]),
                    ('/usr/share/icons/hicolor/scalable/apps',["icons/application-x-ros-launch.svg"]),
                    ('/usr/share/icons/hicolor/scalable/apps',["icons/application-x-ros-bag.svg"]),
                    ('/usr/share/icons/hicolor/scalable/apps',["icons/ros-rviz.svg"]),
                    ('/usr/share/icons/hicolor/scalable/apps',["icons/ros-rqt.svg"]),
                    ('/usr/share/icons/hicolor/scalable/apps',["icons/ros-tool.svg"])
                   ]

if install_pr2:
    files_to_install.extend([('/usr/share/applications', ["ros-rqt_pr2_dashboard.desktop"]),
                             ('/usr/share/applications', ["ros-pr2_simulation.desktop"])
                            ])

setup(name = "ros-workstation",
    version = "0.0.1",
    description = "ROS Workstation",
    author = "I Heart Engineering, Daniel Saier",
    author_email = "code@iheartengineering.com, mail@danielsaier.de",
    url = "https://github.com/saierd/ros-workstation",
    license = "BSD-3-clause",
    data_files = files_to_install,
    long_description = "Desktop Shortcuts for ROS tools."
)

