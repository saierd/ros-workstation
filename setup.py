from distutils.core import setup

install_pr2 = False

desktop_files = ["ros-rqt_console.desktop",
                 "ros-rqt_graph.desktop",
                 "ros-rqt_image_view.desktop",
                 "ros-rqt_logger_level.desktop",
                 "ros-rqt_msg.desktop",
                 "ros-rqt_plot.desktop",
                 "ros-rviz.desktop",
                 "ros-roscore.desktop",
                 "ros-roslaunch.desktop",
                 "ros-rqt_bag.desktop"
                ]

if install_pr2:
    desktop_files.extend(["ros-rqt_pr2_dashboard.desktop",
                          "ros-pr2_simulation.desktop"
                         ])

mime_types = ["ros-roslaunch",
              "ros-rqt_bag"
             ]

icons = ["application-x-ros-launch.svg",
         "application-x-ros-bag.svg",
         "ros-rviz.svg",
         "ros-rqt.svg",
         "ros-tool.svg"
        ]


files_to_install = []

for f in desktop_files:
    files_to_install.append(("/usr/share/applications", ["desktop-files/" + f]))
    
for m in mime_types:
    files_to_install.append(("/usr/share/mime-info", ["mime-types/" + m + ".mime"]))
    files_to_install.append(("/usr/share/mime/packages", ["mime-types/" + m + ".xml"]))

for f in icons:
    files_to_install.append(("/usr/share/icons/hicolor/scalable/apps", ["icons/" + f]))

files_to_install.append(('/usr/share/desktop-directories', ["Robotics.directory"]))


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

