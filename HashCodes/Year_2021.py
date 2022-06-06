input_file_name = 'a.txt'
output_file_name = 'a.out'


if __name__ == '__main__':
    with open(input_file_name, 'r') as file1:
        input_lines = file1.readlines()

    allInput = []

    for line in input_lines:
        allInput.append(line.split())

    # Duration, Intersections, Streets, Cars, BonusPoints
    D, I, S, V, F = map(int, allInput[0])

    streets = allInput[1:S+1]
    paths = allInput[S+1:S+V+1]
    traffic_light_intersections = set()


    for ii in paths:
        for zz in range (1,1 + int(ii[0])):
            found = filter(lambda x:x[2]==ii[zz],streets)
            for ww in found:
                ii.append([ww[0],ww[1],ww[3]])
                if zz < int(ii[0]):
                    traffic_light_intersections.update(ww[1])

    number_of_lights = len(traffic_light_intersections)

    f = open(output_file_name, 'w')
    f.write(str(number_of_lights)+'\n')


    for ii in range(0,number_of_lights):
        nextitem = traffic_light_intersections.pop()
        f.write(nextitem+'\n')

        found = filter(lambda x:x[1]==nextitem,streets)
        count = 0
        temp_streets = []
        for ww in found:
            temp_streets.append(ww[2])
            count = count + 1

        f.write(str(count)+'\n')
        for yy in temp_streets:
            f.write(yy +' 1\n')

    f.close()