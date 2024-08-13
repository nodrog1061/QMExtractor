# QMExtractor


if you get this error:
`OSError: [WinError 193] %1 is not a valid Win32 application`

you need to move the dll files in the `DLL's` directory to `system32` folder as director comes with incorrect dll files

## Install

Run `pip install -r requirements.txt`

## Running the project

ensure OpenQM / Director server is running

now run `python -m uvicorn main:app --reload --port 8000` or `uvicorn main:app --host 0.0.0.0 --port $PORT` for accross network

navigate to `http://LocalHost:8000/docs`

## Known Files that can be called

`LOG`, `CALLS`, `UNITS`, `CONTROL`, `MAPS`
