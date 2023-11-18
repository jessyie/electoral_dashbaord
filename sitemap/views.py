from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
import folium
import pandas as pd # type: ignore
import os # type: ignore
import geopandas as gpd
import fiona
import matplotlib
import locale
import json
from folium import plugins
from django.shortcuts import render, redirect
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings


# Convert WindowsPath object to string
data_loc_str = str(settings.DATA_LOC)

# Create your views here.
# GHMap2 = os.path.join(data_loc_str, 'images', 'ghana_regions16.geojson')
# GHMap = os.path.join(data_loc_str, 'images', 'ghana_regions.geojson')
# ShpW = os.path.join(data_loc_str, 'images', 'WesternG.geojson')
# ShpAs = os.path.join(data_loc_str, 'images', 'Ashanti.geojson')
# ShpAh = os.path.join(data_loc_str, 'images', 'Ahafo.geojson')
# ShpC = os.path.join(data_loc_str, 'images', 'Central.geojson')
# ShpE = os.path.join(data_loc_str, 'images', 'Eastern.geojson')
# ShpGA = os.path.join(data_loc_str, 'images', 'GreaterAccra.geojson')
# ShpN = os.path.join(data_loc_str, 'images', 'Northern.geojson')
# ShpUE = os.path.join(data_loc_str, 'images', 'UpperEast.geojson')
# ShpUW = os.path.join(data_loc_str, 'images', 'UpperWest.geojson')
# ShpV = os.path.join(data_loc_str, 'images', 'Volta.geojson')
# ShpWN = os.path.join(data_loc_str, 'images', 'WesternNorth.geojson')
# ShpS = os.path.join(data_loc_str, 'images', 'Savannah.geojson')
# ShpNE = os.path.join(data_loc_str, 'images', 'NorthEast.geojson')
# ShpB = os.path.join(data_loc_str, 'images', 'Bono.geojson')
# ShpBE = os.path.join(data_loc_str, 'images', 'BonoEast.geojson')
# ShpO = os.path.join(data_loc_str, 'images', 'Oti.geojson')


 #//______________________//

    #//  DATA OF MAP CANVAS
    #//____________________//


# m = folium.Map()

# # file_pathB = os.path.join(data_loc_str, 'my_map', 'my_map.html')

