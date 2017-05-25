import sys
import Gnuplot


if len(sys.argv) != 6:
    print(
        "\n\nInvalid number of arguments!\n"
        "\nArg. 1: folder with .dat files"
        "\nArg. 2: number of files to plot"
        "\nArg. 3: lower limit of dimensions"
        "\nArg. 4: upper limit of dimensions"
        "\nArg. 5: output gif file full path (do not put extension)\n\n")
else:
    folder = str(sys.argv[1])
    max_steps = str(sys.argv[2])
    min_range = str(int(sys.argv[3]))
    max_range = str(int(sys.argv[4]))
    output_file_name = str(sys.argv[5])

    range_str = "[" + min_range + ":" + max_range + "]"

    try:
        file_name = folder + "/step0.dat"
        print(file_name)
        file = open(file_name)
    except IOError:
        print("\nCannot open " + file_name + ".\n")
    else:
        number_of_dimensions = len(file.readline().strip().split()) - 1

        if number_of_dimensions != 2 and number_of_dimensions != 3:
            print("\nNumber of dimensions must be 2 or 3!\n")
        else:
            g = Gnuplot.Gnuplot()

            if number_of_dimensions == 2:
                # 2D
                g("set terminal gif anim delay 5")
                g("set xrange " + range_str)
                g("set yrange " + range_str)
                g("unset colorbox")
                g("set output '" + output_file_name + "_plot.gif'")
                g("do for [i=1:" + max_steps + "] { plot sprintf('" +
                    folder + "/step%d.dat', (i-1)) u 1:2:3 "
                    "with points pt 7 ps 0.5 palette notitle }")

                # 3D
                g("set terminal gif anim delay 5")
                g("set xrange " + range_str)
                g("set yrange " + range_str)
                g("unset colorbox")
                g("set output '" + output_file_name + "_splot.gif'")
                g("do for [i=1:" + max_steps + "] { splot sprintf('" +
                    folder + "/step%d.dat', (i-1)) u 1:2:3 "
                    "with points pt 7 ps 0.5 palette notitle }")

            elif number_of_dimensions == 3:
                # 3D
                g("set terminal gif anim delay 5")
                g("set xrange " + range_str)
                g("set yrange " + range_str)
                g("set zrange " + range_str)
                #g("unset colorbox")
                g("set output '" + output_file_name + "_splot.gif'")
                g("do for [i=1:" + max_steps + "] { splot sprintf('" +
                    folder + "/step%d.dat', (i-1)) u 1:2:3:4 "
                    "with points pt 7 ps 0.5 palette notitle }")
