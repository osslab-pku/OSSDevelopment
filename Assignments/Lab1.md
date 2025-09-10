# Lab 1：熟悉git和GitHub（7分）

**截止日期：基础部分 2024.9.17 11:59am; 扩展部分: 2025.9.24 11:59am**

## 实践目的

熟悉开源软件开发中常用的工具、平台、和开发流程；为课程学习确立初步计划和目标。

## 实践流程
### 基础部分
1. 如果你还没有GitHub账号，请注册一个GitHub账号。
2. 将GitHub账号以填写[表单](https://docs.qq.com/form/page/DUnd3eEdaYlpEREhp)形式发给助教，助教发送GitHub邀请到[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)组织，Lab 1、Lab 4和Lab5中涉及操作GitHub的部分均会在此进行；此外，后续的课程项目也会以此处告知的GitHub账号为准进行评分。
3. 在[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中创建一个GitHub仓库，名为`2025Fall-{学号}-Lab1`。
> 例如，如果学号为2200012345，那么仓库名应当为`2025Fall-2200012345-Lab1`。

4. 在自己的个人电脑上安装git，初始化一个git repository。
> 网上存在大量关于如何在Windows/Mac OS/Linux安装git、初始化git repository、和添加commit的教程，我们在此推荐[MIT的Git教程](https://missing.csail.mit.edu/2020/version-control/)和[Pro Git前五章](https://git-scm.com/book/en/v2)，也可自行搜索参考其他教程，在此不再赘述；除命令行外，VS Code等IDE也提供非常便捷的git操作GUI。

5. 在repository中创建README.md文件，在文件中描述自己目前对开源项目的贡献想法，为本学期的课程学习设定目标。

6. 在一个新的commit中添加README.md进入git仓库，这个commit的commit message应当为`Add README.md with my OSS contribution plan`。
> 为了保证软件项目的可维护性，特别是为了方便他人查看和理解一个项目的开发历史，commit message的最低要求通常是**能够简明扼要地总结这个commit所包含的变更**。对于大型项目而言，往往还会对commit message格式做出更加严格的要求，例如[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)，方便对commit进行自动化管理。

7. 将这个repository上传到[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中你创建的GitHub仓库。

### 扩展部分
8. （建议上过一周课程后再继续这一步）相比较于上一次，你的贡献想法和计划发生了什么变化？请在你创建的GitHub仓库中开启一个issue，用一句话描述贡献想法和计划的变化。
> 在真实的开源项目中，Issue和PR的内容通常会有规定的[模板](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates)，以便于维护者快速地处理新的Issue和PR；在本Lab中，因为相关的issue和PR过于trivial，故不对内容作任何要求；但是需要额外注意，如果在真实的开源项目中提交issue和PR，通常需要严格遵循其规定的贡献指南。之后的Lab中涉及到对成熟开源项目的贡献指南的观察和分析。

9. 将你创建的GitHub仓库fork到你自己的账号下，新建一个分支，并在新分支中添加一个或者多个新commit，将想法的变化更新在README.md中，随后回到[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中你创建的GitHub仓库，删除其中README.md的内容并提交删除commit。此时，在你创建的GitHub仓库中开启一个PR，将fork仓库中的新分支合并入[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中仓库的主分支main，解决存在的冲突，设置reviewer为助教，等待助教合并PR。
> 在Lab 1中，你有直接合并PR的权限；在真实的开源项目中，通常只有核心维护者具有PR合并权限，需要通过一轮或多轮[Code Review](https://en.wikipedia.org/wiki/Code_review)，才能合并PR里的变更；此外，开源项目在开发过程中通常会选择在不同的[分支](https://docs.github.com/zh/desktop/making-changes-in-a-branch/managing-branches-in-github-desktop)中同步完成不同的开发工作从而使得不同的开发互不影响，但在合并分支的过程中，如果仓库内的不同分支同时对相同文件进行了更改，通常会产生conflicts，此时需要人为进行检查[解决合并冲突](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)，才能合并以获取分支中的最新更改。

## 评分标准

- （1分）按要求创建了repository。
- （1分）Repository中有README.md，按要求书写了commit message。
- （1分）README.md有开源项目的贡献想法和计划。
- （1分）按要求open issue。
- （1分）按要求fork repository、新建分支并在fork仓库的新分支与原仓库的主分支中同时提交commit修改。
- （1分）按要求提交PR合并分支并解决产生的conflicts。
- （1分）贡献想法体现出了对开源项目的了解和自己的认真思考。

对于每一项评分标准，超过DDL的提交统一不得分。

## 提交方式

Lab 1无需特意提交任何内容，助教会在DDL后检查[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中是否存在相应仓库、README.md、fork/PR合并记录、和贡献想法，做出最终评分。

## 备注

1. Lab 1中所涉及的git操作相对基础，在真实的开源项目中可能会涉及到比较复杂的git操作（例如rebase/squash/submodule等）；因此，虽然Lab 1不对此作强制的评分要求，但是我们强烈建议，如果你对git仍不熟悉，可以自己过一遍[MIT的Git教程](https://missing.csail.mit.edu/2020/version-control/)并做一做附带的练习，以免在之后的课程项目中遭遇困难。
2. 若上述操作流程中存在误操作，或者需要修改贡献想法，自行重新提交即可，只要仓库历史上存在一个符合要求的commit、issue、fork、PR，即符合得分要求。
3. 在评分标准中，贡献想法的长度**不会**作为评分的参考，简明扼要即可；评分的最终解释权归助教所有。
4. 结课后，（大概率在明年开课前）助教可能会删除[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)创建的所有repository，如果有需要，请本地保存您提交的相关内容的备份
