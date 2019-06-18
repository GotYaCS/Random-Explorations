import json
import requests
import datetime
from urllib.request import urlopen

source ='''
{"time":"2019-06-17T10:43:03-05:00","new_changeset":true,"status":{"code":200,"msg":"ok"},"rqst":{"method":"GetDeparturesByStop","params":{"stop_id":"IU:2"}},"departures":[{"stop_id":"IU:2","headsign":"9B Brown","route":{"route_color":"825622","route_id":"BROWN","route_long_name":"Brown","route_short_name":"9","route_text_color":"ffffff"},"trip":{"trip_id":"[@124.0.123534654@][1552400172772]\/36__BB2_MF","trip_headsign":"Parkland College","route_id":"BROWN","block_id":"BB2 MF","direction":"B","service_id":"BB2 MF","shape_id":"[@124.0.123534654@]366"},"vehicle_id":"0322","origin":{"stop_id":"PKLN:1"},"destination":{"stop_id":"PKLN:1"},"is_monitored":true,"is_scheduled":true,"is_istop":false,"scheduled":"2019-06-17T10:39:00-05:00","expected":"2019-06-17T10:43:37-05:00","expected_mins":1,"location":{"lat":40.11058,"lon":-88.225167}},{"stop_id":"IU:2","headsign":"1N Yellow","route":{"route_color":"fcee1f","route_id":"YELLOW","route_long_name":"Yellow","route_short_name":"1","route_text_color":"000000"},"trip":{"trip_id":"[@124.0.123464910@][1552337681550]\/37__Y3_MF","trip_headsign":"Champaign Walmart","route_id":"YELLOW","block_id":"Y3 MF","direction":"North","service_id":"Y3 MF","shape_id":"[@124.0.123464910@]YELLOW 62"},"vehicle_id":"1714","origin":{"stop_id":"ISWS:2"},"destination":{"stop_id":"WALMART:2"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T10:41:00-05:00","expected":"2019-06-17T10:43:55-05:00","expected_mins":1,"location":{"lat":40.10697,"lon":-88.223833}},{"stop_id":"IU:2","headsign":"12W Teal","route":{"route_color":"006991","route_id":"TEAL","route_long_name":"Teal","route_short_name":"12","route_text_color":"ffffff"},"trip":{"trip_id":"[@7.0.41893871@][4][1243540851671]\/11__T1_MF","trip_headsign":"Illinois Terminal","route_id":"TEAL","block_id":"T1 MF","direction":"West","service_id":"T1 MF","shape_id":"12W TEAL 12"},"vehicle_id":"1170","origin":{"stop_id":"ODSS:1"},"destination":{"stop_id":"IT:5"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T10:48:00-05:00","expected":"2019-06-17T10:48:00-05:00","expected_mins":5,"location":{"lat":40.10051,"lon":-88.222833}},{"stop_id":"IU:2","headsign":"22S Illini Limited","route":{"route_color":"5a1d5a","route_id":"ILLINI LIMITED","route_long_name":"Illini Limited","route_short_name":"22","route_text_color":"ffffff"},"trip":{"trip_id":"[@124.0.126343174@][1557347385279]\/15__I1_MF","trip_headsign":"Transit Plaza","route_id":"ILLINI LIMITED","block_id":"I1 MF","direction":"South","service_id":"I1 MF","shape_id":"[@124.0.126343174@]ILLINI 845"},"vehicle_id":"0103","origin":{"stop_id":"LNCLNKLRNY:1"},"destination":{"stop_id":"5THCHAL:4"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T10:46:00-05:00","expected":"2019-06-17T10:48:07-05:00","expected_mins":5,"location":{"lat":40.116723,"lon":-88.2195}},{"stop_id":"IU:2","headsign":"1N YELLOWhopper","route":{"route_color":"fcee1f","route_id":"YELLOWHOPPER","route_long_name":"YELLOWhopper","route_short_name":"1","route_text_color":"000000"},"trip":{"trip_id":"[@124.0.123472930@][1552338942772]\/5__Y7_MF","trip_headsign":"Illinois Terminal","route_id":"YELLOWHOPPER","block_id":"Y7 MF","direction":"North","service_id":"Y7 MF","shape_id":"[@124.0.123472930@]YELLOWHOPPER 23"},"vehicle_id":"1354","origin":{"stop_id":"E14:2"},"destination":{"stop_id":"IT:5"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T10:51:00-05:00","expected":"2019-06-17T10:55:39-05:00","expected_mins":13,"location":{"lat":40.089933,"lon":-88.250333}},{"stop_id":"IU:2","headsign":"2C Red","route":{"route_color":"ed1c24","route_id":"RED","route_long_name":"Red","route_short_name":"2","route_text_color":"000000"},"trip":{"trip_id":"[@14.0.56288404@][1][1302720941921]\/3__R5_MF","trip_headsign":"Market Place","route_id":"RED","block_id":"R5 MF","direction":"Champaign","service_id":"R5 MF","shape_id":"RED 1"},"vehicle_id":"1187","origin":{"stop_id":"LSE:1"},"destination":{"stop_id":"MKTPLC:1"},"is_monitored":true,"is_scheduled":true,"is_istop":false,"scheduled":"2019-06-17T10:56:00-05:00","expected":"2019-06-17T10:58:59-05:00","expected_mins":16,"location":{"lat":40.087907,"lon":-88.190833}},{"stop_id":"IU:2","headsign":"5W GREENhopper","route":{"route_color":"008063","route_id":"GREENHOPPER","route_long_name":"GREENhopper","route_short_name":"5","route_text_color":"ffffff"},"trip":{"trip_id":"[@7.0.41101146@][4][1237930167062]\/19__GNX5__MF","trip_headsign":"Parkland College","route_id":"GREENHOPPER","block_id":"GNX5  MF","direction":"West","service_id":"GNX5  MF","shape_id":"5W HOPPER 81"},"vehicle_id":"1181","origin":{"stop_id":"WASHLRMN:7"},"destination":{"stop_id":"PKLN:1"},"is_monitored":true,"is_scheduled":true,"is_istop":false,"scheduled":"2019-06-17T10:59:00-05:00","expected":"2019-06-17T10:59:00-05:00","expected_mins":16,"location":{"lat":40.098737,"lon":-88.17775}},{"stop_id":"IU:2","headsign":"1N YELLOWhopper","route":{"route_color":"fcee1f","route_id":"YELLOWHOPPER","route_long_name":"YELLOWhopper","route_short_name":"1","route_text_color":"000000"},"trip":{"trip_id":"[@124.0.123472930@][1552338942772]\/38__Y2_MF","trip_headsign":"Illinois Terminal","route_id":"YELLOWHOPPER","block_id":"Y2 MF","direction":"North","service_id":"Y2 MF","shape_id":"[@124.0.123472930@]29"},"vehicle_id":"1350","origin":{"stop_id":"ISWS:2"},"destination":{"stop_id":"IT:5"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T11:01:00-05:00","expected":"2019-06-17T11:02:04-05:00","expected_mins":19,"location":{"lat":40.104183,"lon":-88.230083}},{"stop_id":"IU:2","headsign":"12W Teal","route":{"route_color":"006991","route_id":"TEAL","route_long_name":"Teal","route_short_name":"12","route_text_color":"ffffff"},"trip":{"trip_id":"[@7.0.41893871@][4][1243540851671]\/12__T3_MF","trip_headsign":"Illinois Terminal","route_id":"TEAL","block_id":"T3 MF","direction":"West","service_id":"T3 MF","shape_id":"12W TEAL 12"},"vehicle_id":"1724","origin":{"stop_id":"ODSS:1"},"destination":{"stop_id":"IT:5"},"is_monitored":true,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T11:08:00-05:00","expected":"2019-06-17T11:08:00-05:00","expected_mins":25,"location":{"lat":40.110453,"lon":-88.224417}},{"stop_id":"IU:2","headsign":"4E Blue","route":{"route_color":"355caa","route_id":"BLUE","route_long_name":"Blue","route_short_name":"4","route_text_color":"ffffff"},"trip":{"trip_id":"[@124.0.123530431@][1552398636983]\/41__B2_MF","trip_headsign":"Illinois Terminal","route_id":"BLUE","block_id":"B2 MF","direction":"East","service_id":"B2 MF","shape_id":"[@124.0.123530431@]BLUE 51"},"vehicle_id":"1351","origin":{"stop_id":"RNDBRNRD:2"},"destination":{"stop_id":"IT:1"},"is_monitored":true,"is_scheduled":true,"is_istop":false,"scheduled":"2019-06-17T11:10:00-05:00","expected":"2019-06-17T11:10:00-05:00","expected_mins":27,"location":{"lat":40.111087,"lon":-88.27925}},{"stop_id":"IU:2","headsign":"1N Yellow","route":{"route_color":"fcee1f","route_id":"YELLOW","route_long_name":"Yellow","route_short_name":"1","route_text_color":"000000"},"trip":{"trip_id":"[@124.0.123464910@][1552337681550]\/49__Y8_MF","trip_headsign":"Champaign Walmart","route_id":"YELLOW","block_id":"Y8 MF","direction":"North","service_id":"Y8 MF","shape_id":"[@124.0.123464910@]YELLOW 7"},"vehicle_id":"null","origin":{"stop_id":"E14:2"},"destination":{"stop_id":"WALMART:2"},"is_monitored":false,"is_scheduled":true,"is_istop":true,"scheduled":"2019-06-17T11:11:00-05:00","expected":"2019-06-17T11:11:00-05:00","expected_mins":28,"location":{"lat":0,"lon":0}}]}
'''
# with urlopen("https://gtfsapi.metrarail.com/gtfs/schedule/stop_times/MD-W_MW2231_V1_A") as response:
#     source = response.read()

# with open('route_data.json','w') as outfile:
#     json.dump(source,outfile)

time = '16:50:00'

#print(datetime.datetime.strptime(time, "%H:%M:%S").strftime("%I:%M %p"))

source = json.loads(source)
print(type(source))


for bus in source["departures"]:
    print(bus["headsign"],"will arrive in about",bus["expected_mins"],"minutes")

# for states in data['states']:
#     print(states['abbreviation'])
