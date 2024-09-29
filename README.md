# autoassign_nodeid
This project is for automatically assigning node ids for multiple slave stations in serial communication sequence.

This can find many applications where any master stations need to assign a nodeid atomatically to multiple slave stations in sequential fashion.

/Docs/concept.pdf explains the concept and arrangement of slaves in a sequence in back to back fashion.

/MCU_test/ contains slave target card design which is based on RS485 bus. Sample Arduino code for master and 2 slaves is also in this directory.

/App/Tool is where there will be source code of a tool to develop a GUI software tool which will configure these slave stations so that Master can configure them automaically and poll data from them.

This tool is based on Python and wxPython library is being used.


# latest update
I am planning to migrate the development of target device on stm32 based MCU and Client software on .Net core framework. work in progress as I am not an expert of .Net
