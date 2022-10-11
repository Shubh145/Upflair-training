import tkinter as ttk
import pandas as pd





app = ttk.Tk()
app.title('Recommendation system')
app.geometry('600x400')

cols = ['user_id','movie_id','rating','ts']
df = pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
item_cols = ['movie_id','title'] + [str(i) for i in range(22)]
df1 = pd.read_csv('u.item', sep='|', names = item_cols, encoding = "ISO-8859-1")[['movie_id','title']]
movie = pd.merge(df,df1, on='movie_id')
    

result=ttk.Variable(app)
box=ttk.Listbox(app,height=10)
for row,val in movie.iterrows():

    box.insert(row+1,val['title'])
box.place(x=10,y=10)

def get_movie():
    pass

ttk.Button(app,text='Find Reommendation',font=('Ariel',22),command=get_movie).place(x=200,y=50)
ttk.Button(app,textvariable=result,font=('Ariel',22),command=get_movie).place(x=200,y=100)

app.mainloop()

