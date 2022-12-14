# 2022 Advent of Code Day 1, part 2
#
# problem statement here: https://adventofcode.com/2022/day/1
#
# there's some potential issues here if the sorce is malformed
#     (multiple blank lines, non-numeric data etc.), but
#     I'll just assume that the input data is OK, because
#     data problems never happen.
#
# Note: Don't actually need elfWithMaxTotal, I initially mistakenly thought 
#     this was what was being asked for (... always read the problem...)
#
# This is for part 2 - so just spits out group totals to eb dealt with by other 
#     command line tools
#
# djch 2022-12-14

BEGIN{
    elfTotal=0;

}
{
    if (NF!=0){
        elfTotal = elfTotal + $1;
    }
    else {
        print(elfTotal)
        elfTotal = 0
    }
}
