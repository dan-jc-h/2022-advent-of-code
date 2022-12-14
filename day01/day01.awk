# 2022 Advent of Code Day 1
#
# problem statement here: https://adventofcode.com/2022/day/1
#
# there's some potential issues here if the sorce is malformed
#     (multiple blank lines, etc.)
#
# djch 2022-12-14

BEGIN{
    elfNum=1;
    elfTotal=0;
    elfMaxTotal=0;
    elfWithMaxTotal=0;
}
{
    if (NF!=0){
        elfTotal = elfTotal + $1;
        print elfNum, $1, elfTotal, elfWithMaxTotal, elfMaxTotal
    }
    else {
        print("---")
        if (elfTotal > elfMaxTotal){
            elfMaxTotal = elfTotal
            elfWithMaxTotal = elfNum
        }
        elfNum = elfNum + 1
        elfTotal = 0
    }
}
END{
    print elfWithMaxTotal
}