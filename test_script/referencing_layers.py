from pxr import Usd, UsdGeom
stage = Usd.Stage.Open('HelloWorld.usda')
hello = stage.GetPrimAtPath('/hello')
stage.SetDefaultPrim(hello)


UsdGeom.XformCommonAPI(hello).SetTranslate((4, 5, 6))
print(stage.GetRootLayer().ExportToString())
stage.GetRootLayer().Save()