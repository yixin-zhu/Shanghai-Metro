# 2021冬
## Shanghai Metro 各文件功能与运行说明   
#### 朱奕新 19307090029
***

本次实验使用Python语言，实现了Bellman-Ford 与 Dijkstra两种单源最短路径的图算法。您可以在实验报告“report.pdf”文件中快速阅读关键部分的核心代码，或在源代码中阅读两种算法的完整实现。

report.pdf 文件是本次PJ的实验报告，简要介绍了本PJ的设计思路，并列出了本次PJ的核心算法代码与关键实现细节，请您阅读。

本次程序分为普通版和UI版。普通版直接把结果打印在控制台；UI版则用一个UI界面与用户互动。两个版本核心算法思想与实现并没有本质不同，仅仅是函数返回结果的形式有差异。
***

### 编译运行环境

Windows 10

Python 3.9.1


### 编程语言

Python 

### 使用说明

#### 普通版

1. 保存此文件夹，并在命令行下打开“普通版”文件夹。

2. 输入`python bellmanford.py`命令或者`python dijkstra.py`命令来编译运行。

3. 现在，您需要输入一行站名，每个站名之间用空格分隔。如同performance-testbench.txt中的一行那样。

4. 按下回车键。程序将会在时间最短的路径中挑选一条换乘次数最少的路径给您。

5. 稍等几秒，您可以在控制台观看程序给出的路径、预计需求时间与预计换乘次数。输出格式类似于out.txt中的样子。


#### UI版

1. 保存此文件夹，并在命令行下打开“UI 版”文件夹。

2. 输入`python UI.py`命令来编译运行UI文件。会弹出一个与用户互动的UI面板。

3. 在输入框中输入一行站名，每个站名之间用空格分隔。如同performance-testbench.txt中的一行那样。

4. 挑选您想要用于导航的算法，按下上方两个按钮中的一个。

5. 稍等几秒，您可以在下方text框中观看程序给出的路径、预计需求时间与预计换乘次数。输出格式类似于out.txt中的样子。

***
全部代码在笔者的电脑上测试通过，如果在您的设备上出现意料之外的错误，请联系电话：18358425535
