getemolt
========

gets eEMOLT data , organize and save it in a file


gets north of Georges Bank and Gulf of Maine eMOLT data based on different conditions()

before you run it, please modify control file "getemolt_ctl.txt" first.

After running this program, you can get a file of eMOLT data

The  file will be saved in same folder as this program named by the smallest latitude you input

input values: time period,gbox(maxlon, minlon,maxlat,minlat),depth(deep,low),sites,polygon sites

function uses:getobs_tempsalt_bysite,getobs_tempsalt_byrange,getemolt_ctl,point_in_poly

output : a data file which includes sites, time, lat,lon,temp,depth
