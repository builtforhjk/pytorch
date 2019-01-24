- 打开`终端`, 输入
  ```
  python
  ```
  如果显示版本为2.7.x即可。
- 输入
  ```
  sudo easy_install pip
  ```
  会让你输入你自己电脑的密码，输入密码的时候不会显示出来。然后等待安装pip完成。pip是python的一个工具包知道是用来下载东西的就可以了。
- 安装pip完成后输入
  ```
  pip -V
  ```
  查看pip版本，对应python2.7，如果正常显示就说明pip安装成功。
- pip安装后就利用pip下载程序需要的扩展包，该程序需要PIL，matplotlib，pytorch等
  输入
  ```
  sudo pip install Pillow
  sudo pip install matplotlib
  sudo pip install torch torchvision
  sudo pip install ipython
  sudo pip install jupyter
  ```
  如果提示输入密码继续输入即可。每次输入都会安装一个，等待一段时间再输入下一个。
- 安装后检验是否成功。输入
  ```
  python
  ```
  启动python2
  ```
  import PIL
  import matplotlib.pyplot
  import torch
  import torchvision
  ```
  如果没有报错`error`即安装完成。
- 输入
  ```
  jupyter notebook
  ```
  浏览器会弹出页面，找到该程序所在位置，打开即可。
