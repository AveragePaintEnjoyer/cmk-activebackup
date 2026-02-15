# cmk-activebackup

## Files

```sh
/omd/sites/devel/local/share/check_mk/enabled_packages/synologyactivebackup-1.0.1.mkp
/omd/sites/devel/local/share/check_mk/enabled_packages/synologyactivebackupm365-1.0.0.mkp
```

## Active Backup for Business

Example output of agent:

```json
[
  {
    "task_name": "VM-WIN-t22Uhr",
    "device_name": "SHAPP",
    "result_id": 6639,
    "job_status": 2,
    "job_transferred": 2801762304,
    "job_time_start": 1728158405,
    "job_time_end": 1728158719,
    "job_duration_in_s": 314,
    "job_last_runtime": 152891,
    "repeat_hour": 0,
    "repeat_type": "Weekly",
    "run_hour": 22,
    "run_min": 0,
    "run_weekday": [
      0,
      1,
      2,
      3,
      4,
      5,
      6
    ]
  },
]
```

## Active Backup for Business M365

### Auslesen

Schema ist in zwei Datenbanken aufgeteilt.

- `config.sqlite` beinhaltet konfigurierte Aufgaben
- `log.sqlite` beinhaltet den Status und die Statistiken für jede Ausführung einer Aufgabe

```sh

# die letzte Ausführung von Aufgabe mit task_id = 1
sqlite3 \@ActiveBackup-Office365/db/log.sqlite "select * from job_log_table where task_id = 1 ORDER BY job_execution_id DESC LIMIT 1"
```

Beispielwerte

```sh
448|1735913408|1|||448|0|7||||7235818|6|19|0|0|3|22|0|7004090|2|20|0|0|2|19|0|0|2|19|0|0|7|7|2|0|7|7|2|0|23|37|0|129190|1735913323|1735913408|1|-1|8|3|0|102538|4294967295|-1|

723|1735853434|1|||723|0|1|4294967295||||0|132|0|0|0|132|0|0|0|132|0|0|0|132|0|0|0|132|0|0|0|0|0|0|0|0|0|0|0|2|0|0|0|0|0|0|0|1735853402|1735853434|1|-87|-1|

450|1735914218|1|||450|0|1||||79517|25|0|0|1631|25|0|0|76574|25|0|0|0|25|0|0|0|25|0|0|0|12|0|0|0|12|0|0|0|60|0|0|0|1735914048|1735914218|1|0|11|0|0|1312|4294967295|-1|
```

### Status

Die Tabelle `job_log_table` in `log.sqlite` scheint alle Einträge zubeinhalten bzgl. Ausführung der Aufgabe.
Die Spalte `execution_status` repräsentiert womöglich den Status der Ausführung selbst.

Die Werte könnte folgende Bedeutung haben

- 1 = erfolgreich abgeschlossen
- 6 = abgeschlossen mit übersprungenen Elementen
- 7 = abgebrochen

## Development

Navigate to correct directory on development cmk server

```sh
su devel
cd ~/local/lib/python3/cmk_addons/plugins/synologyactivebackup/agent_based
vim synologyactivebackup.py
```

Troubleshooting and debugging

```sh
# detect plugin itself: test parsed variable
cmk --detect-plugins=synologyactivebackup -v 10.188.188.23

# run discovery: detect services
cmk -vI --detect-plugins=synologyactivebackup 10.188.188.23
```