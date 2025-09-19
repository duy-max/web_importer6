#!/bin/bash

# Script chạy pytest 100 lần, tạo HTML report riêng cho mỗi lần
status=0

# Tạo thư mục lưu report nếu chưa tồn tại
mkdir -p reports

for i in $(seq 1 100); do
    echo "==== RUNNING TEST ROUND $i ===="
    pytest tests --html=reports/report_$i.html --self-contained-html || status=1
done

# Thông báo vị trí report
echo "All reports saved in ./reports/"

# Exit code cuối cùng
exit $status
