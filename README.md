# CooperativeCoptersWanding
 Used to define a trajectory for flight trough drawing a path with the wand in Motiv
 
 ### Steps to Run the Program:
 1. Begin Motiv motion capture and define the wand as a rigid body
 2. Place the wand on the ground and begin recording a session in Motiv
 3. Move the wand in any desired path
 4. Finish recording and export the recording as a CSV file. This saves the position, orientation, and time of each frame of the rigid body
 5. Remove the wand as a rigid body in Motiv and define the drones and payload as rigid bodies
 6. Go to Trajectory_Planner and change the file location in extract_traj to the new one exported
 
