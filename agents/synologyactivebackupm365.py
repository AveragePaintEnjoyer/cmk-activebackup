#!/usr/bin/python3

import sqlite3
import json
import time

# prep

print("<<<synologyactivebackupm365:sep(0)>>>")

current_time = int(time.time())

con_config = sqlite3.connect("/volume1/@ActiveBackup-Office365/db/config.sqlite")
cur_config = con_config.cursor()

con_log = sqlite3.connect("/volume1/@ActiveBackup-Office365/db/log.sqlite")
cur_log = con_log.cursor()

data_list = []

# retrieve a tuple of all configured tasks
select_tasks = cur_config.execute("SELECT task_id FROM task_info_table")
tasks = select_tasks.fetchall()

for task in [task[0] for task in tasks]:
    # claim real task name
    task_name_raw = cur_config.execute("SELECT task_name FROM task_info_table WHERE task_id = ?", (task,)).fetchone()
    task_name = task_name_raw[0] if task_name_raw else None

    # get task data
    data_general = cur_log.execute("select execution_status,transfered_size,start_run_time,end_run_time from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_drive = cur_log.execute("select drive_success_count,drive_warning_count,drive_error_count,drive_transfered_size from job_log_table where task_id = ? ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_mail = cur_log.execute("select mail_success_count,mail_warning_count,mail_error_count,mail_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_archive = cur_log.execute("select archive_mail_success_count,archive_mail_warning_count,archive_mail_error_count,archive_mail_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_contact = cur_log.execute("select contact_success_count,contact_warning_count,contact_error_count,contact_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_calender = cur_log.execute("select calendar_success_count,calendar_warning_count,calendar_error_count,calendar_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_group = cur_log.execute("select group_calendar_success_count,group_calendar_warning_count,group_calendar_error_count,group_calendar_transfered_size,group_mail_success_count,group_mail_warning_count,group_mail_error_count,group_mail_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_site = cur_log.execute("select site_success_count,site_warning_count,site_error_count,site_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
    data_teams = cur_log.execute("select teams_success_count,teams_warning_count,teams_error_count,teams_transfered_size from job_log_table where task_id = ? AND job_type = 0 ORDER BY job_execution_id DESC LIMIT 1", (task,)).fetchone()
   
    # check if value for time exists, then calculate duration and last-runtime
    if data_general[2] and data_general[3]:
        job_duration = data_general[3] - data_general[2]
        job_last_runtime = current_time - data_general[2]
    # assign values to variables
    data_dict = {
        # general data
        'task_name': task_name,
        'job_execution_status': data_general[0],
        'job_transfered_size': data_general[1],
        'job_start_run_time': data_general[2],
        'job_end_run_time': data_general[3],
        'job_duration': job_duration,
        'job_last_runtime': job_last_runtime,
        # onedrive data
        'drive_success_count': data_drive[0],
        'drive_warning_count': data_drive[1],
        'drive_error_count': data_drive[2],
        'drive_transfered_size': data_drive[3],
        # exchange data
        'mail_success_count': data_mail[0],
        'mail_warning_count': data_mail[1],
        'mail_error_count': data_mail[2],
        'mail_transfered_size': data_mail[3],
        # archive data
        'archive_mail_success_count': data_archive[0],
        'archive_mail_warning_count': data_archive[1],
        'archive_mail_error_count': data_archive[2],
        'archive_mail_transfered_size': data_archive[3],
        # contact data
        'contact_success_count': data_contact[0],
        'contact_warning_count': data_contact[1],
        'contact_error_count': data_contact[2],
        'contact_transfered_size': data_contact[3],
        # calender data
        'calendar_success_count': data_calender[0],
        'calendar_warning_count': data_calender[1],
        'calendar_error_count': data_calender[2],
        'calendar_transfered_size': data_calender[3],
        # group data
        'group_calendar_success_count': data_group[0],
        'group_calendar_warning_count': data_group[1],
        'group_calendar_error_count': data_group[2],
        'group_calendar_transfered_size': data_group[3],
        'group_mail_success_count': data_group[4],
        'group_mail_warning_count': data_group[5],
        'group_mail_error_count': data_group[6],
        'group_mail_transfered_size': data_group[7],
        # site data
        'site_success_count': data_site[0],
        'site_warning_count': data_site[1],
        'site_error_count': data_site[2],
        'site_transfered_size': data_site[3],
        # teams data
        'teams_success_count': data_teams[0],
        'teams_warning_count': data_teams[1],
        'teams_error_count': data_teams[2],
        'teams_transfered_size': data_teams[3],
    }
    data_list.append(data_dict)
print(json.dumps(data_list))