#This program allows a freelance video producer to save the running times to a file and 
#adds the total running time together.

def main():

    #Get the number of videos in the project
    project_videos = int(input("Enter the number of videos: "))

    #open the file
    output_file = open("running_time.txt", 'w')

    for count in range(1, project_videos + 1):
        #get the videos running time
        running_time = float(input("Enter the video's running time: "))

        #Write to the file
        output_file.write(str(running_time) + " \n")

    #close the file
    output_file.close()

    #inform the user that data has been written to the file
    print("Data has been written to the file.")

    #call the read_running_times method
    read_running_times()

def read_running_times():
    #initialzie an accumulator 
    accumulator = 0

    #initialize a count variable to 0
    count = 0

    #open the file
    output_file = open('running_time.txt', 'r')

    for line in output_file:
        #convert a line to a float
        run_time = float(line)

        #add 1 to the count
        count += 1 

        #display the running time
        print('Video #', count , ' : ', run_time, sep = '')

        #add the time to total
        accumulator += run_time

        #close the file 
    output_file.close()

    #display the running time
    print("The running time is ", accumulator, " seconds")

main()