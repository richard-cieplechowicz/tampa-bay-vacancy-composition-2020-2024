#!/usr/bin/env python3
"""Rebuild the Tampa Bay vacancy-composition table from pinned ACS source snapshots."""
import csv, json, pathlib
P=pathlib.Path(__file__).parent
prior=list(csv.DictReader((P/'prior-tampa-bay-zip-housing-2024.csv').open()))
source=json.loads((P/'census-reporter-acs2024-5yr-b25002-b25004.json').read_text())
assert source['release']['id']=='acs2024_5yr' and source['release']['years']=='2020-2024'
assert len(prior)==132 and len(source['data'])==132
head=['zcta','assigned_county','population','housing_units','occupied_units','vacant_units','vacant_units_moe_90pct','for_rent_units','for_rent_moe_90pct','rented_not_occupied_units','for_sale_only_units','sold_not_occupied_units','seasonal_recreational_occasional_units','seasonal_moe_90pct','migrant_worker_units','other_vacant_units','other_vacant_moe_90pct','vacancy_rate_pct','for_rent_share_of_vacant_pct','seasonal_share_of_vacant_pct','small_vacant_base_flag']
out=[]
for r in prior:
 d=source['data']['86000US'+r['zip']];e=d['B25004']['estimate'];m=d['B25004']['error'];o=d['B25002']['estimate'];om=d['B25002']['error']
 def val(tab,n):
  x=tab.get('B25004%03d'%n)
  return x if x is not None and x>=0 else ''
 total=o['B25002001']; vacant=o['B25002003'];occupied=o['B25002002'];v=val(e,1)
 assert total==occupied+vacant, r['zip'];assert vacant==v, r['zip'];assert all(val(e,i)!='' for i in range(1,9)),r['zip'];assert sum(val(e,i) for i in range(2,9))==v,r['zip']
 assert (round(v/total*100,1)==float(r['vacancy_rate_pct']) if total else not r['vacancy_rate_pct']),r['zip']
 out.append(dict(zip(head,[r['zip'],r['county'],r['population'],total,occupied,vacant,om['B25002003'],val(e,2),val(m,2),val(e,3),val(e,4),val(e,5),val(e,6),val(m,6),val(e,7),val(e,8),val(m,8),round(v/total*100,1) if total else '',round(val(e,2)/v*100,1) if v else '',round(val(e,6)/v*100,1) if v else '','yes' if v<300 else 'no'])))
with (P/'tampa-bay-vacancy-composition-by-zcta-2020-2024.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,head);w.writeheader();w.writerows(out)
print('rows',len(out),'housing',sum(x['housing_units'] for x in out),'vacant',sum(x['vacant_units'] for x in out),'for rent',sum(x['for_rent_units'] for x in out),'seasonal',sum(x['seasonal_recreational_occasional_units'] for x in out),'small bases',sum(x['small_vacant_base_flag']=='yes' for x in out))
for c in sorted(set(x['assigned_county'] for x in out)):
 a=[x for x in out if x['assigned_county']==c];v=sum(x['vacant_units'] for x in a);print(c,len(a),v,'for rent',sum(x['for_rent_units'] for x in a),'seasonal',sum(x['seasonal_recreational_occasional_units'] for x in a))
