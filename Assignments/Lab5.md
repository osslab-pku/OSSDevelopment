# Lab 5：Python开源软件包安装/管理/打包/上载（10分）

**截止日期：2025.12.17 11:59am**

## 实践目的

* 以Python为例，了解对软件项目进行依赖管理、打包、和发布的基本流程

## 初始文件

请基于你的Lab 4，继续完成本次Lab

## 实践流程

1. 在`pyproject.toml`中修改`tool.poetry.name`为`pygraph-{姓名拼音}`（例如，`pygraph-zhangsan`），这将是上传到TestPyPI的包名，不能与已有包冲突。

2. 在`pyproject.toml`中配置需要打包的文件为`pygraph.py`，这需要用到[tool.poetry.packages](https://python-poetry.org/docs/pyproject/#packages)选项。

3. 修改后，使用`poetry update`更新项目配置。

4. 使用Poetry打包`pygraph-xxxx`：

    ```shell script
    poetry build
    ```

    上述命令会在`dist/`文件夹中生成wheel文件和源代码tar包，这些是在PyPI上发布所必须的文件。

5. 在[TestPyPI](https://test.pypi.org/)注册一个账号，请注意不要在[PyPI](https://pypi.org)上直接注册。

    > [TestPyPI](https://test.pypi.org)是与PyPI分离的Python包发布平台，主要用于学习和测试，不影响真正的Python生态。TestPyPI要求[Two factor authentication (2FA)验证](https://test.pypi.org/help/#twofa)，可以使用[Gauth](https://chromewebstore.google.com/detail/gauth-authenticator/ilgcnhelpchnceeipipijaljkblbcobl?hl=zh-CN&utm_source=ext_sidebar)完成验证。

6. 在`pyproject.toml`中添加[Twine](https://twine.readthedocs.io/en/stable/)作为开发依赖，并使用`poetry install`安装Twine。

    > [Python官方文档](https://packaging.python.org/en/latest/key_projects/#twine): Twine is the primary tool developers use to upload packages to the Python Package Index or other Python package indexes. It is a command-line program that passes program files and metadata to a web API. Developers use it because it’s the official PyPI upload tool, it’s fast and secure, it’s maintained, and it reliably works.

7. 使用Twine在TestPyPI上手动发布`pygraph-xxxx`：

    ```shell script
    twine upload --repository testpypi dist/*
    ```
    > 注意，PyPi 调整了安全策略，不再允许启用两步验证的账号使用用户名密码来上传项目了，必须使用 API 令牌来进行身份验证。登录 PyPi ，进入账户设置页，点击「添加 API 令牌」按钮创建 API 令牌。然后修改 ~/.pypirc 配置文件， 用户名字段改为__token__ ，密码字段改为刚才创建的令牌，运行上述命令即可完成上传。也可通过-u以及-p传入用户名及密码。
    
    此时就可以在TestPyPI上查看你的软件包了（例如[pygraph-zhangsan](https://test.pypi.org/project/pygraph-zhangsan/0.1.0/)）。

    可以尝试退出poetry shell，在一个新的Python环境中运行类似如下命令以安装你的软件包：

    ```shell script
    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pygraph-zhangsan
    ```

    这里`--extra-index-url`是为了确保pygraph可以安装从PyPI上来的间接依赖。

    然后，在Python解释器中可以尝试导入pygraph包，类似如下：

    ```
    PS D:\GitHub\OSSDevelopment> pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pygraph-zhangsan
    Looking in indexes: https://test.pypi.org/simple/, https://pypi.org/simple/
    Collecting pygraph-zhangsan
    Downloading https://test-files.pythonhosted.org/packages/97/fe/0818386b03b062e7d217acbdfc20c5f1bd6cc455c06e07463f5a86da8fc1/pygraph_zhangsan-0.1.0-py3-none-any.whl.metadata (276 bytes)
    Downloading https://test-files.pythonhosted.org/packages/97/fe/0818386b03b062e7d217acbdfc20c5f1bd6cc455c06e07463f5a86da8fc1/pygraph_zhangsan-0.1.0-py3-none-any.whl (1.8 kB)
    Installing collected packages: pygraph-zhangsan
    Successfully installed pygraph-zhangsan-0.1.0
    PS D:\GitHub\OSSDevelopment> python
    Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32      
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import pygraph
    >>> g = pygraph.Graph([(1,2),(3,4)])
    >>> g
    Graph({1: {2}, 2: {1}, 3: {4}, 4: {3}})
    ```

    但是，像这样在本地手动发布Python包对于团队协作开发的开源项目而言，不是最佳实践。比较好的做法是在GitHub上配置CD流水线，在master分支上达成特定条件（例如使用tag标记的版本）时，自动发布到PyPI。接下来的操作将会达成这一点。

8. 借助[networkx](https://networkx.org/documentation/stable/index.html)（可以使用[`poetry add`](https://python-poetry.org/docs/cli/#add)命令添加新依赖），为pygraph实现计算最短路径的功能，并通过测试。在开发完成后，将`pyproject.toml`中的版本号修改为`0.2.0`。

    > 也许这里封装networkx显得很蠢，不过在实际编程中，由于图数据结构无处不在（常常蕴含在其他复杂结构化数据里），经常会有将当前的数据转换格式并应用已有图算法的情况。

9. 你的GitHub仓库内[配置TestPyPI的TOKEN为Secret](https://help.github.com/en/actions/automating-your-workflow-with-github-actions/creating-and-using-encrypted-secrets)。

10. 添加一个新的GitHub Action流水线，使得若你的仓库[在GitHub上创建了一个新release](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#release)，流水线将会构建、测试、打包pygraph并发布到TestPyPI。

11. 将所有更改完成后，push到GitHub，在GitHub上创建一个新的Release，检查自动发布是否生效。

    > 如果配置错误，可修改后重新发布release，测试流水线是否有效

12. 可以尝试仿照步骤7，在TestPyPI安装你的包并调用代码，测试发布是否有效。

## 评分标准

- （3分）TestPyPI上有通过步骤1-7发布的Python包。
- （3分）pygraph实现了计算最短路径的功能并包含可通过的测试样例。
- （4分）配置了能够自动发布Python包的GitHub Action流水线。

## 提交方式

Lab 5无需特意提交任何内容，助教会在DDL后检查[OSS-Dev-Course-PKU](https://github.com/OSS-Dev-Course-PKU)中检查相应仓库，以及所对应的TestPyPI包，做出最终评分。
