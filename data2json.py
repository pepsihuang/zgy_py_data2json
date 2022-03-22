
# 案例excel文档路径


All_data = {}

excelPath = ""

# 获取某个单元格数据

def getItem(excelFilePath, x,y):
    return "item"
    pass


# 定义excel单元格和数据类型map

META_MAP = {
    "name": (1, 2),
    "website": (2, 2)
}


def getAllExcels(path):
    return [
        ""
    ]
    pass

allFile = getAllExcels(excelPath)

for file in allFile:
    name = ""
    for itemInfo in META_MAP:
        itemPos = META_MAP[itemInfo]
        itemData = getItem(itemPos[0], itemPos[1])
        if itemInfo == "name":
            name = itemInfo
            All_data[name] = {}
        All_data[name][itemInfo] = itemData
        pass


print(All_data)