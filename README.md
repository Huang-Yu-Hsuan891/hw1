# hw1
# in part 2
# first step, I remove the data whose value of the PRES (pressure) column is '-99.000' or '-999.000'.
# I use teacher give us command like target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
# and then we will get no pres is -99 and -999 value
# second step, I want to get the data about id is C0A880, C0F9A0, C0G640, C0R190, C0X260.
# so, I declare a list target_id = C0A880, C0F9A0, C0G640, C0R190, C0X260, and next for loop to search the data put into target_data.
# third step, the mean of  the ID of the station in the lexicographical order.
# so, I use for loop to calculate the ean value of pressure
# forth step,if ans is equal to zero, I give them name 'none'
# and print ans.
