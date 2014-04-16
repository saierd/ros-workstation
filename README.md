These are system level files to support ROS Fuerte workstations. Only tested in Cinnamon, but should work decently in Unity and others as well. The package provides a set of desktop files for common ROS tools and a mime type for `.launch` files.

This is a fork from [TurtleBot-Mfg's hydro repository](https://github.com/TurtleBot-Mfg/ros-system-workstation-hydro). Credit belongs to him, I only changed the paths and deleted stuff that didn't work with Fuerte.

# Installation

Install by executing

```shell
sudo python setup.py install --record record.txt
sudo update-mime-database /usr/share/mime
```

This saves a list of installed files to the file `record.txt`. As long as you keep this file you can uninstall everything with

```shell
cat record.txt | sudo xargs rm -rf
```

