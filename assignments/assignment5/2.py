class Sensor:
    """
    Attributes:
    name is a string type
    reading_list is a list
    """
    def __init__(self,name, reading_list):
        self.name = name
        self.reading_list = reading_list

    def __str__(self):
        return "Sensor({},{})".format(self.name,self.reading_list)

    def average(self):
        total = 0
        # get length of reading list
        number = len(self.reading_list)
        if number != 0:
            for i in range(0,number):
                reading = self.reading_list[i]
                total += reading
            average_number = total/number
            return round(float(average_number),1)
        else:
            return 0.0

    def trimmed_average(self):
       #length of reading list is more than and equal 3
        if len(self.reading_list) >= 3:
            #get smallest and largest reading
            smallest = min(self.reading_list)
            largest = max(self.reading_list)
            #remove smallest and largest reading
            self.reading_list.remove(smallest)
            self.reading_list.remove(largest)
            #calculate average
            total = 0
            for i in range(0, len(self.reading_list)):
                reading = self.reading_list[i]
                total += reading
            trimmed_average = total / len(self.reading_list)
            return round(trimmed_average,1)
        else:
            return self.average()

    def is_alert(self,threshold):
        flag = False
        result = self.trimmed_average()
        if result >= threshold:
            flag = True
        return flag


class Network:
    def __init__(self,sensors_list):
        self.sensors_list = sensors_list

    def add_Sensor(self,sensor):
        network = Network()
        original_list = network.sensors_list
        #add new sensor
        original_list.append(sensor)

    def overall_average(self):
        #get all readings of this network
        sensors = self.sensors_list
        if len(sensors) >0:
            overall = 0
            overall_number = 0
            # get every sensors in sensor list
            for sensor in sensors:
                #get reading_list of a sensor
                reading_list = sensor.reading_list
                overall_number = overall_number + len(reading_list)
                for reading in reading_list:
                    #get every readings
                    overall = overall+reading
            # calculate average
            overall_average = round(overall/overall_number,1)
            return overall_average
        else:
            return 0.0


#MAIN
#create sensors
sensors_list=[]
sensors_number = int(input("Enter number of sensors: "))
for i in range(0,sensors_number):
    sensor_name = input("Enter name: ")
    #ask readings for sensor
    readings_number = int(input("Enter number of readings: "))
    reading_list =[]
    for j in range(0,readings_number):
        reading = float(input("Enter reading: "))
        reading_list.append(reading)
    sensor = Sensor(sensor_name,reading_list)
    sensors_list.append(sensor)
# add sensor into network
network = Network(sensors_list)
#read an alert threshold
threshold = float(input("Enter alert threshold: "))
#get overall average
overall_average = network.overall_average()
#print overall average
print()
print("Overall average: {}".format(overall_average))
#list all sensors whose average is at least the threshold
print("Sensors above threshold (trimmed avg >= {}):".format(float(threshold)))
#determine whether sensors are above threshold
for sensor in sensors_list :
    # determine whether sensors are above threshold
    flag = sensor.is_alert(threshold)
    if flag :
        print("{} - {}".format(sensor.name,sensor.trimmed_average()))




