#!/usr/bin/python3

# version 1.1

import sqlite3
import json
import time

# prep

print("<<<synologyactivebackup:sep(0)>>>")

current_time = int(time.time())

con_config = sqlite3.connect("/volume1/@ActiveBackup/config.db")
cur_config = con_config.cursor()

con_activity = sqlite3.connect("/volume1/@ActiveBackup/activity.db")
cur_activity = con_activity.cursor()

data_list = []

# retrieve a tuple of all configured tasks
select_tasks = cur_config.execute("SELECT task_id FROM task_table")
tasks = select_tasks.fetchall()

for task in [task[0] for task in tasks]:
    # claim real task name
    task_name_raw = cur_config.execute("SELECT task_name FROM task_table WHERE task_id = ?", (task,)).fetchone()
    task_name = task_name_raw[0] if task_name_raw else None
    # get schedule
    task_schedule_raw = cur_config.execute("SELECT sched_content FROM task_table WHERE task_id = ?", (task,)).fetchone()
    task_schedule_json = task_schedule_raw[0] if task_schedule_raw else None
    task_schedule = json.loads(task_schedule_json)
    # claim all associated devices from that task
    devices = cur_config.execute("SELECT device_id FROM backup_task_device WHERE task_id = ?", (task,)).fetchall()
    # query for each device in associated task
    for device in [device[0] for device in devices]:
        # retrieve exact hostname, since we will need this later for the results
        device_name_raw = cur_config.execute("select host_name from device_table where device_id = ?", (device,)).fetchone()
        # clean up actual device name, to be able to use it later
        device_name = device_name_raw[0] if device_name_raw else None
        # get result from result table
        result_id_raw = cur_activity.execute("select result_id from result_table where task_id = ? AND task_config like ? AND job_action = 1 ORDER BY result_id DESC LIMIT 1", (task, f"%{device_name}%")).fetchone()
        # clean up actual result id, to be able to use it later
        result_id = result_id_raw[0] if result_id_raw else None
        # get task data: status, transferred bytes, start time, end time
        data = cur_activity.execute("select status,transfered_bytes,time_start,time_end from device_result_table where result_id like ? AND device_name like ?", (f"%{result_id}%", f"%{device_name}%")).fetchone()
        
        # check if data is none, if so skip iteration
        if data is None:
            continue
        
        # check if value for time exists, then calculate duration and last-runtime
        if data[2] and data[3]:
            job_duration = data[3] - data[2]
            job_last_runtime = current_time - data[2]
        # assign values to variables
        data_dict = {
            'task_name': task_name,
            'device_name': device_name,
            'result_id': result_id,
            'job_status': data[0],
            'job_transferred': data[1],
            'job_time_start': data[2],
            'job_time_end': data[3],
            'job_duration_in_s': job_duration,
            'job_last_runtime': job_last_runtime,
            'repeat_hour': task_schedule["repeat_hour"],
            'repeat_type': task_schedule["repeat_type"],
            'run_hour': task_schedule["run_hour"],
            'run_min': task_schedule["run_min"],
            'run_weekday': task_schedule["run_weekday"],
        }
        data_list.append(data_dict)
print(json.dumps(data_list))