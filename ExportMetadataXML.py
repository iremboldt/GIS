import arcpy 
from arcpy import env 
import os
from arcpy import metadata as md

#This is the location of the database connection file, e.g. r"C:\Users\Isaac.Remboldt\AppData\Roaming\Esri\ArcGISPro\Favorites\DOT_GIS_Admin.sde"
workpace = arcpy.GetParameterAsText(0)
#A simple folder location, wherever you want the outputs to be saved.
savelocation = arcpy.GetParameterAsText(1)

#If running directly in the python window, this can just be the same link as "workspace" above
env.workspace = workspace

#This creates a list of the feature classes in a geodatabase
fcList = arcpy.ListFeatureClasses()
#This creates a list of the tables in a geodatabase
tableList = arcpy.ListTables()
#This creates a list of the relationship classes in a geodatabase
relList = [c.name for c in arcpy.Describe(env.workspace).children if c.datatype == "RelationshipClass"]

#This will create a text file in the savelocation. The names of each item is written to the documents so you have a text file with all items in the GDB
print ("Opening Text File")
txtFCList = savelocation + "\\FeatureList.txt"
txtTableList = savelocation + "\\TableList.txt"
txtRelList = savelocation + "\\RelList.txt"

#This opens the text file for features
txtFCFile = open(txtFCList,"w")

print ("Beginning looping through feature classes")
for fc in fcList:
	print (fc)
	save_path = savelocation + "\\" + fc
    path = env.workspace + "\\" + fc
    #Uses the workspace path plus the feature class name to create the full path for the fc
    path_md = md.Metadata(path)
    #This exports the metadata xml into the save folder in FGDC_CSDGM format, and includes all information
    path_md.exportMetadata(save_path, 'FGDC_CSDGM', 'EXACT_COPY', '')
    #The name of the fc is written into the text file
	txtFCFile.write(fc)
	txtFCFile.write(os.linesep)

#Once all the feature classes have been looped through, the text file is saved and closed
print ("Finished Looping through feature classes, saving text file")
txtFCFile.close()

#This is the same process as the feature class loop, but with tables
txtTableFile = open(txtTableList,"w")

print ("Beginning looping through tables")
for table in tableList:
	print (table)
	save_path = savelocation + "\\" + table
    path = env.workspace + "\\" + table
    path_md = md.Metadata(path)
    path_md.exportMetadata(save_path, 'FGDC_CSDGM', 'EXACT_COPY', '')
    txtTableFile.write(table)
	txtTableFile.write(os.linesep)
    
print ("Finished Looping through tables, saving text file")
txtTableFile.close()

#This is the same process as the feature class loop, but with relationship classes
txtRelFile = open(txtRelList,"w")

print ("Beginning looping through relationship classes")
for rel in relList:
	print (rel)
	save_path = savelocation + "\\" + rel
    path = env.workspace + "\\" + rel
    path_md = md.Metadata(path)
    path_md.exportMetadata(save_path, 'FGDC_CSDGM', 'EXACT_COPY', '')
    txtRelFile.write(table)
	txtRelFile.write(os.linesep)

print ("Finished Looping through relationship classes, saving text file")
txtRelFile.close()

print ("Finished Looping through feature classes, saving text file")

print ("done")

