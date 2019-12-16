"""
monthDict = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")

FY20  财年  FY当前年后2位+1

month 月份  从6月开始排 对应英文字母前3位

Division  AP 和FW 交替

DateTemp  时间格式 年-月-日   当前月第一天 例如 2019-06-01

其余字段默认 0
"""

import datetime
import numpy as np
import pandas as pd
from sympy.physics.units import length
import calendar as cal

"""
tempSchema = StructType([
    StructField("Fiscal_Year", StringType()),
    StructField("Month", StringType()),
    StructField("Division", StringType()),
    StructField("DateTemp", StringType()),
    StructField("Overall_IB_Demand", StringType()),
    StructField("3B_IB_Demand", StringType()),
    StructField("1025_IB_DRS", StringType()),
    StructField("1027_IB_DRS", StringType()),
    StructField("1025_IB_NFS_Rebuy", StringType()),
    StructField("1025_IB_CICO", StringType()),
    StructField("1027_IB_CICO", StringType()),
    StructField("IB_STO_From_OtherCountry_To_1025", StringType()),
    StructField("IB_STO_From_OtherCountry_To_1027", StringType()),
    StructField("IB_STO_From_1025_To_OtherCountry", StringType()),
    StructField("IB_STO_From_1027_To_OtherCountry", StringType()),
    StructField("IB_STO_1025_To_1027", StringType()),
    StructField("IB_STO_1027_To_1025", StringType()),
    StructField("1039_IB_Demand", StringType()),
    StructField("IB_Temporary_Mitigation1", StringType()),
    StructField("IB_Temporary_Mitigation2", StringType()),
    StructField("1025_IB_Demand_After3B", StringType()),
    StructField("1025_IB_Demand_AfterMN", StringType()),
    StructField("1025_IB_Demand_After3B&MN", StringType()),
    StructField("1025_IB_Demand_After3B&MN&Others", StringType()),
    StructField("1025_IB_Demand_After3B&MN_PeakWeek", StringType()),
    StructField("1025_IB_Demand_After3B&MN&Others_PeakWeek", StringType()),
    StructField("1027_IB_Demand_AfterOthers", StringType()),
    StructField("3B_IB_Demand_PeakWeek", StringType()),
    StructField("1027_IB_Demand_AfterOthers_PeakWeek", StringType()),
    StructField("1025_IB_Capacity_Normal", StringType()),
    StructField("1025_IB_Capacity_OT", StringType()),
    StructField("1025_IB_Capacity_AfterImprovement", StringType()),
    StructField("1025_IB_Capacity_Improvement", StringType()),
    StructField("1027_IB_Capacity_OT", StringType()),
    StructField("1039_IB_Capacity", StringType()),
    StructField("IB_Temporary_Capacity1", StringType()),
    StructField("IB_Temporary_Capacity2", StringType()),
    StructField("1025_IB_TTL_Capacity", StringType()),
    StructField("1027_IB_TTL_Capacity", StringType()),
    StructField("PE_IB_TTL_Capacity_Final", StringType()),
    StructField("DoNothing_1025_IB_Utilization", StringType()),
    StructField("DoNothing_1025_IB_Gap", StringType()),
    StructField("DoNothing_1027_IB_Utilization", StringType()),
    StructField("DoNothing_1027_IB_Gap", StringType()),
    StructField("AfterMitigation_1025_IB_Utilization", StringType()),
    StructField("AfterMitigation_1025_IB_Gap", StringType()),
    StructField("AfterMitigation_1027_IB_Utilization", StringType()),
    StructField("AfterMitigation_1027_IB_Gap", StringType()),
    StructField("DoNothing_PE_IB_Utilization", StringType()),
    StructField("DoNothing_PE_IB_Gap", StringType()),
    StructField("AfterMitigation_PE_IB_Utilization", StringType()),
    StructField("AfterMitigation_PE_IB_Gap", StringType()),
    StructField("Overall_OB_Demand", StringType()),
    StructField("3B_OB_Demand", StringType()),
    StructField("1025_OB_DRS", StringType()),
    StructField("1027_OB_DRS", StringType()),
    StructField("1025_OB_NFS", StringType()),
    StructField("1025_OB_CICO", StringType()),
    StructField("1027_OB_CICO", StringType()),
    StructField("OB_STO_From_OtherCountry_To_1025", StringType()),
    StructField("OB_STO_From_OtherCountry_To_1027", StringType()),
    StructField("OB_STO_From_1025_To_OtherCountry", StringType()),
    StructField("OB_STO_From_1027_To_OtherCountry", StringType()),
    StructField("OB_STO_1025_To_1027", StringType()),
    StructField("OB_STO_1027_To_1025", StringType()),
    StructField("1039_OB_Demand", StringType()),
    StructField("OB_Temporary_Mitigation1", StringType()),
    StructField("OB_Temporary_Mitigation2", StringType()),
    StructField("1025_OB_Demand_After3B", StringType()),
    StructField("1025_OB_Demand_AfterMN", StringType()),
    StructField("1025_OB_Demand_After3B&MN", StringType()),
    StructField("1025_OB_Demand_After3B&MN&Others", StringType()),
    StructField("1027_OB_Demand_AfterOthers", StringType()),
    StructField("1025_OB_Capacity_Normal", StringType()),
    StructField("1025_OB_Capacity_OT", StringType()),
    StructField("1025_OB_Capacity_AfterImprovement", StringType()),
    StructField("1025_OB_Capacity_Improvement", StringType()),
    StructField("1027_OB_Capacity_OT", StringType()),
    StructField("1039_OB_Capacity", StringType()),
    StructField("1025_P&H", StringType()),
    StructField("1027_P&H", StringType()),
    StructField("OB_Temporary_Capacity1", StringType()),
    StructField("OB_Temporary_Capacity2", StringType()),
    StructField("1025_OB_TTL_Capacity", StringType()),
    StructField("1027_OB_TTL_Capacity", StringType()),
    StructField("PE_OB_TTL_Capacity_Final", StringType()),
    StructField("DoNothing_1025_OB_Utilization", StringType()),
    StructField("DoNothing_1025_OB_Gap", StringType()),
    StructField("DoNothing_1027_OB_Utilization", StringType()),
    StructField("DoNothing_1027_OB_Gap", StringType()),
    StructField("AfterMitigation_1025_OB_Utilization", StringType()),
    StructField("AfterMitigation_1025_OB_Gap", StringType()),
    StructField("AfterMitigation_1027_OB_Utilization", StringType()),
    StructField("AfterMitigation_1027_OB_Gap", StringType()),
    StructField("DoNothing_PE_OB_Utilization", StringType()),
    StructField("DoNothing_PE_OB_Gap", StringType()),
    StructField("AfterMitigation_PE_OB_Utilization", StringType()),
    StructField("AfterMitigation_PE_OB_Gap", StringType())])
    """

