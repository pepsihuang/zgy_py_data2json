
# 案例excel文档路径


All_data = {
    "组织1数据": {

    },
    "组织2数据": {

    }
}

excelPath = ""

# 获取某个单元格数据

def getItem(excelFilePath, x,y):
    return "item"
    pass


# 定义excel单元格和数据类型map

META_MAP = {
    "组织名称":(1, 2),
    "组织全称":(1, 2),
    "组织简称":(1, 2),
    "组织英文名":(1, 2),
    "成立时间":(1, 2),
    "组织岁数（无需填写，表格自动计算）":(1, 2),
    "组织办事处":(1, 2),
    "一句话概括":(1, 2),
    "愿景":(1, 2),
    "使命":(1, 2),
    "组织评级":(1, 2),
    "评级年份":(1, 2),
    "官网链接":(1, 2),
    "领域分类":(1, 2),
    "关注议题":(1, 2),
    "SDGs":(1, 2),
    "当年员工总人数（个）":(1, 2),
    "当年志愿者人数（个）":(1, 2),
    "主要项目地区":(1, 2),
    "影响力指标":(1, 2),
    "时间":(1, 2),
    "动词":(1, 2),
    "数字":(1, 2),
    "单位":(1, 2),
    "影响对象":(1, 2),
    "捐赠方式":(1, 2),
    "名称":(1, 2),
    "捐赠入口":(1, 2),
    "联系方式":(1, 2),
    "信息":(1, 2),
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