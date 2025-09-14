# Lab 4：CI/CD流水线搭建（10分）

**截止日期：2025.11.19 11:59am**

## 实践目的

* 了解使用GitHub Action搭建CI/CD流水线的基本方法。
* 以Python为例，了解典型的软件项目应当具有的基本开发工具、框架和流程。

## 初始文件

[Lab4/](Lab4/)文件夹中是一个功能极简的用Python实现图数据结构的包`pygraph`，该项目目前采用[Poetry](https://python-poetry.org/)进行依赖管理，[pytest](https://docs.pytest.org/en/7.1.x/)作为测试框架，文件结构如下：

* `pygraph.py`实现图数据结构，包含一个类和一些简单函数，均未实现，且结构混乱。
* `pyproject.toml`是Poetry使用的依赖配置文件，文件中声明了本项目支持的Python版本（**仅支持Python 3.10**)，以及本Lab中需要的各种开发依赖。
* `tests/`文件夹包含若干测试。
* `pytest.ini`是`pytest`的配置文件。

Lab 4需要为这个项目配置开发环境，补全未实现的代码，并配置一个包含所有常见阶段的CI/CD流水线。

## 实践流程

1. 请在[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中创建一个**私有**GitHub仓库，名为`2025Fall-{学号}-Lab4`，为老师和助教添加访问权限，并将[Lab4/](Lab4/)文件夹中的所有文件push到仓库内（注意不是push文件夹本身）。

    > 不要设置为公开仓库或者为其他同学添加访问权限，否则此Lab评分作废；若误操作，请联系助教删除仓库

2. 将新创建的仓库clone到本地，配置Python开发环境，安装Poetry，使用Poetry配置虚拟环境，并安装所有依赖。

    ```shell script
    # 若Python和Poetry配置正确，用如下两行命令即可配置虚拟环境并安装所有依赖
    poetry shell
    poetry install
    ```

3. 使用[black](https://black.readthedocs.io/en/stable/)对代码进行重新格式化。

    ```shell script
    black .
    ```

4. 使用[pre-commit](https://pre-commit.com/)工具为项目添加Pre-Commit Hook，使得git能够在commit前，调用black对代码进行自动格式化。这需要涉及到编写一个`.pre-commit-config.yaml`文件，并运行`pre-commit install`命令。

    > 为项目配置统一、简洁的代码风格，是为了降低其他人阅读代码时的认知负荷，方便团队协作。这一流程可以利用现有工具高度自动化，不会为开发带来任何额外负担。

5. 修改`pygraph.py`文件，实现其中所有功能，保证运行如下命令可以通过所有测试，并生成测试覆盖率报告。

    ```shell script
    pytest -r P --cov=pygraph
    ```

    > 这里采用的开发范式是[测试驱动开发](https://en.wikipedia.org/wiki/Test-driven_development)（Test-Driven Development，TDD），先通过编写测试用例精准描述需求，再在测试用例的基础上实现代码。这一开发方式可以“倒逼”程序员思考代码实现的简洁性、灵活性和可测试性，有助于提升项目代码质量，在敏捷开发中经常使用。

    > 由于本Lab的核心要点并不在于代码实现，因此这里刻意使用了非常简单的代码。不过需要注意，Lab里涉及到的代码实践可适用于，且往往对于长期维护的大型软件项目不可或缺。我们强烈鼓励同学们在自己的其他项目中借鉴运用相关实践（对于各种技术栈，其内核都是相通的），提升整体的工程水平。

6. 使用[pdoc3](https://pdoc3.github.io/pdoc/)为`pygraph`自动生成API文档，可以在`html/`文件夹中查看生成的API文档。

    ```shell script
    pdoc --html pygraph
    ```

7. 使用GitHub Action配置五阶段CI/CD流水线，包含如下步骤：

    * 初始化Python环境，安装Poetry；
    * 使用Poetry自动安装所有依赖；
    * 使用black检测代码是否存在格式问题；
    * 使用pytest运行单元测试；
    * 使用pdoc3生成API文档，并将API文档部署到仓库中的`gh-page`分支。

    > 对于公有仓库，可以配置GitHub读取`gh-page`分支，在github.io直接提供相应的公开可访问的网页，这样便实现了API文档的持续部署（对于软件包本身的持续部署，我们留到Lab 5再实现）。
    >
    > 不过非常遗憾的是，私有仓库的GitHub Page是收费功能。如果同学们以后创建自己的项目，可以尝试用同样的方法自动部署各种网页，确认实际效果。

    > 需要注意CI环境里是不能使用`poetry shell`的（[相关讨论](https://github.com/python-poetry/poetry/discussions/3526)）。

8. 将所有更改体现在GitHub仓库中;

9. 撰写一份简要的实验报告，记录你的流水线搭建过程及最后搭建成功的pipeline输出结果，并简要总结心得体会。（注意：报告长度不作为评分标准，无严格格式要求，能清晰展示解决了哪些问题、实现了哪些任务即可）

## 提交前检查

在提交前，请确保在一台安装了Python和Poetry的机器上，能够依次运行如下命令并正常输出结果

```shell script
poetry shell              # activate a working virtual environment
poetry install            # install all dependencies
pre-commit install        # install pre-commit hooks
black .                   # lint all Python code
pytest -r P --cov=pygraph # run all tests with test stdout and coverage report
pdoc --html pygraph       # build API documentation and deploy to html/
``` 

> 对于所有需要给别人使用的代码，确保其他人能够轻松地按照开发文档，配置能够运行你的代码的标准化的开发环境，是至关重要的。Python生态里的大量工具链都是为了能够做到这一点。

此外，请确保你的GitHub仓库里，GitHub Action包含了所有要求的流水线阶段，且能不报错正常执行（有小绿勾）。

> 助教会人工检查流水线配置是否正确。需要尤其注意的是，`black`在默认配置下，即使存在代码格式问题，也只会重新格式化而不会报错，这对于CI流水线中的检查是不合适的（CI环境下重新格式化了也没用）。因此，需要通过相应配置选项让`black`检查是否存在风格错误。

## 评分标准

- （2分）所有测试能够通过。
- （2分）配置了能够自动格式化代码的Pre-Commit Hook。
- （5分）配置了至少包含如下五个阶段的GitHub Action流水线：初始化Python环境、安装依赖、代码风格检查、运行单元测试、部署API文档。
- （1分）实验报告清晰准确记录了相关实践过程

## 提交方式

在DDL前将PDF版本的实验报告发送至助教邮箱（hzye@stu.pku.edu.cn），命名为“25Fall-(姓名)-Lab4Report”；同时，助教会在DDL后检查[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中检查相应仓库，综合做出最终评分。

## 参考资料

1. [Poetry文档](https://python-poetry.org/docs/)
2. [pytest文档](https://docs.pytest.org/en/7.1.x/getting-started.html)
3. [pytest测试里用到的fixture功能](https://docs.pytest.org/en/6.2.x/fixture.html)
4. [black文档](https://black.readthedocs.io/en/stable/)
5. [pre-commit文档](https://pre-commit.com/)
6. [pdoc3文档](https://pdoc3.github.io/pdoc/)
7. [GitHub Action文档](https://docs.github.com/en/actions)，[基本概念](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)，[测试&构建Python项目](https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions)
8. 可能有用的GitHub Action插件：
     1. https://black.readthedocs.io/en/stable/integrations/github_actions.html
     2. https://github.com/actions/setup-python
     3. https://github.com/marketplace/actions/deploy-to-github-pages
