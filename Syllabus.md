
# 2022年秋冬学期——课程大纲 (subject to change)

**主要内容： 开源开发方法、技术和实践OSP + 开源文化OSC + 上机实习lab  + 课程项目PRJ**

授课教师：周明辉 zhmh@pku.edu.cn     
助教：    何昊 heh@pku.edu.cn      

## 第1次课：开源软件及其开发概述（课堂lecture）  09/07  

* 100课程简介：课程的目的和内容，以及课程的考核形式。  **lecture100**    
* 101开源软件概述：开源的定义、历史和现状、社区结构和治理，以及开源研究。 **lecture101**  
* 102开源参与概述：怎么参与开源项目和社区（如果时间允许，课堂上访问github/gitee/gitlink，设立平台账号，了解一个开源项目）。**lecture102** 

> **Lab 1：练习使用git和GitHub（7分）**
>  - 注册GitHub账号
>  - 加入课程的[Organization](https://github.com/OSS-Dev-Course-PKU)
>  - 创建GitHub仓库并添加commit，于README.md写下目前的开源项目贡献想法
> 
> Lab 1详细要求参见[WriteUp](Assignments/Lab1.md)，**截止日期：2022.09.28 11:59am**

## 第2次课：开源开发的支持平台和关键技术：熟悉开源平台和Git操作（课堂lecture） 09/14      
  
* 201：Git实践入门  
  - 了解版本控制，了解使用Git，https://missing.csail.mit.edu/2020/version-control/   
* 202：GitHub实践入门    
  - 了解如何用开源协作工具，熟悉Github/Gitee/GitLink--建立账号和代码仓库，浏览和fork项目

> **Lab 1扩展：练习使用issue、fork和PR**
>  - 提交一个issue，描述自己的想法（相比较于第一次提交）做出了哪些变化
>  - 将仓库fork到自己的账号下，对README.md做出相应修改并提出一个PR
>
> Lab 1详细要求参见[WriteUp](Assignments/Lab1.md)，**截止日期：2022.09.28 11:59am**

## 第3次课：开源贡献指南（课堂lecture） 09/21   

* 301：开源贡献指南：  
  - learn how the open source community works;    
  - criteria to select open source project and task to participate in.  
  - 以1~2个GitHub项目/任务为例，展示如何做贡献（消除畏惧感）.

> **Lab 2：了解开源项目的开发方式和贡献流程（7分）**
> 
> 任意选择一个活跃、成熟的开源项目：
> - 了解并报告CONTRIBUTING.md的形式和内容
> - 回答有关其贡献流程、质量管理方式等若干问题
>
> Lab 2详细要求参见[WriteUp](Assignments/Lab2.md)，**截止日期：2022.10.12 11:59am**

## 第4次课：开源项目maintainer分享其维护/开发的经验。（多个项目，为开源任务选择做准备&提供依据）  	 09/28

* 开源项目的分享：项目介绍、技术介绍、项目常用规则、如何参与。    

## 第5次课：如何选择任务参与，GitHub Good First Issue（课堂lecture）  10/12   

> **Lab 3：在开源项目中选择开发任务（8分）** 
> 
> - 选择一个或者多个感兴趣的开源项目，探索并报告：
>   * 是否具有Good First Issue机制
>   * 如果你需要在其中选择开发任务，你会如何做
> - 参考以下几个Good First Issue推荐网站，报告其使用体验，对比其优缺点
>   * [GFI-Bot](https://gfibot.io)
>   * [GitHub Good First Issue](https://github.com/topics/good-first-issue)
>   * [good-first-issue.dev](https://goodfirstissue.dev/)
> 
> Lab 3详细要求参见[WriteUp](Assignments/Lab3.md)，**截止日期：2022.10.26 11:59am**


## 第6次课：（课程项目开题报告）选择开源项目和开源任务  10/19

* 学生报告，如何根据criteria to select open source project and task来进行开源任务的选择

## 第7次课：CI/CD（上机实习） 10/26
 
> **Lab 4：CI/CD流水线搭建（10分）** 
> 
> 了解三种CI流程管理工具Travis CI、GitHub Actions、Gitee Go, 知道如何使用这些工具编写简单的CI流水线，并且在实践项目上完成符合要求的成功构建
>
> Lab 4详细要求参见[WriteUp](Assignments/Lab4.md)，**截止日期：2022.11.9 11:59am**
>
> 4Fun: 2021课程实习过程中关于gitee go的建议：https://toscode.gitee.com/pitcher/gitee-go-exercise/issues  


## 第8次课：闭源与开源软工的异同（课堂lecture）11/2



## 第9次课：PyPI/NPM等包生态系统/包管理工具，使用/打包/上载软件包（上机实习） 11/9

> **Lab 5：Python开源软件包安装/管理/打包/上载（10分）**
>
> - 使用pip进行python包的管理；
> - 使用poetry进行python包的管理；
> - 配置自己的python包，包括配置setup.py、setup.cfg和pyproject.toml；
> - 熟悉Python包生态系统平台PyPI，并且通过setuptools、wheel和build三种方式将自己的python包发布到testpypi平台上（注意，不是pypi平台。Testpypi https://test.pypi.org 是与PyPI分离的python包发布平台，使练习时发布的python包不会影响到真正的生态）
>
> Lab 5详细要求参见[WriteUp](Assignments/Lab5.md)，**截止日期：2022.11.30 11:59am**

## 第10次课：开源社区及开源文化，与开源布道师面对面 11/16



## 第11次课：（课程项目进度报告）任务选择/合作反馈/工具使用等 PRJ-2  11/23



## 第12次课：开源开发中的沟通实践 11/30   

* 协作和沟通的重要性，如何沟通，分布式沟通中的要点，如何提交PR等。

> **Lab 6：Linux Kernel沟通实践（8分）**
>
> 阅读Linux Kernel中的沟通实践相关资料，体会总结开源沟通的最佳实践（8分）
>
> - 提交issue时如何参与讨论，如何沟通
> - 提交pr时如何沟通
>
> Lab 6详细要求参见[WriteUp](Assignments/Lab6.md)，**截止日期：2022.12.14 11:59am**

## 第13次课：开源开发和生态相关的挑战和研究（课堂lecture） 12/7

* 开源软件供应链
* 开源生态

## 第14次课：开源治理与社区运营	  12/14  

* 开源基金会，开源与法律，开源商业化机制
* 社区运营，例如孵化社区的渠道，如何做meetup和宣传等

## 第15次课：课程项目结题报告 PRJ-3 12/21  （12/26停课复习）

> 最后一次课之后需要提交课程项目最终报告（LaTeX格式），**截止日期：2023.01.04 11:59am**
>
> 课程项目的详细要求参见[WriteUp](Assignments/Project.md)

## 评分标准

* 课堂表现（10分）：  
    - 上课参与讨论、提问，若点名未到且未事先请假，一次扣2分，最多10分
    - 课堂表现优秀者，视情况酌情加分  
*	上机实习Lab（6个，共50分）：  
    - Git/贡献指南/GFI/沟通，7~8分一个，共30分  
    - CI/CD和包管理，10分一个，共20分  
*	课程项目PRJ（40分）：  
    - 3次presentation（开题/中期/结题），每次5分  
    - 期末报告10分  
    - 最后的贡献结果15分  
