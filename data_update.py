import csv

def check_df(df,col):
    try:
        open(df,'r')
    except:
        with open(df,'w',newline='') as Temp_data:
            dataframe = csv.DictWriter(Temp_data, fieldnames = col)
            dataframe.writeheader()

def add_data(t,d,df,col):
    with open(df,'a',newline='') as Temp_data:
        dataframe = csv.DictWriter(Temp_data, fieldnames = col)
        new_data = {"Temperature":t,"Date":d}
        dataframe.writerow(new_data)

def value_del(df):
    i=0
    lines = list()
    with open(df, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            if i!=1:
                lines.append(row)
            i+=1
    with open(df, 'w',newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
        
def find_len(df):
    with open(df) as f:
        return(sum(1 for line in f)-1)
        
