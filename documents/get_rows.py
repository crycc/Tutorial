import datetime
from dateutil.relativedelta import relativedelta


def get_rows():
    FY_list = ['FY20', 'FY21', 'FY22', 'FY23', 'FY24', 'FY25']
    monthDict = []
    Division_list = ["AP", "AW"] * 72
    fy_2 = sorted(FY_list * 24)
    list_temp = []
    # 最终输出的rows
    # s_shape = (144, 98)
    # 日期辅助表
    date_list = []
    date_now = datetime.datetime.now().strftime('%Y-05-01')
    # 转日期格式
    date_before = datetime.datetime.strptime(date_now, '%Y-%m-%d')
    for a in range(72):
        date_before += relativedelta(months=1)
        date_list.append(date_before.strftime('%Y-%m-%d'))
        date_list.append(date_before.strftime('%Y-%m-%d'))
        monthDict.append(date_before.strftime('%b'))
        monthDict.append(date_before.strftime('%b'))
    for temp_0 in range(98):
        list_temp.append("0")
    for temp_1 in range(144):
        list_temp[0] = fy_2[temp_1]
        list_temp[1] = monthDict[temp_1]
        list_temp[2] = Division_list[temp_1]
        list_temp[3] = date_list[temp_1]
        # print(list_temp)
        print(list_temp)


if __name__ == "__main__":
    get_rows()