# m = folium.Map(location=[6.67461973426974, -1.5654175654494509], zoom_start= 6)
# folium.Marker(location=[6.67461973426974, -1.5654175654494509], tooltip='Click for more', popup='Geography Department(KNUST)').add_to(m)
# g = folium.GeoJson(GHMap, name = 'Regions').add_to(m)
# g2 = folium.GeoJson(GHMap2, name = '16_Regions').add_to(m)
# ps_group = plugins.FeatureGroupSubGroup(m, name='Polling Stations (PS)')
# shp1 = folium.GeoJson(
#     ShpW, name = 'Western ps',
#     marker=folium.Circle(radius=4, fill_color="orange", fill_opacity=0.4, color="orange", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp2 = folium.GeoJson(
#     ShpAs, name = 'Ashanti PS',
#     marker=folium.Circle(radius=4, fill_color="blue", fill_opacity=0.4, color="blue", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp3 = folium.GeoJson(
#     ShpAh, name = 'Ahafo PS',
#     marker=folium.Circle(radius=4, fill_color="red", fill_opacity=0.4, color="red", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp4 = folium.GeoJson(
#     ShpGA, name = 'Greater Accra PS',
#     marker=folium.Circle(radius=4, fill_color="green", fill_opacity=0.4, color="green", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp5 = folium.GeoJson(
#     ShpC, name = 'Central PS',
#     marker=folium.Circle(radius=4, fill_color="purple", fill_opacity=0.4, color="purple", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp6 = folium.GeoJson(
#     ShpE, name = 'Eastern PS',
#     marker=folium.Circle(radius=4, fill_color="darkred", fill_opacity=0.4, color="darkred", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp7 = folium.GeoJson(
#     ShpN, name = 'Northern PS',
#     marker=folium.Circle(radius=4, fill_color="darkblue", fill_opacity=0.4, color="darkblue", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp8 = folium.GeoJson(
#     ShpUE, name = 'Upper East PS',
#     marker=folium.Circle(radius=4, fill_color="black", fill_opacity=0.4, color="black", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp9 = folium.GeoJson(
#     ShpUW, name = 'Upper West PS',
#     marker=folium.Circle(radius=4, fill_color="beige", fill_opacity=0.4, color="beige", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp10 = folium.GeoJson(
#     ShpV, name = 'Volta PS',
#     marker=folium.Circle(radius=4, fill_color="gray", fill_opacity=0.4, color="gray", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp11 = folium.GeoJson(
#     ShpS, name = 'Savannah PS',
#     marker=folium.Circle(radius=4, fill_color="cadetblue", fill_opacity=0.4, color="cadetblue", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp12 = folium.GeoJson(
#     ShpO, name = 'Oti PS',
#     marker=folium.Circle(radius=4, fill_color="lightgreen", fill_opacity=0.4, color="lightgreen", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp13 = folium.GeoJson(
#     ShpWN, name = 'WesternNorth PS',
#     marker=folium.Circle(radius=4, fill_color="lightgray", fill_opacity=0.4, color="lightgray", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp14 = folium.GeoJson(
#     ShpB, name = 'Bono PS',
#     marker=folium.Circle(radius=4, fill_color="pink", fill_opacity=0.4, color="pink", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp15 = folium.GeoJson(
#     ShpBE, name = 'Bono East PS',
#     marker=folium.Circle(radius=4, fill_color="pink", fill_opacity=0.4, color="pink", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# shp16 = folium.GeoJson(
#     ShpNE, name = 'North East PS',
#     marker=folium.Circle(radius=4, fill_color="darkgreen", fill_opacity=0.4, color="darkgreen", weight=1),
#     tooltip=folium.GeoJsonTooltip(fields=["PS Name"]),
#     zoom_on_click=True)
# ps_group.add_child(shp1)
# ps_group.add_child(shp2)
# ps_group.add_child(shp3)
# ps_group.add_child(shp4)
# ps_group.add_child(shp5)
# ps_group.add_child(shp6)
# ps_group.add_child(shp7)
# ps_group.add_child(shp8)
# ps_group.add_child(shp9)
# ps_group.add_child(shp10)
# ps_group.add_child(shp11)
# ps_group.add_child(shp12)
# ps_group.add_child(shp13)
# ps_group.add_child(shp14)
# ps_group.add_child(shp15)
# ps_group.add_child(shp16)



# m.add_child(ps_group)

# m._name = "map_name"
# m._id = "1"

# # Get map variable name in output HTML
# mapJsVar = m.get_name()
# psGroupVar = ps_group.get_name()
# #<button id="reset-button" style="border-style: solid; border-radius: 4px; margin-left: 70px; background-color: #6e7785; color: #d68d33; font-weight: bold; position: absolute; z-index: 100;">RESET MAP</button> 
# # Inject HTML into the map HTML
# m.get_root().html.add_child(folium.Element("""

# <script type="text/javascript">
# window.onload = function() {
#     var updateLayerVisibility = function() {
#         var mapZoom = {map_name_1}.getZoom();
        
#         // Check the zoom level and show/hide the ps_group layer
#         if (mapZoom >= 6) {
#             {map_name_1}.addLayer({ps_group});
#         } else {
#             {map_name_1}.removeLayer({ps_group});
#         }
#     }
    
#     updateLayerVisibility();
    
#     {map_name_1}.on("zoomend", updateLayerVisibility);
# }
# </script>
# """.replace("{map_name_1}", mapJsVar).replace("{ps_group}", psGroupVar)))

# reset_button_html = """
# <div style="position: absolute; top: 103px; left: 10px; z-index: 1000;">
#     <button onclick="window.location.href=window.location.href" style="border-style: solid; border-radius: 4px; background-color: #6e7785; color: #d68d33; font-weight: bold;">Reset Map</button>
# </div>
# """

