# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:26:15 2013

@author: hxu
"""
import datetime as dt


def getemolt_ctl_py():
   select=[1,0,0,1,0,0]
   dtime='[2003,8,25,0,1;2003,8,27,0,0]'
   idepth=[10,200]
   bdepth=[20,200]
   latlon=[4642,7116,4162,6648] #
   polygon=[(-7106,4316),(-6984,4435),(-6743,4552),(-6659,4440),(-6967,4246)]
   site=''   # like  DJ01,PF01
   num=1
#######################################################
########################################################
#The first line represent index of the following 5 line,'1' means picking,'0' means not.
#the 2nd line represent the period of date
#the 3rd line represent the range depth of sensor
#the 4th line represent the range depth of bottom
#the 5th line represent the range lat,lon of range:maxlat,maxlon,minlat,minlon
#the 6th line is working for polygon, you can select sites by a special range
#the 7th line represent the sites you need, use "," to split
#the 8th line represent how many periods(the 2nd line) you want
####################################################

   select1=select[0]
   select2=select[1]
   select3=select[2]
   select4=select[3]
   select5=select[4]
   select6=select[5]
   if select1 ==1:
       dtime=dtime[0:dtime.index(']')].strip('[').split(';')
       mindtime=dt.datetime.strptime(dtime[0],'%Y,%m,%d,%H,%M')
       maxdtime=dt.datetime.strptime(dtime[1],'%Y,%m,%d,%H,%M') 
   if select2 ==1:
       i_mindepth=float(idepth[0])
       i_maxdepth=float(idepth[1])
   else:
       i_mindepth=0
       i_maxdepth=2000

       
   if select3 ==1:
       b_mindepth=float(bdepth[0])
       b_maxdepth=float(bdepth[1])
   else:
       b_mindepth=0
       b_maxdepth=2000
       
   if select4 ==1:
       lat_max=float(latlon[0])
       lon_max=float(latlon[1])
       lat_min=float(latlon[2])
       lon_min=float(latlon[3])
   else:
       lat_max=5000
       lon_max=5000  
       lat_min=3000
       lon_min=8000
   if select5 ==1:
       polygon=polygon
   else:
       polygon==''     
   if select6 ==1:
       site=site[0:site.index(']')].strip('[').split(',') 
   else:
       site=''


   return mindtime,maxdtime,i_mindepth,i_maxdepth,b_mindepth,b_maxdepth,lat_max,\
   lon_max,lat_min,lon_min,polygon,site,num