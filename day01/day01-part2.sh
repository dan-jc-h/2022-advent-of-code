awk -f day01-part2.awk day01-input-data.txt | sort -nr | head -3 | awk 'BEGIN {sum=0};{sum = sum + $1};END{print(sum)}'