# # Add the custom HTML button to the map
# m.get_root().html.add_child(folium.Element(reset_button_html))


# # Define a function to reset the map
# # def reset_map(e):
# #     m = folium.Map(location=[6.67461973426974, -1.5654175654494509], zoom_start= 6)
# #     m.fit_bounds(m.get_bounds())

# # mapObj = folium.Map(location=[24.217011233401, 81.0791015625000], zoom_start=5)

# # folium.Marker(location=[24.217011233401, 81.0791015625000],
# #                 tooltip='center',
# #                 icon=folium.DivIcon(html="""Hello World""",
# #                                     class_name="mapText"),
# #                 ).add_to(mapObj)

# # # get map variable name in output html
# # mapJsVar = mapObj.get_name()

# # # inject html into the map html
# # mapObj.get_root().html.add_child(folium.Element("""
# # <style>
# # .mapText {
# #     white-space: nowrap;
# #     color:red;
# #     font-size:large
# # }
# # </style>
# # <script type="text/javascript">
# # windows.onload = function(){
# #     var sizeFromZoom = function(z){return (0.5*z)+"em"}
# #     var updateTextSizes = function(){
# #         var mapzoom = {mapObj}.getZoom();
# #         var txtSize = sizeFromZoom(mapZoom);
# #         $(".mapText").css("font-size", txtSize);
# #     }
# #     updateTextSizes();
# #     {mapObj}.on("Zoomend", updateTextSizes);
# # }
# # </script>

# # """.replace("{mapObj}", mapJsVar)))


# # Add the custom control to the map's root HTML element
# #m.get_root().html.add_child(folium.Element(reset_html))

# # Add Fullscreen control
# fullscreen_control = folium.plugins.Fullscreen()
# m.add_child(fullscreen_control)

# #geocode = folium.GeoJson(ShpW, name = 'Western Electoral Station', zoom_start=20).add_to(m)
# folium.GeoJsonTooltip(fields=["region"]).add_to(g)
# folium.GeoJsonTooltip(fields=["region"]).add_to(g2)
# folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
# folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
# folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
# folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
# folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

# folium.LayerControl().add_to(m)




# m = m._repr_html_()
census='Total Pop'

