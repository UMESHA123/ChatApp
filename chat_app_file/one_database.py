import psycopg2
def chat_database():
    con=psycopg2.connect(host="ec2-23-21-4-7.compute-1.amazonaws.com",database="d3cgb3tsbur7dj",user="huzavcwsvfccit",password="2c961ae9faa5eafc0340e151a64ab5631699caf63850c1a03218f9524e4e66d1",port="5432",)
    cur=con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS ChatData( one_chat text,send_data text);''')
    con.commit()
    cur.execute('''CREATE TABLE IF NOT EXISTS ChatData1( one_chat text);''')
    con.commit()

chat_database()