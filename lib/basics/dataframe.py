import pandas as pd
import lib.date as date
data = [
    [1000, 21, 1],
    [1000, 21, 2],
    [1000, 21, 2],
    [1000, 23, 1],
    [1000, 23, 2],
    [1000, 23, 2],
    [1000, 23, 2],
    [1000, 25, 1],
    [1000, 25, 2],
    [1000, 25, 2],
    [1000, 25, 2],
    [1000, 25, 2],
    [1000, 25, 2],
    [1000, 25, 2],
    [1005, 21, 1],
    [1005, 21, 2],
    [1005, 25, 1],
    [1005, 25, 2],
    [1005, 25, 2],
    [1005, 25, 6],
    [1005, 25, 6],
    [1005, 23, 1],
    [1005, 23, 2],
    [1005, 23, 2],
    [1005, 23, 6],
    [1005, 23, 4]
]

df = pd.DataFrame(data, columns=["uid", "gid", "xtype"])
# apply + lambda
# 取每行 uid 数据前两位
print(df["uid"].apply(lambda x: str(x)[:2]))

# group by + apply + lambda
# 按 uid, gid 分组
gid_dict1 = df.groupby(["uid", "gid"]).apply(lambda x: max(x["xtype"].tolist())).to_dict()
gid_dict2 = df.groupby(["uid", "gid"]).apply(lambda x: x["xtype"].tolist()).to_dict()
# gid_dict2 = { (uid1, gid1): [type1, type2...], (uid2, gid2): [..], ....}      # 字典的 key 可以是元组
print(gid_dict1)
print(gid_dict2)

# group by + agg(聚合)
df1 = df.groupby(["uid", "gid"]).agg({"xtype": "max"})
print(df1)
print(df1.to_dict())

df2 = df.groupby("uid").agg({"gid": "min", "xtype": ["min", "max"]})
print(df2)
print(df2.to_dict())

