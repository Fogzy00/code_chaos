import datetime
import pytz
import os

log_file_path = 'C:\Users\Fogzy\Documents\GitHub\code_chaos\Write Log File'
log_file_name = '\loggy.txt'
log_file = log_file_path + log_file_name
event_id = 1

 
# Get current date/timestamp
now = datetime.datetime.now(pytz.timezone('US/Central'))

# Assign date and time to variables (to be written later)
curr_date = now.strftime('%m/%d/%Y')
curr_time = now.strftime('%H:%M:%S')

# Get user that is logged in
curr_user = os.getlogin()

# event_id =
with open(log_file,'r') as f:
    f.readlines()
    for line in lines:
        print(line)

log_file_launch_writer = [event_id,
                            curr_date,
                            curr_time,
                            curr_user,
                            'Application launched',
                            'The application was launched by ' + curr_user + ' at ' + curr_time + ' on ' + curr_date + '\n'
                            ]

eventID = event_id + 1


print(log_file_launch_writer)
# log_file_launch_input = log_file_launch_input.append(curr_date, curr_time,'Application launched',"Testttttt description ohboy it's a big one")
# print(log_file_launch_input)

# write a log eventID and prevEventID


# # Table
# #EventId|Date|Time|User|Event|Description


# f.write('\t'.join(l[1:]) + '\n')


# # def log_entry_launched(logfilepath):
# #     with open(logfilepath,'a') as f:
#     f.write()

#     return

# def log_entry_closed:

# def log_entry_other2:



# # log program name
# # version
# # user name
# # date/time
# # time closed

