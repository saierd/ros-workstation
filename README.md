This package provides a set of desktop files for common ROS tools and a mime type for `.launch` files. It should work with Ubuntu and most ROS versions.

It is a fork of [this repository for ROS Hydro](https://github.com/TurtleBot-Mfg/ros-system-workstation-hydro). Credit belongs to them, I only changed the shortcuts to work with other ROS versions.

## Install

Install everything by executing

```shell
sudo python setup.py install --record record.txt
sudo update-mime-database /usr/share/mime
```

## Uninstall

The command above saves a list of installed files to the file `record.txt`. As long as you keep this file you can uninstall all the shortcuts with

```shell
cat record.txt | sudo xargs rm -rf
```

## PR2 Shortcuts

If you want to install shortcuts for the PR2 robot you can modify the following line in `setup.py` before installing:

```python
install_pr2 = True
```



