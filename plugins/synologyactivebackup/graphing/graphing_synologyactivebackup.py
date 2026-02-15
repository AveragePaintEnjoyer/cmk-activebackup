from cmk.graphing.v1 import Title
from cmk.graphing.v1.graphs import Graph, MinimalRange
from cmk.graphing.v1.metrics import Color, DecimalNotation, Metric, Unit, TimeNotation, SINotation
from cmk.graphing.v1.perfometers import Closed, FocusRange, Open, Perfometer

metric_synologyactivebackup_status = Metric(
    name = "ab4b_result",
    title = Title("Backup Status"),
    unit = Unit(DecimalNotation("")),
    color = Color.YELLOW,
)

metric_synologyactivebackup_transfered = Metric(
    name = "ab4b_transfered",
    title = Title("Transfered Data"),
    unit = Unit(SINotation("bytes")),
    color = Color.LIGHT_BLUE,
)

metric_synologyactivebackup_time = Metric(
    name = "ab4b_duration_in_s",
    title = Title("Backup Duration"),
    unit = Unit(TimeNotation()),
    color = Color.LIGHT_BLUE,
)

metric_synologyactivebackup_last = Metric(
    name = "ab4b_last_run",
    title = Title("Time since last Backup"),
    unit = Unit(TimeNotation()),
    color = Color.LIGHT_BLUE,
)