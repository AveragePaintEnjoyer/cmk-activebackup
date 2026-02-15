#!/usr/bin/env python3

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric
import json

all_job_status = {
    "0": (State.UNKNOWN, "Unbekannt"),
    "1": (State.OK, "Erfolgreich"),
    "2": (State.UNKNOWN, "Unbekannt"),
    "3": (State.UNKNOWN, "Unbekannt"),
    "4": (State.UNKNOWN, "Unbekannt"),
    "5": (State.UNKNOWN, "Unbekannt"),
    "6": (State.OK, "Abgeschlossen mit übersprungenen Elementen"),
    "7": (State.CRIT, "Abgebrochen"),
    "8": (State.UNKNOWN, "Unbekannt"),
    "9": (State.UNKNOWN, "Unbekannt"),
    "10": (State.UNKNOWN, "Unbekannt"),
}

# parse agent output and make data more usable
def parse_synologyactivebackupm365(string_table):
    # load json data from string_table
    # check if data is not empty
    if len(string_table) > 0:
        line = str(" ".join(string_table[0]))
        try:
            json_output = json.loads(line)
        except Exception as read_json_error:
            json_output = {"timestamp": "EXEC-ERROR - please check output of plugin on host - Additional info: %s" % str(read_json_error)}
    else:
        json_output = {"timestamp": "EXEC-ERROR - please check output of plugin on host"}
    # initiate variable parsed
    parsed = {}
    # iterate through list of dictionaries
    for json_array in json_output:
        parsed["Task: " + json_array["task_name"]] = json_array
    # return variable parsed
    return parsed

# finds and creates actual services based of the agent output
def discover_synologyactivebackupm365(section):
    for group in section:
        yield Service(item=group)

