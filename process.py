log_file = open("um-server-01.txt")


def sales_reports(log_file):
    #creates function to run report
    for line in log_file:
        #going through each line from the file
        line = line.rstrip()
        #removes spaces from each line from file
        day = line[0:3]

        if day == "Mon":
            print(line)


sales_reports(log_file)
