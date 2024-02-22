### Creating mistro connection and getpass ###
from mstrio.connection import Connection
from getpass import getpass

### Creating function to import the contents of a published Cube into a DataFrame ###
from mstrio.project_objects import load_cube, OlapCube
my_cube = OlapCube(connection=conn, id=id)
my_cube = load_cube(connection=conn, cube_id=cube_id)
cube_df = my_cube.to_dataframe()
# cube_df.print() would give general idea about published cube. 

### Creating reports DataFrame ###
from mstrio.project_objects import Report
my_report = Report(connection=conn, report_id=report_id, parallel=False)
reports_df = my_report.to_dataframe()
# reports_df.print() will print the reports accordingly. 


### There are several enhanchemnts like we can apply filters by apply_filters() methods, get attributes metrics and create multi level tables using mstrio-py. 
###
