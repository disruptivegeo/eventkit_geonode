from geoserver.catalog import Catalog

cat = Catalog('http://localhost:8080/geoserver/rest')
ds = cat.create_datastore('eventkit_geonode','geonode')
ds.connection_parameters.update(host='localhost', port='5432', database='eventkit_geonode', user='eventkit_geonode', passwd='eventkit_geonode', dbtype='postgis', schema='public')
try:
    cat.save(ds)
except Exception as e:
    print e

