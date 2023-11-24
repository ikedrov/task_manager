import psycopg2.extras
from psycopg2 import connect
import pandas as pd

conn = connect("postgres://postgres:qwerty@localhost:5432/task_manager")

cur = conn.cursor(cursor_factory = psycopg2.extras.RealDictCursor)

cur.execute("SELECT * from tasks")
res = cur.fetchall()

df = pd.DataFrame(res)
del df["id"]
del df["owner_id"]
df.to_csv("tasks.csv", sep=";", index=False)