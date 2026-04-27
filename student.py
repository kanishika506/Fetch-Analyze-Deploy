import pandas as pd 
df=pd.read_csv("/home/kverma/Fetch-Analyze-Deploy/datasets/student_performance_finalscore.csv")
#print(df.head())
#print("Shape",df.shape)
#print("\n Columns",df.columns)
#print("\n Info \n ",df.info()) #datatypes of each columns
print("\n Descirbe",df.describe()) #basics statistics on numeric columns
