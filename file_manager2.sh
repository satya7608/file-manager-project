#!/bin/bash

# ===== CONFIG =====
PASSWORD="1234"
LOGFILE="file_manager.log"
START_TIME=$(date +%s)

# ===== COLORS =====
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# ===== LOGIN =====
echo -e "${CYAN}===== LOGIN REQUIRED =====${NC}"
read -s -p "Enter Password: " pass
echo ""

if [ "$pass" != "$PASSWORD" ]; then
    echo -e "${RED}Access Denied!${NC}"
    exit
fi

echo -e "${GREEN}Login Successful!${NC}"
sleep 1
clear

# ===== LOG FUNCTION =====
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> $LOGFILE
}

# ===== MAIN LOOP =====
while true
do
    echo -e "${CYAN}==============================="
    echo -e "   MINI FILE MANAGER PRO"
    echo -e "===============================${NC}"
    echo -e "${YELLOW}1. List Files"
    echo "2. Create File"
    echo "3. Delete File"
    echo "4. Rename File"
    echo "5. View File"
    echo "6. Create Directory"
    echo "7. Delete Directory"
    echo "8. Show Path"
    echo "9. Exit${NC}"
    echo "==============================="

    read -p "Enter choice: " ch

    case $ch in

        1)
            ls -lh
            log_action "Listed files"
            ;;

        2)
            read -p "File name: " f
            touch "$f"
            echo -e "${GREEN}File created${NC}"
            log_action "Created file $f"
            ;;

        3)
            read -p "File name: " f
            rm -f "$f"
            echo -e "${RED}File deleted${NC}"
            log_action "Deleted file $f"
            ;;

        4)
            read -p "Old name: " o
            read -p "New name: " n
            mv "$o" "$n"
            echo -e "${GREEN}Renamed${NC}"
            log_action "Renamed $o to $n"
            ;;

        5)
            read -p "File name: " f
            cat "$f"
            log_action "Viewed file $f"
            ;;

        6)
            read -p "Directory name: " d
            mkdir "$d"
            echo -e "${GREEN}Directory created${NC}"
            log_action "Created directory $d"
            ;;

        7)
            read -p "Directory name: " d
            rm -r "$d"
            echo -e "${RED}Directory deleted${NC}"
            log_action "Deleted directory $d"
            ;;

        8)
            pwd
            log_action "Checked path"
            ;;

        9)
            END_TIME=$(date +%s)
            DURATION=$((END_TIME - START_TIME))
            echo -e "${CYAN}Session Time: $DURATION seconds${NC}"
            log_action "Exited program (Session $DURATION sec)"
            exit
            ;;

        *)
            echo -e "${RED}Invalid choice!${NC}"
            ;;

    esac

    echo ""
    read -p "Press Enter to continue..."
    clear

done