def initialise_chart(year = '2020', region='Ashanti'):

    # Preprocessing of data
    
    
    filename2 = year + '.csv' 
    path2 = os.path.join(data_loc_str, 'EDATA', filename2)
    df2 = gpd.read_file(path2)

    filename3 = 'District_pop_demographics' + year + '.csv' 
    path3 = os.path.join(data_loc_str, 'EDATA', filename3)
    df3 = gpd.read_file(path3)

     # // Grouped according to Year and Office
    grouped = df2.groupby(['YEAR', 'OFFICE'])
    dfGroup = grouped.get_group((year, 'Parliament'))
    dfGroup2 = grouped.get_group((year, 'Presidential First Round'))
    
    groupedNewA = df2.groupby(['YEAR', 'OFFICE', 'REGION'])
    dfGroupNew1 = groupedNewA.get_group((year, 'Parliament', region))
    dfGroupNew1B = groupedNewA.get_group((year, 'Presidential First Round', region))

    grouped2P = df3.groupby(['Region'])
    dfGroup2P = grouped2P.get_group(region)

    
    
    # =======================================


   
    #//____________________________//

    #//  ANALYSIS OF DATA [PANDAS]
    #//____________________________//


    # gapa = df2[["YEAR", "VALID_VOTES"]]
    # #gapa['YEAR'] = gapa['YEAR'].apply(pd.to_numeric)
    # gapa['VALID_VOTES'] = gapa['VALID_VOTES'].replace(',','', regex=True)
    # gapa['VALID_VOTES'] = gapa['VALID_VOTES'].apply(pd.to_numeric)
    # gapaSum = gapa.groupby(by=['YEAR'])['VALID_VOTES'].sum().reset_index()
    # gapa1AX = gapaSum['YEAR'].values.tolist()
    # gapa1AY = gapaSum['VALID_VOTES']


    # // Finding the Total VALID_VOTES votes on Parliament (A)
    dfGroupA = dfGroup.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupA = dfGroupA.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSum = dfGroupA['VALID_VOTES'].sum() # Sum operation on a specific column
    #print(tSum)

    # // Finding the Total VALID_VOTES votes on Presidential (A)
    dfGroupB = dfGroup2.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True)
    dfGroupB = dfGroupB.apply(pd.to_numeric)
    tSum2 = dfGroupB['VALID_VOTES'].sum()
    #print(tSum2)

    # // Finding the Total sum based on each region for Parliament (B)
    dfRegions = dfGroup[["REGION", "VALID_VOTES"]]
    dfRegions['VALID_VOTES'] = dfRegions['VALID_VOTES'].replace(',','', regex=True)
    dfRegions['VALID_VOTES'] = dfRegions['VALID_VOTES'].astype('int')
    dfRegionsSum = dfRegions.groupby(by=["REGION"])["VALID_VOTES"].sum().reset_index()
    graph1AX = dfRegionsSum['REGION'].values.tolist()
    graph1AY = dfRegionsSum['VALID_VOTES']
    #print(dfRegionsSum)
    #print(graph1AX)

    # // Finding the Total sum based on each region for Presidential (B)
    dfRegions2 = dfGroup2[["REGION", "VALID_VOTES"]]
    dfRegions2['VALID_VOTES'] = dfRegions2['VALID_VOTES'].replace(',','', regex=True)
    dfRegions2['VALID_VOTES'] = dfRegions2['VALID_VOTES'].astype('int')
    dfRegionsSum2 = dfRegions2.groupby(by=["REGION"])["VALID_VOTES"].sum().reset_index()
    graph1BX = dfRegionsSum2['REGION']
    graph1BY = dfRegionsSum2['VALID_VOTES']
    #print(dfRegionsSum2)

    # // Do Total sum operations for each party on Parliament (C)
    dfGroupC = dfGroup.loc[:,'NPP':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupC = dfGroupC.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSumC = dfGroupC.sum().reset_index() # Sum operation on a specific column
    graph2AX = tSumC['index']
    graph2AY = tSumC[0]
    #print(graph2AX)

    # // Do Total sum operations for each party on Presidential (C)
    dfGroupD = dfGroup2.loc[:,'NPP':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupD = dfGroupD.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSumD = dfGroupD.sum().reset_index() # Sum operation on a specific column
    graph2BX = tSumD['index']
    graph2BY = tSumD[0]
    #print(graph2BX)

    # // Do the sum operations of each region on each party for both offices Parliament (D)
    data = [dfGroupA, dfRegions]
    dfMerge = pd.concat(data, axis=1, join='inner')
    dfGroupG = dfMerge.loc[:,'NPP':'IND4'].replace(',','', regex=True)
    dfGroupG = dfGroupG.apply(pd.to_numeric)
    df_grouped3 = dfMerge.groupby(by="REGION")[dfGroupG.columns[:37]].sum().reset_index()
    graph3AY = df_grouped3.loc[:,'NPP':'IND4'].values.tolist()
    graph3AX = df_grouped3['REGION'].values.tolist()
    df_grouped3z = df_grouped3.values.tolist()
    b = df_grouped3

    # // Do the sum operations of each region on each party for both offices Presidential (D)
    data1 = [dfGroupB, dfRegions2]
    dfMergeB = pd.concat(data1, axis=1, join='inner')
    dfGroupE = dfMergeB.loc[:,'NPP':'IND4'].replace(',','', regex=True)
    dfGroupE = dfGroupE.apply(pd.to_numeric)
    df_grouped4 = dfMergeB.groupby(by="REGION")[dfGroupE.columns[:37]].sum().reset_index()
    graph3BY = df_grouped4.iloc[:,1:].values.tolist()
    graph3BX = df_grouped4['REGION'].values.tolist()
    df_grouped4z = df_grouped4.values.tolist()


    # ---------------------------------

    # //   CONSTITUENCY LEVEL ////

    # _________________________________

    # // Finding the Total VALID_VOTES Constituency on Parliament (A)
    dfGroupAC = dfGroupNew1.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupAC = dfGroupAC.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSumR = dfGroupAC['VALID_VOTES'].values.sum() # Sum operation on a specific column
    #print(tSumR)
    
    
    # // Finding the Total VALID_VOTES Constituency on Presidential (A)
    dfGroupBC =  dfGroupNew1B.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True)
    dfGroupBC = dfGroupBC.apply(pd.to_numeric)
    tSum2R = dfGroupBC['VALID_VOTES'].sum()
    #print(tSum2R)

     # // Have a column holding the sum operations of each constituency based on each region(Ashanti)Parliament for both offices (B)
    dfConst = dfGroupNew1[["CONSTITUENCY", "VALID_VOTES"]]
    dfConst['VALID_VOTES'] = dfConst['VALID_VOTES'].replace(',','', regex=True)
    dfConst['VALID_VOTES'] = dfConst['VALID_VOTES'].astype('int')
    graphSub1AX = dfConst['CONSTITUENCY'].values.tolist()
    graphSub1AY = dfConst['VALID_VOTES'].values.tolist()
    #print(graphSub1AY)
    
    
    # // Have a column holding the sum operations of each constituency based on each region(Ashanti) Presidential for both offices (B)
    dfConst1B = dfGroupNew1B[["CONSTITUENCY", "VALID_VOTES"]]
    dfConst1B['VALID_VOTES'] = dfConst1B['VALID_VOTES'].replace(',','', regex=True)
    dfConst1B['VALID_VOTES'] = dfConst1B['VALID_VOTES'].astype('int')
    graphSub1BX = dfConst1B['CONSTITUENCY'].values.tolist()
    graphSub1BY = dfConst1B['VALID_VOTES'].values.tolist()
    # print(graphSub1AY)

    # // Do Total sum operations for each party on Parliament CONSTITUENCY (C)
    dfGroupCP = dfGroupNew1.loc[:,'NPP':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupCP = dfGroupCP.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSumCP = dfGroupCP.sum().reset_index() # Sum operation on a specific column
    graph2AXP = tSumCP['index'].tolist()
    graph2AYP = tSumCP[0]
    #print(graph2AXP)
    
    # // Do Total sum operations for each party on Presidential CONSTITUENCY (C)
    dfGroupDP = dfGroupNew1B.loc[:,'NPP':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroupDP = dfGroupDP.apply(pd.to_numeric) # Converting all the string in the columns to integers
    tSumDP = dfGroupDP.sum().reset_index() # Sum operation on a specific column
    graph2BXP = tSumDP['index']
    graph2BYP = tSumDP[0]
    #print(graph2BXP)
    
    
    # // (D) Ashanti(Parliament) Do Total sum operations for each party on each constituency based on each region for both necessary offices (F) Parliament
    dfGroup1A = dfGroupNew1.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroup1A = dfGroup1A.apply(pd.to_numeric) # Converting all the string in the columns to integers
    dfConst = dfGroupNew1[["CONSTITUENCY", "VALID_VOTES"]]
    data1A = [dfGroup1A, dfConst]
    dfMerge1A = pd.concat(data1A, axis=1, join='inner')
    #print(df2)
    dfGroupG1A = dfMerge1A.loc[:,'NPP':'IND4'].replace(',','', regex=True)
    dfGroupG1A = dfGroupG1A.apply(pd.to_numeric)
    df_grouped3_1A = dfMerge1A.groupby(by="CONSTITUENCY")[dfGroupG1A.columns[:37]].sum().reset_index()
    graph3AY_1A = df_grouped3_1A.iloc[:,1:]
    graph3AX_1A=df_grouped3_1A.CONSTITUENCY
    df_grouped3zP = df_grouped3_1A.values.tolist()
    #print(df_grouped3_1A.CONSTITUENCY)
    
    
    # // (D) Ashanti(Presidential) Do Total sum operations for each party on each constituency based on each region for both necessary offices (F) Parliament
    dfGroup1B = dfGroupNew1B.loc[:,'VALID_VOTES':'IND4'].replace(',','', regex=True) # Selecting specific columns and getting rid of the commas in the string
    dfGroup1B = dfGroup1B.apply(pd.to_numeric) # Converting all the string in the columns to integers
    dfConstB = dfGroupNew1B[["CONSTITUENCY", "VALID_VOTES"]]
    data1B = [dfGroup1B, dfConstB]
    dfMerge1B = pd.concat(data1B, axis=1, join='inner')
    #print(df2)
    dfGroupG1B = dfMerge1B.loc[:,'NPP':'IND4'].replace(',','', regex=True)
    dfGroupG1B = dfGroupG1B.apply(pd.to_numeric)
    df_grouped3_1B = dfMerge1B.groupby(by="CONSTITUENCY")[dfGroupG1B.columns[:37]].sum().reset_index()
    graph3AY_1B = df_grouped3_1B.iloc[:,1:]
    graph3AX_1B=df_grouped3_1B.CONSTITUENCY
    df_grouped3zP2 = df_grouped3_1B.values.tolist()
    #print(df_grouped3_1B.CONSTITUENCY)

    

    tSum = dfGroupA['VALID_VOTES'].values.sum().astype(int).tolist()
    tSum2 = dfGroupB['VALID_VOTES'].values.sum().astype(int).tolist()
    tSumR = dfGroupAC['VALID_VOTES'].values.sum().astype(int).tolist()
    tSum2R = dfGroupBC['VALID_VOTES'].values.sum().astype(int).tolist() 
    graph1AX = dfRegionsSum['REGION'].values.tolist()
    graph1AY = dfRegionsSum['VALID_VOTES'].values.astype(int).tolist()
    graphSub1AX = dfConst['CONSTITUENCY'].values.tolist()
    #graphSub1AY = dfConst['VALID_VOTES'].values.astype(int).tolist() 
    graph1BX = dfRegionsSum2['REGION'].values.tolist()
    graph1BY = dfRegionsSum2['VALID_VOTES'].values.astype(int).tolist()
    graphSub1BX = dfConst1B['CONSTITUENCY'].values.tolist()
    #graphSub1BY = dfConst1B['VALID_VOTES'].values.astype(int).tolist()  
    graph2AX = tSumC['index'].values.astype(str).tolist()
    graph2AY = tSumC[0].values.astype(int).tolist()
    graph2AXP = tSumCP['index'].values.astype(str).tolist()
    graph2AYP = tSumCP[0].values.astype(int).tolist()  
    graph2BX = tSumD['index'].values.astype(str).tolist()
    graph2BY = tSumD[0].values.astype(int).tolist()
    graph2BXP = tSumDP['index'].values.astype(str).tolist()
    graph2BYP = tSumDP[0].values.astype(int).tolist() 
    graph3AY = df_grouped3.iloc[:,1:].values.astype(int).tolist()
    graph3AX = df_grouped3['REGION'].values.tolist()
    graph3BY = df_grouped4.iloc[:,1:].values.astype(int).tolist()
    graph3BX = df_grouped4['REGION'].values.tolist()
    # gapa1AX = gapaSum['YEAR'].values.tolist()
    tSumCA = tSumC.values.tolist()
    tSumDA = tSumD.values.tolist()
    tSumCAP = tSumCP.values.tolist()
    tSumDAP = tSumDP.values.tolist()

    dfp = df_grouped3
    json_records = dfp.reset_index().to_json(orient = 'records')
    arr = []
    arr = json.loads(json_records)

    dfp2 = df_grouped4
    json_records2 = dfp2.reset_index().to_json(orient = 'records')
    arr2 = []
    arr2 = json.loads(json_records2)

     #________________________________

    #// POPULATION DATA PROCESSING//

    #_______________________________

   # // Finding the Total Pop in relation to the Regions
    dfGroupA2P = df3[["Region", census]] # Selecting specific columns and getting rid of the commas in the string
    dfGroupA2P[census] = dfGroupA2P[census].astype('float') # Converting all the string in the columns to integers
    tSum2P = dfGroupA2P[census].values.sum() # Sum operation on a specific column
    dfContinentSum2P = dfGroupA2P.groupby(by=["Region"])[census].sum().reset_index()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census]

    # // Finding the Total Pop in relation to the Districts
    dfGroupB2P = dfGroup2P[["Constituency", census]] # Selecting specific columns and getting rid of the commas in the string
    dfGroupB2P[census] = dfGroupB2P[census].astype('float') # Converting all the string in the columns to integers
    tSumB2P = dfGroupB2P[census].values.sum() # Sum operation on a specific column
    dfContinentSumB2P = dfGroupB2P.groupby(by=["Constituency"])[census].sum().reset_index()
    graph1BX2P = dfContinentSumB2P['Constituency'].values.tolist()
    graph1BY2P = dfContinentSumB2P[census]

    #// List of the header columns
    dfGroupH = df3.columns.tolist()[3:-1]
    
    tSum2P = dfGroupA2P[census].values.sum().astype('float').tolist()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census].values.tolist()

    tSumB2P = dfGroupB2P[census].values.sum().astype('float').tolist()
    graph1BX2P = dfContinentSumB2P['Constituency'].values.tolist()
    graph1BY2P = dfContinentSumB2P[census].values.tolist()

 
    context = {
    'tSum' : tSum,
    'tSum2' : tSum2,
    'tSumR' : tSumR,
    'tSum2R' : tSum2R,
    'tSumCA' : tSumCA,
    'tSumDA' : tSumDA,
    'tSumCAP' : tSumCAP,
    'tSumDAP' : tSumDAP,
    'df_grouped3z' : df_grouped3z,
    'df_grouped4z' : df_grouped4z,
    'df_grouped3zP' : df_grouped3zP,
    'df_grouped3zP2' : df_grouped3zP2,
    'graph1AX' : graph1AX,
    'graph1AY' : graph1AY,
    'graphSub1AX' : graphSub1AX,
    'graphSub1AY' : graphSub1AY,
    'graph1BX' : graph1BX,
    'graph1BY' : graph1BY,
    'graphSub1BX' : graphSub1BX,
    'graphSub1BY' : graphSub1BY,
    'graph2AX' : graph2AX,
    'graph2AY' : graph2AY,
    'graph2AXP' : graph2AXP,
    'graph2AYP' : graph2AYP,
    'graph2BX' : graph2BX,
    'graph2BY' : graph2BY,
    'graph2BXP' : graph2BXP,
    'graph2BYP' : graph2BYP,
    'graph3AY' : graph3AY,
    'graph3AX' : graph3AX,
    'graph3BY' : graph3BY,
    'graph3BX' : graph3BX,
    # 'gapa1AX' : gapa1AX ,
    'd' : arr,
    'd2' : arr2,
    # 'm' : m,
    'tSum2P' : tSum2P,
    'tSumB2P' : tSumB2P,
    'graph1AX2P' : graph1AX2P,
    'graph1AY2P' : graph1AY2P,
    'graph1BX2P' : graph1BX2P,
    'graph1BY2P' : graph1BY2P,
    'dfGroupH' : dfGroupH
    
    }
    return context  

# Routes
                        
def map(request):
    data = initialise_chart()
    # data['m'] = m
    return render(request, 'map.html', data)

# def highlight_region(selected_region, geojson_layer):
#     for feature in geojson_layer.data['features']:
#         region_name = feature['properties']['region']
#         if region_name == selected_region:
#             feature['properties']['style'] = {'fillColor': 'yellow', 'fillOpacity': 0.6}
#         else:
#             feature['properties']['style'] = {'fillOpacity': 0.2}
#     geojson_layer.style_function = lambda feature: feature['properties']['style']

def update_charts(request):
    
    selected_year = request.GET.get("year")
    selected_region = request.GET.get("region")
    

    if selected_year == "2008":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2008.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2008.csv')        
    elif selected_year == "2008_Re-election":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2008_Re-election.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2008_Re-election.csv')        
    elif selected_year == "2012":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2012.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2012.csv')       
    elif selected_year == "2016":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2016.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2016.csv')        
    elif selected_year == "2020":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2020.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2020.csv')
    else:
        return JsonResponse({"error": "Invalid selection."})

    if not selected_region:
        data = initialise_chart(selected_year)

    else:
        data = initialise_chart(selected_year, selected_region)

    
        # highlighted_region_data = highlight_region(selected_region, g)  # Assuming 'g' is your GeoJSON layer
        # data['highlighted_region'] = highlighted_region_data
    return JsonResponse(data)


def selectCensus(request):

    census = request.GET.get('census')
    year = request.GET.get('year')
    region = request.GET.get('region')

    
    filename3 = 'District_pop_demographics' + year + '.csv' 
    path3 = os.path.join(data_loc_str, 'EDATA', filename3)
    df3 = gpd.read_file(path3)   
    
    grouped2P = df3.groupby(['Region'])
    dfGroup2P = grouped2P.get_group(region) 

     #________________________________

    #// POPULATION DATA PROCESSING//

    #_______________________________

   # // Finding the Total Pop in relation to the Regions
    dfGroupA2P = df3[["Region", census]] # Selecting specific columns and getting rid of the commas in the string
    dfGroupA2P[census] = dfGroupA2P[census].astype('float') # Converting all the string in the columns to integers
    tSum2P = dfGroupA2P[census].values.sum() # Sum operation on a specific column
    dfContinentSum2P = dfGroupA2P.groupby(by=["Region"])[census].sum().reset_index()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census]

    # // Finding the Total Pop in relation to the Districts
    dfGroupB2P = dfGroup2P[["Constituency", census]] # Selecting specific columns and getting rid of the commas in the string
    dfGroupB2P[census] = dfGroupB2P[census].astype('float') # Converting all the string in the columns to integers
    tSumB2P = dfGroupB2P[census].values.sum() # Sum operation on a specific column
    dfContinentSumB2P = dfGroupB2P.groupby(by=["Constituency"])[census].sum().reset_index()
    graph1BX2P = dfContinentSumB2P['Constituency'].values.tolist()
    graph1BY2P = dfContinentSumB2P[census]

    #// List of the header columns
    dfGroupH = df3.columns.tolist()[3:-1]
    
    tSum2P = dfGroupA2P[census].values.sum().astype('float').tolist()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census].values.tolist()

    tSumB2P = dfGroupB2P[census].values.sum().astype('float').tolist()
    graph1BX2P = dfContinentSumB2P['Constituency'].values.tolist()
    graph1BY2P = dfContinentSumB2P[census].values.tolist()


    context = {

    'tSum2P' : tSum2P,
    'tSumB2P' : tSumB2P,
    'graph1AX2P' : graph1AX2P,
    'graph1AY2P' : graph1AY2P,
    'graph1BX2P' : graph1BX2P,
    'graph1BY2P' : graph1BY2P,
    'dfGroupH' : dfGroupH
    
    }

    return JsonResponse(context)

# def about(request):
#    context = {

#    }

#    return render(request, 'index.html', context)



    
# def reset_map(request):
#     selected_year = request.GET.get("year")
    
#     selected_region = request.GET.get("region")
    
#     if selected_year in ["2008", "2008_Re-election", "2012", "2016"]:
#         geojson_layer = g
#     else:
#         geojson_layer = g2
    
#     highlight_region(selected_region, geojson_layer)  # Update the GeoJSON layer styling
    
#     # Get the GeoJSON data for the highlighted region layer
#     highlighted_geojson_data = geojson_layer.to_dict()
    
#     return JsonResponse({"highlighted_geojson_data": highlighted_geojson_data})



