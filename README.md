# incling_example_project
Pre-Interview Task

This was a fun little exercise that allowed me to demonstrate how I would go about completing the task given.

Features 
  - Rest API Validates Orders Task assigned to a Tile. Tasks within a tile cannot have the same order number
  e.g. a Task , Titled 'First' assigned to a Tile with launch_date on the 22/11/2020 and Ordered in postion 1 
  and a  Task , Titled 'second' assigned to a Tile with launch_data on the 22/11/2020 and Ordered in postion 1 --- will not be valid 
  howerver a Task, Title 'Third' assigned to a Tile with a launch_data on the 28/11/2020 and Ordered in postion 1 --- will be valid
  
  -  Set up hyperlinks for the RestApi so you can go from a task to the assigned Tile and vice versa. 
  -  Tile Detail shows the tasks assigned to it
  
 
Things I would have done differently:
  - Started the project with a TDD approach
  - used fixtures to test and prepopulate the database
  - Abstract the user model and create a one to one relatonship with the TileObject
  
