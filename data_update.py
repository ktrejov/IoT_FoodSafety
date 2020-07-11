import csv

def check_df(df,col):
    try:
        open(df,'r')
    except:
        with open(df,'w') as Temp_data:
            dataframe = csv.DictWriter(Temp_data, fieldnames = col)
            dataframe.writeheader()

def add_data(t,d,df,col):
    with open(df,'a') as Temp_data:
        dataframe = csv.DictWriter(Temp_data, fieldnames = col)
        new_data = {"Temperature":t,"Date":d}
        dataframe.writerow(new_data)