
"""
######################
Notes
it used for getting north of Georges Bank and Gulf of Maine eMOLT data based on different conditions()
After running this program, you can get  a file of eMOLT data
The  file will be saved in same folder as this program named by the smallest latitude you input
input values: time period,gbox(maxlon, minlon,maxlat,minlat),depth(deep,low),sites,polygon sites
function uses:getobs_tempsalt_bysite,getobs_tempsalt_byrange,getemolt_ctl,point_in_poly
output : a data file which includes sites, time, lat,lon,temp,depth

@author: huanxin
"""

######################################

import sys
import os

ops=os.defpath
pydir='../'
sys.path.append(pydir)
from hx import getemolt_ctl,point_in_poly,getobs_tempsalt_bysite,getobs_tempsalt_byrange


inputfilename='./getemolt_ctl.txt' # control file path
input_time,depth,gbox,polygon,site=getemolt_ctl(inputfilename)  # get input values from control file

f = open(str(gbox[3])+'.dat', 'w')  # create file and name it
f.writelines('site'+'         '+'lat         '+' lon        '+' depth(m)'+'    '+'      time'+'              '+'temp(C)'+'\n')
#write title
if site=='':
    time,sea_water_temperature,depth2,sites,lat,lon=getobs_tempsalt_byrange(gbox,depth,input_time) #get data
    for k in range(len(sites)):
       if polygon=='':
           
           f.writelines(str(sites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth2[k]+'      '\
           +str(time[k].strftime('%Y-%m-%d %H:%M:%S'))+'       '+str(sea_water_temperature[k])+'\n')
       else: # judge a site in or out of the polygon
           inside=point_in_poly(lon[k],lat[k],polygon)
           if inside == True:
                      f.writelines(str(sites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth2[k]+'      '\
                      +str(time[k].strftime('%Y-%m-%d %H:%M:%S'))+'       '+str(sea_water_temperature[k])+'\n')
           else:
               continue
else:
    for q in range(len(site)):
        time,sea_water_temperature,depth2,sites,lat,lon=getobs_tempsalt_bysite(site[q],input_time,depth) #get data
        for k in range(len(sites)): 
           f.writelines(str(sites[k])+'    '+'%10.2f' % lat[k]+'   '+'%10.2f' % lon[k]+'   '+'%10.2f' % depth2[k]+'      '\
           +str(time[k].strftime('%Y-%m-%d %H:%M:%S'))+'       '+str(sea_water_temperature[k])+'\n')

f.close()
