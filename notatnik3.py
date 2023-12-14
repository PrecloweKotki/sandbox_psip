import sqlalchemy

db_params = sqlalchemy.URL.create(
    drivername="postgres+pg5432",
    username="postgres",
    password="koczkodan",
    host="localhost",
    database="Koc_server"
)
engine=sqlalchemy.create_engine(db_params)
connection=engine.connect()
sql_query_1="INSERT INTO public.my_table(name) VALUES('JOKER')"
connection.execute(sql_query_1)