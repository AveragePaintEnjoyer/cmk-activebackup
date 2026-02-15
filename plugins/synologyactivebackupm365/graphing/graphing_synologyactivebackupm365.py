from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph, MinimalRange
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit, TimeNotation, SINotation, StrictPrecision
from cmk.graphing.v1.perfometers import Closed, FocusRange, Open, Perfometer

# general

metric_synologyactivebackupm365_transfered = Metric(
    name = "ab4bm365_transfered",
    title = Title("Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.LIGHT_BLUE,
)

metric_synologyactivebackupm365_time = Metric(
    name = "ab4bm365_duration_in_s",
    title = Title("Backup Duration"),
    unit = Unit(TimeNotation()),
    color = Color.LIGHT_BLUE,
)

metric_synologyactivebackupm365_last = Metric(
    name = "ab4bm365_last_run",
    title = Title("Time since last Backup"),
    unit = Unit(TimeNotation()),
    color = Color.LIGHT_BLUE,
)

# transfered data

metric_trans_drive = Metric(
    name = "drive_transfered_size",
    title = Title("Drive - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_mail = Metric(
    name = "mail_transfered_size",
    title = Title("Mail - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_archive = Metric(
    name = "archive_transfered_size",
    title = Title("Archive - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_contact = Metric(
    name = "contact_transfered_size",
    title = Title("Contact - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_calendar = Metric(
    name = "calendar_transfered_size",
    title = Title("Calender - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_group_calender = Metric(
    name = "group_calendar_transfered_size",
    title = Title("Group calender - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_group_mail = Metric(
    name = "group_mail_transfered_size",
    title = Title("Group mail - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_site = Metric(
    name = "site_transfered_size",
    title = Title("Sharepoint site - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

metric_trans_teams = Metric(
    name = "teams_transfered_size",
    title = Title("Teams - Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.YELLOW,
)

# success count

metric_success_drive = Metric(
    name = "drive_success_count",
    title = Title("Drive - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_mail = Metric(
    name = "mail_success_count",
    title = Title("Mail - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_archive = Metric(
    name = "archive_success_count",
    title = Title("Archive - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_contact = Metric(
    name = "contact_success_count",
    title = Title("Contact - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_calendar = Metric(
    name = "calendar_success_count",
    title = Title("Calender - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_group_calender = Metric(
    name = "group_calendar_success_count",
    title = Title("Group calender - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_group_mail = Metric(
    name = "group_mail_success_count",
    title = Title("Group mail - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_site = Metric(
    name = "site_success_count",
    title = Title("Sharepoint site - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

metric_success_teams = Metric(
    name = "teams_success_count",
    title = Title("Teams - Success Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.GREEN,
)

# warning count

metric_warning_drive = Metric(
    name = "drive_warning_count",
    title = Title("Drive - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_mail = Metric(
    name = "mail_warning_count",
    title = Title("Mail - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_archive = Metric(
    name = "archive_warning_count",
    title = Title("Archive - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_contact = Metric(
    name = "contact_warning_count",
    title = Title("Contact - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_calendar = Metric(
    name = "calendar_warning_count",
    title = Title("Calender - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_group_calender = Metric(
    name = "group_calendar_warning_count",
    title = Title("Group calender - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_group_mail = Metric(
    name = "group_mail_warning_count",
    title = Title("Group mail - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_site = Metric(
    name = "site_warning_count",
    title = Title("Sharepoint site - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

metric_warning_teams = Metric(
    name = "teams_warning_count",
    title = Title("Teams - Warning Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.ORANGE,
)

# error count

metric_error_drive = Metric(
    name = "drive_error_count",
    title = Title("Drive - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_mail = Metric(
    name = "mail_error_count",
    title = Title("Mail - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_archive = Metric(
    name = "archive_error_count",
    title = Title("Archive - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_contact = Metric(
    name = "contact_error_count",
    title = Title("Contact - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_calendar = Metric(
    name = "calendar_error_count",
    title = Title("Calender - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_group_calender = Metric(
    name = "group_calendar_error_count",
    title = Title("Group calender - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_group_mail = Metric(
    name = "group_mail_error_count",
    title = Title("Group mail - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_site = Metric(
    name = "site_error_count",
    title = Title("Sharepoint site - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

metric_error_teams = Metric(
    name = "teams_error_count",
    title = Title("Teams - Error Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.RED,
)

# aggr count

metric_aggr_drive = Metric(
    name = "aggr_drive",
    title = Title("Drive - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_mail = Metric(
    name = "aggr_mail",
    title = Title("Mail - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_archive = Metric(
    name = "aggr_archive",
    title = Title("Archive - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_contact = Metric(
    name = "aggr_contact",
    title = Title("Contact - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_calendar = Metric(
    name = "aggr_calendar",
    title = Title("Calender - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_group_calender = Metric(
    name = "aggr_group_calendar",
    title = Title("Group calender - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_group_mail = Metric(
    name = "aggr_group_mail",
    title = Title("Group mail - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_site = Metric(
    name = "aggr_site",
    title = Title("Sharepoint site - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

metric_aggr_teams = Metric(
    name = "aggr_teams",
    title = Title("Teams - Count"),
    unit = Unit(DecimalNotation(""), StrictPrecision(0)),
    color = Color.WHITE,
)

# combined

graph_trans_combined = Graph(
    name = "transfered_size_combined",
    title = Title("Transfered Data for each app"),
    simple_lines=[ "drive_transfered_size", "mail_transfered_size", "archive_transfered_size", "contact_transfered_size", "calendar_transfered_size", "group_calendar_transfered_size", "group_mail_transfered_size", "site_transfered_size", "teams_transfered_size" ]
)

graph_drive_combined = Graph(
    name = "count_drive_combined",
    title = Title("Count - OneDrive"),
    simple_lines=["drive_success_count", "drive_warning_count", "drive_error_count", "aggr_drive"]
)

graph_mail_combined = Graph(
    name = "count_mail_combined",
    title = Title("Count - Exchange"),
    simple_lines=["mail_success_count", "mail_warning_count", "mail_error_count", "aggr_mail"]
)

graph_archive_combined = Graph(
    name = "count_archive_combined",
    title = Title("Count - Archive"),
    simple_lines=["archive_success_count", "archive_warning_count", "archive_error_count", "aggr_archive"]
)

graph_contact_combined = Graph(
    name = "count_contact_combined",
    title = Title("Count - Contact"),
    simple_lines=["contact_success_count", "contact_warning_count", "contact_error_count", "aggr_contact"]
)

graph_calendar_combined = Graph(
    name = "count_calendar_combined",
    title = Title("Count - Calendar"),
    simple_lines=["calendar_success_count", "calendar_warning_count", "calendar_error_count", "aggr_calendar"]
)

graph_site_combined = Graph(
    name = "count_site_combined",
    title = Title("Count - Sharepoint Sites"),
    simple_lines=["site_success_count", "site_warning_count", "site_error_count", "aggr_site"]
)

graph_teams_combined = Graph(
    name = "count_teams_combined",
    title = Title("Count - Teams"),
    simple_lines=["teams_success_count", "teams_warning_count", "teams_error_count", "aggr_teams"]
)

graph_group_calendar_combined = Graph(
    name = "count_group_calendar_combined",
    title = Title("Count - Group Calendar"),
    simple_lines=["group_calendar_success_count", "group_calendar_warning_count", "group_calendar_error_count", "aggr_group_calendar"]
)

graph_group_mail_combined = Graph(
    name = "count_group_mail_combined",
    title = Title("Count - Group Mail"),
    simple_lines=["group_mail_success_count", "group_mail_warning_count", "group_mail_error_count", "aggr_group_mail"]
)

#graph_count_combined = Graph(
#    name = "count_combined",
#    title = Title("Counted elements for each app"),
#    simple_lines=["drive_success_count", "drive_warning_count", "drive_error_count", "mail_success_count", "mail_warning_count", "mail_error_count", "archive_success_count", "archive_warning_count", "archive_error_count", "contact_success_count", "contact_warning_count", "contact_error_count", "calendar_success_count", "calendar_warning_count", "calendar_error_count", "group_calendar_success_count", "group_calendar_warning_count", "group_calendar_error_count", "group_mail_success_count", "group_mail_warning_count", "group_mail_error_count", "site_success_count", "site_warning_count", "site_error_count", "teams_success_count", "teams_warning_count", "teams_error_count", "aggr_drive", "aggr_mail", "aggr_archive", "aggr_contact", "aggr_calendar", "aggr_group_calendar", "aggr_group_mail", "aggr_site", "aggr_teams"]
#)