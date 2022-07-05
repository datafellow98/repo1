import pandas as pd
import numpy as np
form1 = pd.read_excel("Balmaitri.xlsx" , sheet_name="family_member_repeat")
#first count the values
cnt1 = form1.groupby(["ward","Ethnic Group"],as_index=False)["Ethnic Group"].count().rename("Count")
cnt1.to_excel("C:\Python\Household Profile\Table2.xlsx")
#form2 = pd.read_excel("Table2.xlsx")
#form2["Total"] = form2.groupby("ward").Count.transform('sum')
#form2.to_excel("Profile1.xlsx")
