# gunicorn daemon controller

![image](images/image.gif)

## Disclaimer warning

- There is NO WARRANTY!
- Take no responsibility for any of this.

## Confirmed environment

- Ubuntu 20.04.2 LTS
- GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)
- Python 3.8.10 (venv)
- Python packages is shown below (FastAPI is optional)

```
fastapi==0.65.2
gunicorn==20.1.0
setproctitle==1.2.2
uvicorn==0.14.0
```

### Isntall packages using by pip

- This procedure is needed to confirm examples.
- If you don't need examples, you need the only gunidaemonctl file.

```
pip install -r requirements.txt
```

## Overview

- Control the gunicorn's daemons using by Bash.

## Structure of files

```
├── gunicorn_config            <-- gunicorn config files
│   ├── guni_conf_prod.py
│   └── guni_conf_staging.py
├── gunidaemonctl              <-- Bash script
├── main.py                    <-- Python Web app example1
└── main_fast_api.py           <-- Python Web app example2 (Use FastAPI)
```

## config


### gunidaemonctl config

- Set path for gunicorn config files.
- Absolute path is recommended.
- An example is shown below.

```
vim gunidaemonctl

GUNICORN_CONFIG_PATH="./gunicorn_config/"
```

### gunicorn config

- Create gunicorn config files in the directory you set on gunidaemonctl-bash.
- The filename must be same as proc_name.
- Treat the filename as [app_id].
- Set the unique id because it's used to identify app's process id.
- An example is shown below.

```bash
vim gunicorn_config/guni_conf_staging.py

proc_name = 'guni_conf_staging' # The proc name must be set to the same value as the filename of gunicorn config.
```

- Also python Web app path is set in the gunicorn config.
- Absolute path is recommended.
- An example is shown below.

```bash
vim gunicorn_config/guni_conf_staging.py

pythonpath = './'
```


## Operation

### Outline

```
./gunidaemonctl [operation] [app_id]
```

- [operation] : start | ps | pid | stop
- [app_id]  : proc_name (gunicorn config filename)


### Start the daemon

```
./gunidaemonctl start guni_conf_staging
```


### Stop the daemon

```
./gunidaemonctl stop guni_conf_staging
```

### Show the processes of gunicorn

```
./gunidaemonctl ps guni_conf_staging

ubuntu 1001 0.8 2.2 0 0 ? S 12:10 0:00 gunicorn: master [guni_conf_staging]
ubuntu 1002 2.4 3.3 0 0 ? S 12:10 0:00 gunicorn: worker [guni_conf_staging]
ubuntu 1003 2.4 3.3 0 0 ? S 12:10 0:00 gunicorn: worker [guni_conf_staging]
```

### Show the pid of the master of the workers

```
./gunidaemonctl pid guni_conf_staging

master pid:
1001
```
