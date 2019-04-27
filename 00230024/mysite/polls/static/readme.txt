静态文件命名空间

虽然我们 可以 像管理模板文件一样，把 static 文件直接放入 polls/static
——而不是创建另一个名为 polls 的子文件夹，不过这实际上是一个很蠢的做法。
Django 只会使用第一个找到的静态文件。如果你在 其它 应用中有一个相同名字的
静态文件，Django 将无法区分它们。我们需要指引 Django 选择正确的静态文件，
而最简单的方式就是把它们放入各自的 命名空间 。
也就是把这些静态文件放入 另一个 与应用名相同的目录中。


在刚创建的 polls/static 文件夹中创建一个名为 polls 的文件夹，
再在 polls 文件夹中创建一个名为 style.css 的文件。
换句话说，你的样式表路径应是 polls/static/polls/style.css。
因为 AppDirectoriesFinder 的存在，你可以在 Django 中
简单地使用以 polls/style.css 的形式引用此文件!!!类似你引用模板路径的方式。