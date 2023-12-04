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
    dfRegions = dfGroup[["REGION", "VALID_VOTES"]].copy()
    dfRegions['VALID_VOTES'] = dfRegions['VALID_VOTES'].replace(',','', regex=True)
    dfRegions['VALID_VOTES'] = dfRegions['VALID_VOTES'].astype('int')
    dfRegionsSum = dfRegions.groupby(by=["REGION"])["VALID_VOTES"].sum().reset_index()
    graph1AX = dfRegionsSum['REGION'].values.tolist()
    graph1AY = dfRegionsSum['VALID_VOTES']
    #print(dfRegionsSum)
    #print(graph1AX)

    # // Finding the Total sum based on each region for Presidential (B)
    dfRegions2 = dfGroup2[["REGION", "VALID_VOTES"]].copy()
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
    dfConst = dfGroupNew1[["CONSTITUENCY", "VALID_VOTES"]].copy()
    dfConst['VALID_VOTES'] = dfConst['VALID_VOTES'].replace(',','', regex=True)
    dfConst['VALID_VOTES'] = dfConst['VALID_VOTES'].astype('int')
    graphSub1AX = dfConst['CONSTITUENCY'].values.tolist()
    graphSub1AY = dfConst['VALID_VOTES'].values.tolist()
    #print(graphSub1AY)
    
    
    # // Have a column holding the sum operations of each constituency based on each region(Ashanti) Presidential for both offices (B)
    dfConst1B = dfGroupNew1B[["CONSTITUENCY", "VALID_VOTES"]].copy()
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

     #________________________________

    #// POPULATION DATA PROCESSING//

    #_______________________________

   # // Finding the Total Pop in relation to the Regions
    dfGroupA2P = df3[["Region", census]].copy() # Selecting specific columns and getting rid of the commas in the string
    dfGroupA2P[census] = dfGroupA2P[census].astype('float') # Converting all the string in the columns to integers
    tSum2P = dfGroupA2P[census].values.sum() # Sum operation on a specific column
    dfContinentSum2P = dfGroupA2P.groupby(by=["Region"])[census].sum().reset_index()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census]

    # // Finding the Total Pop in relation to the Districts
    dfGroupB2P = dfGroup2P[["Constituency", census]].copy() # Selecting specific columns and getting rid of the commas in the string
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
    elif selected_year == "2024":
        csv_path = os.path.join(data_loc_str, 'EDATA', '2024.csv')
        csv_path2 = os.path.join(data_loc_str, 'EDATA', 'District_pop_demographics2024.csv')
    else:
        return JsonResponse({"error": "Invalid selection."})

    if not selected_region:
        data = initialise_chart(selected_year)

    else:
        data = initialise_chart(selected_year, selected_region)

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
    dfGroupA2P = df3[["Region", census]].copy() # Selecting specific columns and getting rid of the commas in the string
    dfGroupA2P[census] = dfGroupA2P[census].astype('float') # Converting all the string in the columns to integers
    tSum2P = dfGroupA2P[census].values.sum() # Sum operation on a specific column
    dfContinentSum2P = dfGroupA2P.groupby(by=["Region"])[census].sum().reset_index()
    graph1AX2P = dfContinentSum2P['Region'].values.tolist()
    graph1AY2P = dfContinentSum2P[census]

    # // Finding the Total Pop in relation to the Districts
    dfGroupB2P = dfGroup2P[["Constituency", census]].copy() # Selecting specific columns and getting rid of the commas in the string
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

