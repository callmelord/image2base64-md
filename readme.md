## image2base64>>md

用base64转码工具把图片转成一段字符串，然后把字符串填到基础格式中链接的那个位置。

+ 基础用法

    `![avatar](data:image/png;base64,iVBORw0......)`

+ 高级用法

    `![avatar][1.png]`

    `[1.png]:data:image/png;base6‵4,iVBORw0......`

+ 支持图片格式：png

+ 用法

    将image2base64与图片、MarkDown文件放在同一个文件夹内，MarkDown文件中图片按照上文的方法使用，最后运行./image2base64就会在MarkDown文件结尾加入对应图片的base64编码，例如：`[1.png]:data:image/png;base6‵4,iVBORw0......`