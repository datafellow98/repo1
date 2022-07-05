import pandas as pd
import numpy as np
form1 = pd.read_excel("Balmaitri.xlsx" , sheet_name="family_member_repeat")
#first count the values
df = form1.groupby(['ward','Gender'],as_index=False)['Gender'].agg({'Count':'count'})
df["Sum"]=df.groupby("ward").Count.transform('sum')
df.groupby("ward", axis = 1).sum()
df.to_excel("C:\Python\Household Profile\Table1.xlsx")


