# Tampa Bay vacancy composition by ZCTA, 2020-2024

Richard Cieplechowicz (also legally known as Ryszard Cieplechowicz) · September 29, 2026

A vacancy rate alone does not say why housing units are vacant. In the 132 Tampa Bay ZIP Code Tabulation Areas (ZCTAs) selected for the existing housing dataset, the American Community Survey (ACS) estimates 184,380 vacant housing units out of 1,513,832 total units. Of the estimated vacant units, 81,351 (44.1%) are classified as seasonal, recreational, or occasional use and 33,244 (18.0%) as for rent. The categories are survey estimates, not a count of available homes today.

The four-county selection includes 53 ZCTAs assigned to Hillsborough, 47 to Pinellas, 23 to Pasco, and 9 to Hernando. The estimated seasonal/recreational/occasional share of vacant units is 21.5%, 52.2%, 53.7%, and 45.5%, respectively. Those are descriptive ratios of summed ZCTA estimates, not countywide vacancy estimates or precise comparisons. In particular, this table should not be read as a measure of rental inventory.

## Source and method

Source: U.S. Census Bureau, [2020-2024 ACS five-year detailed table B25004, Vacancy Status](https://api.census.gov/data/2024/acs/acs5/groups/B25004.html), and [B25002, Occupancy Status](https://api.census.gov/data/2024/acs/acs5/groups/B25002.html). The estimates and 90% margins of error were retrieved through [Census Reporter's API](https://api.censusreporter.org/1.0/data/show/acs2024_5yr?table_ids=B25002,B25004&geo_ids=86000US33701), an access layer, not the data author. The raw response is pinned in this repository; `download.py` fetches it in small batches and `build.py` reproduces the CSV.

The 132 ZCTAs and assigned county come from the [prior Tampa Bay housing and rent dataset](https://github.com/richard-cieplechowicz/tampa-bay-zip-housing-data). That selection uses 2020 Census ZCTA-to-county relationships, choosing the county with the greatest land-area share, and requires at least 500 residents. A ZCTA can cross county borders. These sums do not cover every ZCTA or all addresses in each county.

For every row, `vacant_units` agrees between B25002 and B25004, and the seven B25004 categories sum to the B25004 total. The vacancy rate matches the prior published CSV. Shares are category counts divided by B25004 vacant units, rounded to one decimal; shares are blank if no vacant units are estimated. The quality flag marks fewer than 300 estimated vacant units, an analytic caution rather than an official Census flag.

## Fields

- `zcta`, `assigned_county`, `population`: the prior selection and population context; ZCTA is not the USPS delivery ZIP.
- `housing_units`, `occupied_units`, `vacant_units`, `vacant_units_moe_90pct`: ACS B25002 estimates and published 90% margin of error for vacancy.
- `for_rent_units`, `rented_not_occupied_units`, `for_sale_only_units`, `sold_not_occupied_units`, `seasonal_recreational_occasional_units`, `migrant_worker_units`, `other_vacant_units`: seven B25004 estimates.
- `for_rent_moe_90pct`, `seasonal_moe_90pct`, `other_vacant_moe_90pct`: published ACS 90% margins of error for selected categories; other category MOEs remain in the pinned raw source.
- `vacancy_rate_pct`: B25002 vacant units / total housing units.
- `for_rent_share_of_vacant_pct`, `seasonal_share_of_vacant_pct`: B25004 category count / B25004 vacant total, rounded. These are not rental vacancy rates. Derived ratios have no computed margin of error here.
- `small_vacant_base_flag`: `yes` under 300 estimated vacant units.

## Limits

The ACS 2020-2024 five-year period is not current property availability. B25004 "for rent" is a vacancy-status classification, not a listing scrape; "seasonal, recreational, or occasional use" does not prove any unit is available to rent. ACS samples have uncertainty, particularly for small ZCTAs; margins of error on sums or derived shares have not been calculated, so differences may not be meaningful. Zero estimates can have nonzero margins of error. Census geography and the selected ZCTA-to-county assignment limit county interpretations. Do not average ZCTA shares or infer an individual's situation from these area-level measures.

## Reproduce and cite

`python3 download.py && python3 build.py` rebuilds from the Census Reporter release; `python3 build.py` works offline from the pinned response and prior CSV. Source data: U.S. Census Bureau, 2020-2024 ACS five-year detailed tables B25002 and B25004. The compilation is CC BY 4.0; Census source data are public domain. Suggested citation: Cieplechowicz, Richard (Ryszard). *Tampa Bay vacancy composition by ZCTA, 2020-2024* (2026).
