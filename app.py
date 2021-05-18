import streamlit as st
import psycopg2

def db_conn():
    conn = psycopg2.connect(host="localhost", port = 5432, database="dailyjournal", user="postgres", password="fasjoin21")
    cur=conn.cursor()
       
    return conn,cur


def update_view(d):
    conn,cur=db_conn()
    sx="select * from public.dailyjournal WHERE date = %s"
    cur.execute(sx,(d,))
    getv=cur.fetchone()
    articlecount,edvideo,bookreading,chess,typing,drawing,lefthand,ted,language=getv[0],getv[1],getv[2],getv[3],getv[4],getv[5],getv[6],getv[7],getv[8]
    articlecount=st.number_input("Enter Articles Read",min_value=articlecount,step=1)
    edvideo=st.number_input("Enter Ed-videos seen",min_value=edvideo,step=5)
    bookreading=st.number_input("Enter Book reading time",min_value=bookreading,step=5)
    chess=st.number_input("Enter chess time played",min_value=chess,step=5)
    typing=st.number_input("Enter typing ",min_value=typing,step=5)
    drawing=st.number_input("Enter drawing time",min_value=drawing,step=5)
    lefthand=st.number_input("Enter Left hand writing time",min_value=lefthand,step=5)
    ted=st.number_input("Enter ted Videos seen",min_value=ted,step=1)
    language=st.number_input("Enter Languages read",min_value=language,step=5)
    us='UPDATE public.dailyjournal SET articlecount= %s,edvideo= %s,bookreading= %s,chess= %s,typing= %s,drawing= %s,lefthand= %s,ted= %s,language= %s where date=%s'
    cur.execute(us,(articlecount,edvideo,bookreading,chess,typing,drawing,lefthand,ted,language,d))
    conn.commit()




    

def main():
    st.text("loaded")
    l=["Nothing","Create New Day","Update Values"]
    sel=st.selectbox("Do you wish to",l)
    if sel=="Nothing":
        st.text("Nothing")
    elif sel=="Update Values":
        conn,cur=db_conn()
        date_sel=st.date_input("Select Date")
        
        
        
        update_view(date_sel)
        
        
        # s="select * from dailyjournal WHERE date = '"+date_sel+"'"
        # getvals=cur.execute(s)
        # print(getvals)
        # s="UPDATE dailyjournal SET api = %s , apiupdated = %s where username = %s"
        # cur.execute(s,(apid,today,username))
        # conn.commit()

    else:
        udate=st.date_input("Select Date")
        if st.checkbox("Create"):
            print(udate)
            conn,cur=db_conn()
            print(udate)
            cur.execute('INSERT INTO public.dailyjournal(dateid,date,articlecount,edvideo,bookreading,chess,typing,drawing,lefthand,ted,language) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(str(udate),udate,0,0,0,0,0,0,0,0,0))
            conn.commit()
            conn.close()
            return "done"

        

main()