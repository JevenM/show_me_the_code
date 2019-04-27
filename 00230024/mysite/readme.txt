官网教程
https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial02/



创建项目
django-admin startproject mysite

启动项目
py manage.py runserver 8080

创建应用
py manage.py startapp polls

使用数据库之前先执行
python manage.py migrate
（这个 migrate 命令检查 INSTALLED_APPS 设置，
为其中的每个应用创建需要的数据表，至于具体会创建什么，
这取决于你的 mysite/settings.py
设置文件和每个应用的数据库迁移文件）

将应用路径添加到INSTALLED_APP中，之后执行
python manage.py makemigrations polls
（通过运行 makemigrations 命令，Django 会检测你对模型文件的修改
（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移）

我们看看迁移命令会执行哪些 SQL 语句。sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：
python manage.py sqlmigrate polls 0001

运行
python manage.py check
这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作

【
现在，你只需要记住，改变模型需要这三步：

编辑 models.py 文件，改变模型。
运行 python manage.py makemigrations 为模型的改变生成迁移文件。
运行 python manage.py migrate 来应用数据库迁移。
】

创建一个能登录管理页面的用户
py manage.py createsuperuser




mysite是一个项目
polls是项目中的一个应用

