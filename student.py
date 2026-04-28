import matplotlib.pyplot as plt
import pandas as pd 
df=pd.read_csv("/home/kverma/Fetch-Analyze-Deploy/datasets/student_performance_finalscore.csv")
#print(df.head())
#print("Shape",df.shape)
print("\n Columns",df.columns)
#print("\n Info \n ",df.info()) #datatypes of each columns
#print("\n Descirbe",df.describe()) #basics statistics on numeric columns
#print(df[["Exam_Anxiety_Score", "Final_Score"]].corr())
#df["Final_Score"].hist()
#plt.show()
#print(df.select_dtypes(include="number").corr()['Final_Score'].sort_values())
income_score=df.groupby("Family_Income_Level")["Final_Score"].mean()
income_score.plot(kind="bar" )
plt.show()
#df.plot.scatter(x="Exam_Anxiety_Score",y="Final_Score")
#plt.show()

