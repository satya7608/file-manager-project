#!/bin/bash

echo "===== LOG ANALYZER ====="

file="system.log"

if [ ! -f "$file" ]; then
    echo "Log file not found!"
    exit 1
fi

echo ""
echo "1. Show full log"
echo "2. Show only ERROR"
echo "3. Show only WARNING"
echo "4. Show only INFO"
echo "5. Search keyword"
echo "6. Count ERROR"
echo "7. Count WARNING"
echo "8. Count INFO"
echo "9. Show user activity"
echo "10. Exit"

read -p "Enter choice: " ch

case $ch in

1)
    echo "Full Log:"
    cat $file
    ;;

2)
    echo "ERROR Logs:"
    grep "ERROR" $file
    ;;

3)
    echo "WARNING Logs:"
    grep "WARNING" $file
    ;;

4)
    echo "INFO Logs:"
    grep "INFO" $file
    ;;

5)
    read -p "Enter keyword: " key
    grep "$key" $file
    ;;

6)
    echo "Total ERROR:"
    grep -c "ERROR" $file
    ;;

7)
    echo "Total WARNING:"
    grep -c "WARNING" $file
    ;;

8)
    echo "Total INFO:"
    grep -c "INFO" $file
    ;;

9)
    echo "User Activity:"
    grep "User" $file
    ;;

10)
    echo "Exiting..."
    ;;

*)
    echo "Invalid choice"
    ;;

esac
