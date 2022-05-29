import datetime
import pytz
import pandas as pd

log_file = r'C:\Users\Fogzy\Documents\GitHub\code_chaos\Write Log File\loggy.csv'

# Get current date/timestamp
now = datetime.datetime.now(pytz.timezone('US/Central'))

# Assign date and time to variables (to be written later)
curr_date = now.strftime('%m/%d/%Y')
curr_time = now.strftime('%H:%M:%S')

# Get user that is logged in (to be written later)
curr_user = os.getlogin()

# Get eventID. Read the csv log file to a dataframe, extract the eventID column and get the max. Add 1 to that to get the new eventID.
df_logfile = pd.read_csv(log_file,index_col=False)
df_eventid = df_logfile['event_id']
max_eventid = df_eventid.max()
curr_eventid = max_eventid + 1

# Put new log events into list - these variables aren't updating....
write_log_launch = [curr_eventid,
                            curr_date,
                            curr_time,
                            curr_user,
                            'Application launched',
                            'The application was launched by ' + curr_user + ' at ' + curr_time + ' on ' + curr_date'
                            ]
# print(write_log_launch)
column_names = ['event_id','date','time','user','event','description']

# Write the new log entry to new df
df_new_log = pd.DataFrame(write_log_launch,index_col=False).T
df_new_log.columns = column_names

print(df_logfile)
print(df_new_log)

# #Concat the new and the old dfs
concat_list = [df_logfile,df_new_log]
df_output = pd.concat(concat_list, ignore_index=False)

# Re-write log file
df_output.to_csv(log_file,index=False)

# Print final df.
print(df_output)

