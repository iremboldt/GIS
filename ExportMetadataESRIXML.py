import arcpy 
from arcpy import env 
import os
from arcpy import metadata as md

workpace = arcpy.GetParameterAsText(0)
savelocation = arcpy.GetParameterAsText(1)

env.workspace = workspace

fcList = arcpy.ListFeatureClasses()
tableList = arcpy.ListTables()
relList = [c.name for c in arcpy.Describe(env.workspace).children if c.datatype == "RelationshipClass"]

print ("Opening Text File")
txtFCList = savelocation + "\\FeatureList.txt"
txtTableList = savelocation + "\\TableList.txt"
txtRelList = savelocation + "\\RelList.txt"

txtFCFile = open(txtFCList,"w")

print ("Beginning looping through feature classes")
for fc in fcList:
	print (fc)
	save_path = savelocation + "\\" + fc
    path = env.workspace + "\\" + fc
    path_md = md.Metadata(path)
    pathxml = pathmd.xml
    file = open(savelocation+fc+".xml", "w")
    file.write(pathxml)
    file.close()
    
print ("Finished Looping through feature classes, saving text file")
txtFCFile.close()

txtTableFile = open(txtTableList,"w")

print ("Beginning looping through feature classes")
for table in tableList:
	print (table)
	save_path = savelocation + "\\" + table
    path = env.workspace + "\\" + table
    path_md = md.Metadata(path)
    pathxml = pathmd.xml
    file = open(savelocation+table+".xml", "w")
    file.write(pathxml)
    file.close()
    
print ("Finished Looping through tables, saving text file")
txtTableFile.close()

txtRelFile = open(txtRelList,"w")

print ("Beginning looping through feature classes")
for rel in relList:
	print (rel)
	save_path = savelocation + "\\" + rel
    path = env.workspace + "\\" + rel
    path_md = md.Metadata(path)
    pathxml = pathmd.xml
    file = open(savelocation+rel+".xml", "w")
    file.write(pathxml)
    file.close()

print ("Finished Looping through relationship classes, saving text file")
txtRelFile.close()

print ("Finished Looping through feature classes, saving text file")

print ("done")
