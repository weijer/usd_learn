from pxr import Usd, Vt, UsdGeom

stage = Usd.Stage.Open('HelloWorld.usda')
xform = stage.GetPrimAtPath('/hello')
print(xform)
sphere = stage.GetPrimAtPath('/hello/world')
print(sphere)

# 列出每个 prim 上的可用属性名称
print(xform.GetPropertyNames())
print(sphere.GetPropertyNames())

# 读取 sphere prim 上的 extent 属性
extentAttr = sphere.GetAttribute('extent')

# Vt.Vec3fArray(2, (Gf.Vec3f(-1.0, -1.0, -1.0), Gf.Vec3f(1.0, 1.0, 1.0)))
# UsdPrim::GetPropertyNames 演示了我们可以通过名称获取属性。
# 实际上，要遍历 prim 的属性，通常使用 UsdPrim::GetProperties、UsdPrim::GetAttributes或UsdPrim::GetRelationships之一更方便。
# 它们返回可以直接操作的UsdProperty、UsdAttribute和 UsdRelationship对象。
extent_obj = extentAttr.Get()

# 修改半径
radiusAttr = sphere.GetAttribute('radius')
radius_modify_res = radiusAttr.Set(2)
print(radius_modify_res)

#
extent_modify_res = extentAttr.Set(extentAttr.Get() * 2)
print(extent_modify_res)

# 打印生成的场景描述
print(stage.GetRootLayer().ExportToString())

# 与Hello World Redux - 使用通用 Prims一样，我们可以使用UsdGeom模式 API来实现 。
# 这种方法的一个好处是一流的 API 隐藏了属性的原始名称是primvars:displayColor的事实。
# 这使客户端代码不必知道该细节
sphereSchema = UsdGeom.Sphere(sphere)
color = sphereSchema.GetDisplayColorAttr()
res_color_modify = color.Set([(0, 0, 1)])
print(res_color_modify)

# 打印生成的场景描述
print(stage.GetRootLayer().ExportToString())

# 保存修改
#stage.GetRootLayer().Save()
