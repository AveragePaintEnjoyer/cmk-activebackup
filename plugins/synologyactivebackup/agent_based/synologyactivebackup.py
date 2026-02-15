#!/usr/bin/env python3

from cmk.agent_based.v2 import AgentSection, CheckPlugin, Service, Result, State, Metric
import json

all_job_status = {
    "0": (State.UNKNOWN, "Unbekannt"),
    "1": (State.WARN, "Unvollständig"),
    "2": (State.OK, "Erfolgreich"),
    "3": (State.WARN, "Teilweise abgeschlossen"),
    "4": (State.CRIT, "Fehlgeschlagen"),
    "5": (State.CRIT, "Abgebrochen")
}


# parse agent output and make data more usable
def parse_synologyactivebackup(string_table):
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
        parsed["Task: " + json_array["task_name"] + " - Device: " + json_array["device_name"]] = json_array
    # return variable parsed
    return parsed


# finds and creates actual services based of the agent output
def discover_synologyactivebackup(section):
    for group in section:
        yield Service(item=group)


# actual check which determines possible state of the service based of the agent output
def check_synologyactivebackup(item, section):
    # read dictionary of specific item
    content = section.get(item)

    # map variables
    ab4b_status = str(content["job_status"])
    ab4b_result = int(content["result_id"])
    ab4b_transfered = int(content["job_transferred"])
    ab4b_duration_in_s = int(content["job_duration_in_s"])
    ab4b_last_run = int(content["job_last_runtime"])

    # compare active backup status with lookup table
    if ab4b_status in all_job_status:
        mk_status, mk_summ = all_job_status[ab4b_status]
    else:
        mk_status = State.UNKNOWN
        mk_summ = "Plugin Fehler!"

    # return status and service summary
    yield Result(state=mk_status, summary=f"Status: {mk_summ}")

    # return metric: result, transfered size, duration in s, last runtime
    yield Metric(name="ab4b_result", value=ab4b_result)
    yield Metric(name="ab4b_transfered", value=ab4b_transfered)
    yield Metric(name="ab4b_duration_in_s", value=ab4b_duration_in_s)
    yield Metric(name="ab4b_last_run", value=ab4b_last_run)

# define section in agent. this is necessary to able to find and parse the agent output
agent_section_synologyactivebackup = AgentSection(
    name = "synologyactivebackup",
    parse_function = parse_synologyactivebackup,
)


# define the plugin itself
check_plugin_synologyactivebackup = CheckPlugin(
    # plugin name
    name = "synologyactivebackup",
    sections = ["synologyactivebackup"],
    # generated service name (how it will be displayed in wato)
    service_name = "ActiveBackup %s",
    # function which will detect services of this kind of plugin
    discovery_function = discover_synologyactivebackup,
    # actual check function, which determines possible state and data
    check_function = check_synologyactivebackup,
)