monthDict = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC")
Division_list = ("AP", "AW")
s_shape = (144, 98)
FY_list=['FY20','FY21','FY22','FY23','FY24','FY25']
# np_new=np.empty(shape=[n, m])
# new_array = np.empty(())
b = np.zeros(s_shape, dtype=np.int)
a = b.astype(np.uint8)
print(b)
# 创建一个元素全为0的数组
# a = np.array([(0,0,0,0,...),...(0, 0, 0,0,...)], dtype = np_new)
date_list = list()


# 日期临时表
# 1,4,5,8,9,12
# if (i+1)%4==1:
#     pass
# elif (i+1)%4==2:
#     pass
# elif (i+1)%4==3:
#     pass
# else (i+1)%4==0:
#     pass

def create_assist_date(date_before=None, date_last=None):
    # 创建日期辅助表

    if date_before is None:
        date_before = '2019-06-01'
    if date_last is None:
        date_last = '2019-07-01'
    # 转为日期格式
    date_before = datetime.datetime.strptime(date_before, '%Y-%m-%d')
    date_last = datetime.datetime.strptime(date_last, '%Y-%m-%d')

    date_list.append(date_before.strftime('%Y-%m-%d'))
    # date_list = []
    if date_before < date_last:
        # 月份加1
        date_before += datetime.timedelta(months=+1)
        date_list.append(date_before.strftime('%Y-%m-%d'))
        date_list.append(date_before.strftime('%Y-%m-%d'))
    else:
        # 年份加1
        date_before += datetime.timedelta(years=+1)
        date_list.append(date_before.strftime('%Y-%m-%d'))
        date_list.append(date_before.strftime('%Y-%m-%d'))
    return date_list


def modify_1():
    for i in range(144):
        if i < 24:
            a[i][0] = "FY20"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        elif i < 48:
            a[i][0] = "FY21"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        elif i < 72:
            a[i][0] = "FY22"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        elif i < 96:
            a[i][0] = "FY23"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        elif i < 120:
            a[i][0] = "FY24"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        else:
            a[i][0] = "FY25"
            a[i][1] = monthDict[i]
            a[i][2] = Division_list[i]
            a[i][3] = date_list[i]
        return a
        # print(a)


