# Lab 6：Linux Kernel中的沟通实践（8分）

**截止日期：2025.11.19 11:59am**

## 实践目的

通过阅读顶级开源项目的开发文档，结合自己迄今为止的开源开发经验，体会开源开发中沟通与协作的最佳实践。

## 实践流程

**前两个问题二选一回答即可

> （4分）阅读Linux Kernel中的沟通与协作的实践相关资料（参见末尾），对于下面几个沟通的例子，依次回答：这个例子是否有违反Linux Kernel的沟通最佳实践（即Linux官方文档中定义的沟通要求）？如果有，在这一场景下应该怎么做？为什么需要这么做？
>
>    1. "This limitation should be explained in the cover letter and changelog." (Patch #759033)
>    2. "Commit e21d2170f36602ae2708 (“video: remove unnecessary platform_set_drvdata()”) removed the unnecessary platform_set_drvdata(), but left the variable “dev” unused, delete it." ([Patch #2833310](https://patchwork.kernel.org/project/linux-fbdev/patch/51F0F88D.8060903@cn.fujitsu.com/))
>    3. "This adds a device tree definition file for LEGO MINDSTORMS EV3." ([Patch #728065](https://patchwork.kernel.org/project/linux-arm-kernel/patch/1484253167-27568-1-git-send-email-david@lechnology.com/)) 
>
> 解释的时候请一并附上Linux官方文档中的有关内容（关于沟通的要求）。

（在这里写下你的回答）

> （4分）选择一个你感兴趣的开源项目，选择三个沟通的例子，依次对每个例子回答：
这个例子是否违反了这个项目（文档定义的）沟通最佳实践，或者一般意义上的开源项目沟通最佳实践？如果有，在这一场景下应该怎么做？为什么需要这么做？
或者，这个例子是否有你认为做的很好的地方？如果有，为什么？
请一并列出你的回答涉及的例子的链接。

（在这里写下你的回答）

> （4分）你迄今为止与开源社区做的沟通交流中，有哪些做的符合你认为的最佳实践的地方？有哪些做的不太合适，可以改进的地方？请提供你的沟通交流的相关链接，结合实际例子总结。

（在这里写下你的回答）
注意，由于目前仅是学期中进度，可能有部分同学的课程项目**尚未展开**有效沟通，此部分**可以留空**，在**12月3日11:59am**之前随时可以补充提交这部分内容，如果补充提交，请将文件命名为`学号-姓名-Lab6（补充）.md`；如在本次Lab提交中有明确说明，之后的补充提交仍然按照100%的比例给分，否则视作本次提交一并回答，后续不再接受补交。

## 提交方式

请在截止日期之前，将此markdown文件（请检查前面的问题是不是已经都回答了）发送到助教邮箱（hzye@stu.pku.edu.cn），文件命名统一为`学号-姓名-Lab6.md`。

## 评分标准

对实践流程中提出的所有问题，均有合理的回答即得满分，否则酌情扣分。

提交超出截止日期24小时内，最多获得80%的分数；提交超出截止日期48小时内，最多获得50%的分数；超出截止日期48小时的提交不得分。

## 参考资料

* https://www.kernel.org/doc/html/latest/process/howto.html
* https://www.kernel.org/doc/html/latest/process/management-style.html#managementstyle
* https://www.kernel.org/doc/html/latest/process/submitting-patches.html#submittingpatches
* https://www.kernel.org/doc/html/latest/process/development-process.html
* Tan, Xin, and Minghui Zhou. "How to communicate when submitting patches: An empirical study of the Linux kernel." Proceedings of the ACM on Human-Computer Interaction 3.CSCW (2019): 1-26. https://dl.acm.org/doi/abs/10.1145/3359210
