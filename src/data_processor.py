import geopandas


gpkg_path = "../data/gpkgData/pend-gdis-1960-2018-disasterlocations.gpkg"

gdf = geopandas.read_file(gpkg_path)

print(gdf.head())

print(gdf.disastertype)
