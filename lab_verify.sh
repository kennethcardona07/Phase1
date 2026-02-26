#!/bin/bash
LOG="setup_verify.txt"
echo "--- FELLOWSHIP LAB REPORT ---"  > $LOG
echo "User: $USER | Host: $(hostname)" >> $LOG
date >> $LOG 
echo "Audit Complete."

