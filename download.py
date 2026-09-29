#!/usr/bin/env python3
"""Download pinned Census Reporter ACS tables for the original 132-area selection."""
import csv,json,pathlib,urllib.request,time,subprocess
P=pathlib.Path(__file__).parent
rows=list(csv.DictReader((P/'prior-tampa-bay-zip-housing-2024.csv').open()))
all_data={}; tables=None; geography={};release=None
for i in range(0,len(rows),8):
 ids=','.join('86000US'+r['zip'] for r in rows[i:i+8]);url='https://api.censusreporter.org/1.0/data/show/acs2024_5yr?table_ids=B25002,B25004&geo_ids='+ids
 result=json.loads(subprocess.check_output(['curl','-sSL','--fail','--max-time','20',url]))
 assert result['release']['id']=='acs2024_5yr'
 all_data.update(result['data']);geography.update(result['geography']);tables=result['tables'];release=result['release']
 time.sleep(.15)
assert len(all_data)==132
(P/'census-reporter-acs2024-5yr-b25002-b25004.json').write_text(json.dumps({'data':all_data,'geography':geography,'release':release,'tables':tables},indent=2)+'\n')
print('downloaded',len(all_data))
