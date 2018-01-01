import tushare as ts

df = ts.get_realtime_quotes('000581')
print(df[['code', 'name', 'price', 'bid', 'b1_v', 'b1_p', 'b2_v', 'b2_p', 'b3_v', 'b3_p', 'b4_v', 'b4_p', 'b5_v',
          'b5_p', 'ask', 'volume', 'amount', 'time']])


df = ts.get_tick_data('000581', date='2017-12-28')
#print(df)
print(ts.__version__)