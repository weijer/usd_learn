# 获取USD

USD是一个令人惊叹的技术栈，但不幸的是，这也是它很难入门的原因。它是一套库和工具，它们都是构成USD的更大生态系统的一部分。虽然第三方工具越来越好，但仅仅“获取USD”就可能是相当具有挑战性的。

皮克斯动画工作室在 [GitHub上提供源代码](https://github.com/PixarAnimationStudios/USD)，对于开发人员来说，这通常是入门的第一步。他们会克隆存储库，引导正确版本的Python和他们最喜欢的C + +编译器，然后花很长时间喝咖啡，为他们的系统构建所有的工具和库。

只是说，这种方法并不是每个人都会采用的。幸运的是，它也不是开始使用USD的唯一方法。

作为一个新手，一般来说有两种获取和使用USD的方法。

> 在宿主应用程序中
> 
> 主机应用程序是选择将USD嵌入其工具集或完全基于USD构建的第三方软件。
> 
> 以下是一小部分最著名的这类应用：
> 
> . [NVIDIA Omniverse Create](https://www.nvidia.com/en-us/omniverse/apps/create/)——基于[NVIDIA's Omniverse](https://www.nvidia.com/en-us/omniverse)构建的功能强大的USD装配软件，它可以使您非常流畅地使用原生USD
> 
> . [Autodesk Maya + MayaUsd](https://www.autodesk.com/products/maya)——专业的3D软件，Maya USD集成是可以在安装过程中安装的附加组件
> 
> . [SideFx Houdini + Solaris](https://www.sidefx.com/products/houdini/solaris/)——专业的3D软件，内置的USD和基于USD的外观开发套件称为Solaris

> 独立使用
> 
> 这是目前最不方便艺术家的选项，但对于那些想要体验皮克斯动画工作室提供的USD的人来说，这可能很有趣。以独立方式使用USD有两种方式：
> 
> **. 预构建的二进制文件**
> 
> 虽然可用的预构建二进制文件很少，但NVIDIA确实在[developer.nvidia.com/usd](https://developer.nvidia.com/usd#bin) 上提供了一些。
> 
> **. 自己编译**
> 
> 这是使用USD的“传统”入门方式，对于非软件工程师来说，这可能是令人难以置信的艰巨任务。但是，如果你确实想走这条路；[皮克斯动画工作室提供了很棒的制作指导](https://github.com/PixarAnimationStudios/USD)


如果你是USD的新手，并且你想学习构建和使用USD；建议通过宿主应用程序构建USD组合和层。每个宿主应用都有自己的学习曲线，以及在USD方面的独特的挑战和特性；但可能会让你走得最快。

!> 本书中的所有图像都使用了自己编译的方法，并且严重依赖于USDview等USD捆绑工具。