# Component for discord bot to keep track of its best friends.
# Adds people who greet him to text file and keeps track of the
# persons points.
class BotFileHandler:
    def __init__(self, file):
        self.filename = file

    def get_top_friends_list(self):

        file_object = open(self.filename, 'r')
        name_list = []
        value_list = []
        sorted_list = []

        # Gather data into two lists: names and values
        for line in file_object:
            stats = line.split(":")
            name_list.append(stats[0])
            value_list.append(int(stats[1]))

        while (len(value_list) != 0):
            # Find out iterator of highest value in value_list
            max_value = max(value_list)
            i = value_list.index(max_value)

            # Add the corresponding name and value into sorted list,
            # delete from name- and value_list
            list_element = [name_list[i], value_list[i]]
            sorted_list.append(list_element)
            del name_list[i]
            del value_list[i]

        file_object.close()
        return sorted_list

    def get_top_friends_str(self):

        sorted_str = ""
        friends_list = self.get_top_friends_list()

        j = 1
        for friend in friends_list:
            sorted_str += str(j) + " " + friend[0] + "(" + str(friend[1])\
                          + ")" + "\n"
            j += 1
        return sorted_str

    def add_points(self, reciever, amount):

        friends_list = self.get_top_friends_list()
        not_found = True

        for i in range(amount):
            for friend in friends_list:
                if friend[0] == reciever:
                    friend[1] = friend[1] + 1
                    not_found = False
            if not_found:
                friends_list.append([reciever, 1])

        file_object = open(self.filename, 'w')

        for friend in friends_list:
            file_object.write(friend[0] + ":" + str(friend[1]) + "\n")

        file_object.close()
