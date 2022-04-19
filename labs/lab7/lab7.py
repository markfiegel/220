"""
Mark Fiegel
lab7.py
I made a program that reads a file, does computations, and then writes a new one
I certify that this assignment is entirely my own work.
"""
def weighted_average(in_file_name,out_file_name):
    file = open(in_file_name, "r")
    new_line = file.read().split('\n')
    file.close()
    average = 0
    counter = 0
    lineup = ''
    for i in range(len(new_line)):
        lines = new_line[i]
        splitter =lines.split(':')
        y = splitter[1].lstrip()
        num_split = y.split(' ')
        avg_accum = 0
        weights = 0
        for p in range(0,len(num_split),2):
            tp = float(num_split[p])*float(num_split[p+1])/100
            weights += float(num_split[p])
            avg_accum += tp
        if weights < 100:
            writer = '{name}\'s average: error weights are less than 100'.format(name = splitter[0])
        elif weights > 100:
            writer = '{name}\'s average: error weights are higher than 100'.format(name = splitter[0])
        elif weights == 100:
            writer = '{name}\'s average: {average}'.format(name = splitter[0], average = avg_accum )
            average +=avg_accum
            counter += 1
        lineup += f"{writer}\n"
        if i == len(new_line)-1:
            lineup += f"Class average: {average/counter}"
            new_file = open(out_file_name,'w')
            new_file.write(lineup)
            new_file.close()
def main():
    weighted_average('grades.txt','avg.txt')
main()
#ignore the next few lines, dont know how to get them off github haha