getemolt
========

gets eEMOLT data , organizes and saves it in a file


gets  eMOLT data based on different conditions()

before you run it, please modify control file "getemolt_ctl.txt" first.

After running this program, you can get a file of eMOLT data

The  file will be saved in same folder as this program named by the datetime you create

input values: time period,gbox(maxlon, minlon,maxlat,minlat),depth(deep,low),sites,polygon sites

function uses:getobs_tempsalt_bysite,getobs_tempsalt_byrange,getemolt_ctl,point_in_poly

output : a data file which includes sites, time, lat,lon,temp,depth

flowchart: 


<a href="https://github.com/xhx509/getemolt/blob/master/getemolt_flowchart.png">getemolt.py</a>
