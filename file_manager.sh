#!/bin/bash
while true
do
echo "===================================="
echo " MINI FILE MANAGER SYSTEM"
echo "===================================="
echo "1. Show Current Directory"
echo "List Files (ls)"
echo "Create Directory (mkdir)"
echo "Change Directory (cd)"
echo "Create File (touch)"
echo "Edit File (vim)"
echo "Delete File"
echo "Exit"
echo "======================================"
read -p "Enter your choice:" choice
case $choice in
1) 
echo "Current Directory:"
pwd
;;
2)
echo "Files in Directory:"
ls
;;
3)
read -p "Enter directory name: " dirname
mkdir $diname
echo "Directory created!"
;;

4)
read -p "Enter directory naem to move: " dir
cd $dir 2>/dev/null
if [$? -eq 0 ]
then
	echo "Moved to $dir"
else
	echo "Directory not found!"
fi 
;;
5) 
read -p "enter file name: " fname
touch $fname
echo "File createdd!"
;;
6)
read -p "Enter file name to edit: " editfile
vim $editfile
;;

7)
read -p "Enter file name to delete: " delfile
rm -- $delfile
;;
8)
echo "Exiting..."
break
;;

*)
echo "Invalid choice!"
;;

esac
echo ""
read -p "Press Enter to continue..."
done
