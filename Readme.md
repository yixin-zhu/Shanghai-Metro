# 2021秋数据结构   
## PROJECT2各文件功能与运行说明   
#### 朱奕新 19307090029
***

本次实验使用Python语言，实现了单源最短路径的图算法。您可以在实验报告“report.pdf”文件中快速阅读关键部分的核心代码，或在源代码中阅读两种算法的完整实现。

report.pdf 文件是本次lab的实验报告，简要介绍了本PJ的设计思路，并列出了本次Lab的核心算法代码与关键实现细节，请您阅读。

本次程序分为普通版和UI版。普通版直接把结果打印在控制台；UI版则用一个UI界面与用户互动。
***

### 编译运行环境

Windows 10

Python 3.9.1


### 编程语言

Python 

### 使用说明

#### 普通版

1. 保存此文件夹，并在命令行下打开“普通版”文件夹。

2. 输入`python bellmanford.py`命令或者来编译运行。

3. 现在，您需要输入一行站名，每个站名之间用空格分隔。

4. 稍等几秒，您可以在控制台观看。


#### UI版

1. 保存此文件夹，并在命令行下打开所要测试的树的文件夹。

2. 输入`python UI.py`命令来编译运行UI文件。

3. 下面并列的三个方框用来输入参数，如只有一个参数，比如文件操作、search、delete等，请把参数写在第一个框中；如有三个参数，比如update、insert等，请从左至右填写key、part、frequency参数。上方八个按钮分别是用户可进行的八个操作，按下即可执行。

4. 在下方的text方框中，您可以观看每一步的操作中程序反馈的输出结果。

***
全部代码在笔者的电脑上测试通过，如果在您的设备上出现意料之外的错误，请联系电话：18358425535