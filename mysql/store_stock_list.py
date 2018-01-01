insert_sql = "INSERT INTO stock_info (code, tick, volume, open, close, high, low) VALUES ('%s', '%s', %s, %s, %s, %s, %s);"


def write_data(conn, data):
    cur = conn.cursor()
    for index, row in data.iterrows():
        row_tulpe = (row['code'], row['date'], row['volume'], row['open'], row['close'], row['high'], row['low'])
        wsql = insert_sql % row_tulpe
        try:
            cur.execute(wsql)
        except:
            pass
    conn.commit()
