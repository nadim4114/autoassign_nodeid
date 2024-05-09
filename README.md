# autoassign_nodeid
This project is for automatically configuring node ids for multiple slave stations in serial commuinccation sequence.
This can find many applications where any slave stations need to assign a node This can find many applications where any slave stations need to assign a node 
/Docs/concept.pdf explains the concept and arrangement of slaves in a sequence.
/MCU_test/ contains card design which is based on RS485. Sample Arduno code for master and 2 slaves is also in this directory.
/App/Tooll is where I am working on a tool to develop a GUI configuration tool which will configure these slave stations so that Master can configure them automaically and poll data from them.

This tool is based on Python and wxPython library is being used.
