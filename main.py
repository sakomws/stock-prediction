#!/usr/bin/python
from __future__ import print_function
import sys
import time
from yahoofinancials import YahooFinancials as YF
import collect
import prediction

DEFAULT_ARGS = ('GOOGL')
MODULE_ARGS = ('yf', 'yahoofinancial', 'yahoofinancials')
HELP_ARGS = ('-h', '--help')
global mark
global company
mark= '-' * 64
if len(sys.argv) > 1:
     company=sys.argv[1]
else:
    company='Google'

def timeit(f, *args):
    print(mark)
    st = time.time()
    f(*args)
    et = time.time()
    print(mark)
    print('Operation completed in: ',et - st, 'seconds.')

if __name__ == '__main__':
    api = set(s for s in dir(YF) if s.startswith('get_'))
    api.update(MODULE_ARGS)
    api.update(HELP_ARGS)
    ts = sys.argv[1:]
    queries = [q for q in ts if q in api]
    ts = [t for t in ts if not t in queries] or DEFAULT_ARGS
    if [h for h in HELP_ARGS if h in queries]:
        helpapi(queries)
    elif queries:
        customapi(queries, ts)
    else:
        a=collect.Collect(ts[0] if 1 == len(ts) else ts)
        timeit(a.data_collect)
        timeit(a.print_console)
        timeit(a.save_csv)
        b=prediction.Prediction()
        b.training_data()
        b.testing_data()
        b.predict_price()