# actual check which determines possible state of the service based of the agent output
def check_synologyactivebackupm365(item, section):
    # read dictionary of specific item
    content = section.get(item)

    # map variables: general
    ab4bm365_status = str(content["job_execution_status"])
    ab4bm365_transfered = int(content["job_transfered_size"])
    ab4bm365_duration_in_s = int(content["job_duration"])
    ab4bm365_last_run = int(content["job_last_runtime"])
    # map variables: drive
    drive_success_count=int(content["drive_success_count"])
    drive_warning_count=int(content["drive_warning_count"])
    drive_error_count=int(content["drive_error_count"])
    drive_transfered_size=int(content["drive_transfered_size"])
    # map variables: mail
    mail_success_count=int(content["mail_success_count"])
    mail_warning_count=int(content["mail_warning_count"])
    mail_error_count=int(content["mail_error_count"])
    mail_transfered_size=int(content["mail_transfered_size"])
    # map variables: archive
    archive_success_count=int(content["archive_mail_success_count"])
    archive_warning_count=int(content["archive_mail_warning_count"])
    archive_error_count=int(content["archive_mail_error_count"])
    archive_transfered_size=int(content["archive_mail_transfered_size"])
    # map variables: contact
    contact_success_count=int(content["contact_success_count"])
    contact_warning_count=int(content["contact_warning_count"])
    contact_error_count=int(content["contact_error_count"])
    contact_transfered_size=int(content["contact_transfered_size"])
    # map variables: calendar
    calendar_success_count=int(content["calendar_success_count"])
    calendar_warning_count=int(content["calendar_warning_count"])
    calendar_error_count=int(content["calendar_error_count"])
    calendar_transfered_size=int(content["calendar_transfered_size"])
    # map variables: group
    group_calendar_success_count=int(content["group_calendar_success_count"])
    group_calendar_warning_count=int(content["group_calendar_warning_count"])
    group_calendar_error_count=int(content["group_calendar_error_count"])
    group_calendar_transfered_size=int(content["group_calendar_transfered_size"])
    group_mail_success_count=int(content["group_mail_success_count"])
    group_mail_warning_count=int(content["group_mail_warning_count"])
    group_mail_error_count=int(content["group_mail_error_count"])
    group_mail_transfered_size=int(content["group_mail_transfered_size"])
    # map variables: sharepoint
    site_success_count=int(content["site_success_count"])
    site_warning_count=int(content["site_warning_count"])
    site_error_count=int(content["site_error_count"])
    site_transfered_size=int(content["site_transfered_size"])
    # map variables: teams
    teams_success_count=int(content["teams_success_count"])
    teams_warning_count=int(content["teams_warning_count"])
    teams_error_count=int(content["teams_error_count"])
    teams_transfered_size=int(content["teams_transfered_size"])

    # compare active backup status with lookup table
    if ab4bm365_status in all_job_status:
        mk_status, mk_summ = all_job_status[ab4bm365_status]
    else:
        mk_status = State.UNKNOWN
        mk_summ = "Plugin Fehler!"
    
    # return status and service summary
    yield Result(state=mk_status, summary=f"Status: {mk_summ}")

    # return metric: general
    yield Metric(name="ab4bm365_transfered", value=ab4bm365_transfered)
    yield Metric(name="ab4bm365_duration_in_s", value=ab4bm365_duration_in_s)
    yield Metric(name="ab4bm365_last_run", value=ab4bm365_last_run)
    # return metric: drive
    yield Metric(name="drive_success_count", value=drive_success_count)
    yield Metric(name="drive_warning_count", value=drive_warning_count)
    yield Metric(name="drive_error_count", value=drive_error_count)
    yield Metric(name="drive_transfered_size", value=drive_transfered_size)
    # return metric: mail
    yield Metric(name="mail_success_count", value=mail_success_count)
    yield Metric(name="mail_warning_count", value=mail_warning_count)
    yield Metric(name="mail_error_count", value=mail_error_count)
    yield Metric(name="mail_transfered_size", value=mail_transfered_size)
    # return metric: archive
    yield Metric(name="archive_success_count", value=archive_success_count)
    yield Metric(name="archive_warning_count", value=archive_warning_count)
    yield Metric(name="archive_error_count", value=archive_error_count)
    yield Metric(name="archive_transfered_size", value=archive_transfered_size)
    # return metric: contact
    yield Metric(name="contact_success_count", value=contact_success_count)
    yield Metric(name="contact_warning_count", value=contact_warning_count)
    yield Metric(name="contact_error_count", value=contact_error_count)
    yield Metric(name="contact_transfered_size", value=contact_transfered_size)
    # return metric: calendar
    yield Metric(name="calendar_success_count", value=calendar_success_count)
    yield Metric(name="calendar_warning_count", value=calendar_warning_count)
    yield Metric(name="calendar_error_count", value=calendar_error_count)
    yield Metric(name="calendar_transfered_size", value=calendar_transfered_size)
    # return metric: group
    yield Metric(name="group_calendar_success_count", value=group_calendar_success_count)
    yield Metric(name="group_calendar_warning_count", value=group_calendar_warning_count)
    yield Metric(name="group_calendar_error_count", value=group_calendar_error_count)
    yield Metric(name="group_calendar_transfered_size", value=group_calendar_transfered_size)

    yield Metric(name="group_mail_success_count", value=group_mail_success_count)
    yield Metric(name="group_mail_warning_count", value=group_mail_warning_count)
    yield Metric(name="group_mail_error_count", value=group_mail_error_count)
    yield Metric(name="group_mail_transfered_size", value=group_mail_transfered_size)
    # return metric: sharepoint
    yield Metric(name="site_success_count", value=site_success_count)
    yield Metric(name="site_warning_count", value=site_warning_count)
    yield Metric(name="site_error_count", value=site_error_count)
    yield Metric(name="site_transfered_size", value=site_transfered_size)
    # return metric: teams
    yield Metric(name="teams_success_count", value=teams_success_count)
    yield Metric(name="teams_warning_count", value=teams_warning_count)
    yield Metric(name="teams_error_count", value=teams_error_count)
    yield Metric(name="teams_transfered_size", value=teams_transfered_size)
    # return metric: aggregated
    yield Metric(name="aggr_drive", value=drive_success_count+drive_warning_count+drive_error_count)
    yield Metric(name="aggr_mail", value=mail_success_count+mail_warning_count+mail_error_count)
    yield Metric(name="aggr_archive", value=archive_success_count+archive_warning_count+archive_error_count)
    yield Metric(name="aggr_contact", value=contact_success_count+contact_warning_count+contact_error_count)
    yield Metric(name="aggr_calendar", value=calendar_success_count+calendar_warning_count+calendar_error_count)
    yield Metric(name="aggr_group_calendar", value=group_calendar_success_count+group_calendar_warning_count+group_calendar_error_count)
    yield Metric(name="aggr_group_mail", value=group_mail_success_count+group_mail_warning_count+group_mail_error_count)
    yield Metric(name="aggr_site", value=site_success_count+site_warning_count+site_error_count)
    yield Metric(name="aggr_teams", value=teams_success_count+teams_warning_count+teams_error_count)

# define section in agent. this is necessary to able to find and parse the agent output
agent_section_synologyactivebackupm365 = AgentSection(
    name = "synologyactivebackupm365",
    parse_function = parse_synologyactivebackupm365,
)

# define the plugin itself
check_plugin_synologyactivebackupm365 = CheckPlugin(
    # plugin name
    name = "synologyactivebackupm365",
    sections = ["synologyactivebackupm365"],
    # generated service name (how it will be displayed in wato)
    service_name = "ActiveBackupM365 %s",
    # function which will detect services of this kind of plugin
    discovery_function = discover_synologyactivebackupm365,
    # actual check function, which determines possible state and data
    check_function = check_synologyactivebackupm365,
)