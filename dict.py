import pandas as pd
details={
		'Name':['alice','bob','charlie'],
		'age':[25,30,35],
		'score':[88,76,91]
	}
df=pd.DataFrame(details)
print(df)
