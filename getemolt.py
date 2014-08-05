
"""
######################
Notes
it uses for getting emolt data based on different conditions()
After running this program, you can get emolt data into a file
The saving file will be in same floder as this program

@author: huanxin
"""
import datetime as dt
import sys
import os
import pytz
import pandas as pd
from dateutil.parser import parse
ops=os.defpath
pydir='../'
sys.path.append(pydir)

def getobs_tempsalt_bysite(site,input_time):
    """
Function written by Jim Manning and used in "modvsobs" and "getemolt",it was modified by Huanxin
get data from url, return depth temperature,latitude,longitude, and start and end times
input_time can either contain two values: start_time & end_time OR one value:interval_days
and they should be timezone aware
example: input_time=[dt(2003,1,1,0,0,0,0,pytz.UTC),dt(2009,1,1,0,0,0,0,pytz.UTC)]
"""
    mintime=input_time[0].strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')  # change time format
    maxtime=input_time[1].strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')    
   
    url='http://comet.nefsc.noaa.gov:8080/erddap/tabledap/eMOLT.csv?SITE,time,depth,sea_water_temperature,latitude,longitude&time>='\
    +str(mintime)+'&time<='+str(maxtime)+'&SITE="'+str(site)+'"&orderBy("depth,time")'
    df=pd.read_csv(url,skiprows=[1])
    for k in range(len(df)):
       df.time[k]=parse(df.time[k])

    return df.time.values,df.sea_water_temperature.values,df.depth.values,df.SITE.values,df.latitude.values,df.longitude.values

def getobs_tempsalt_byrange(gbox,depth,input_time):
    """
Function written by Huanxin and used in "getemolt"
get data from url, return depth temperature,latitude,longitude, and start and end times
gbox includes 4 values, maxlon, minlon,maxlat,minlat, like:  [-69.0,-73.0,41.0,40.82]
depth includes bottom depth and surface depth,like:  [80,0]
input_time can either contain two values: start_time & end_time OR one value:interval_days
and they should be timezone aware
example: input_time=[dt(2003,1,1,0,0,0,0,pytz.UTC),dt(2009,1,1,0,0,0,0,pytz.UTC)]
"""
    i_maxdepth=depth[0];i_mindepth=depth[1];lon_max=gbox[0];lon_min=gbox[1];lat_max=gbox[2];lat_min=gbox[3]
    mintime=input_time[0].strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')  # change time format
    maxtime=input_time[1].strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')
    url='http://comet.nefsc.noaa.gov:8080/erddap/tabledap/eMOLT.csv?SITE,time,depth,sea_water_temperature,latitude,longitude&time>='\
    +str(mintime)+'&time<='+str(maxtime)+'&depth<='+str(i_maxdepth)+'&depth>='+str(i_mindepth)+'&latitude>='\
    +str(lat_min)+'&latitude<='+str(lat_max)+'&longitude>='+str(lon_min)+'&longitude<='+str(lon_max)+'&orderBy("SITE,depth,time")'
    df=pd.read_csv(url,skiprows=[1])
    for k in range(len(df)):
       df.time[k]=parse(df.time[k])
    return df.time.values,df.sea_water_temperature.values,df.depth.values,df.SITE.values,df.latitude.values,df.longitude.values
    



input_time=[dt.datetime(2003,1,1,0,0,0,0,pytz.UTC),dt.datetime(2009,1,1,0,0,0,0,pytz.UTC)] # start time and end time
gbox=[-69.0,-73.0,41.0,40.82] #  maxlon, minlon,maxlat,minlat
depth=[80,0]  #bottom depth,    surface depth
site=['SO07','ST02']   # if you do not want to input site, write: site=''
f = open(str(gbox[3])+'.dat', 'w')  # create file and name it
f.writelines('site'+'         '+'lat         '+' lon        '+' depth(m)'+'    '+'      time'+'              '+'temp(C)'+'\n')
if site=='':
    time,sea_water_temperature,depth2,sites,lat,lon=getobs_tempsalt_byrange(gbox,depth,input_time)
    for k in range(len(sites)):
       f.writelines(str(sites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth2[k]+'      '\
       +str(time[k].strftime('%Y-%m-%d %H:%M:%S'))+'       '+str(sea_water_temperature[k])+'\n')
 
else:
    for q in range(len(site)):
        time,sea_water_temperature,depth2,sites,lat,lon=getobs_tempsalt_bysite(site[q],input_time)
        for k in range(len(sites)): 
           f.writelines(str(sites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth2[k]+'      '\
           +str(time[k].strftime('%Y-%m-%d %H:%M:%S'))+'       '+str(sea_water_temperature[k])+'\n')

f.close()