import json
from configparser import ConfigParser

# Config Object: {configFile: "mem.conf", "section": "inputs.cpu", settings}


def setupConfig(data):
    jsonDump = json.dumps(data)
    dataJson = json.loads(jsonDump)

    configFile = dataJson["configFile"]
    section = dataJson["section"]
    updates = dataJson["updates"]
    baseContents = __salt__["cp.get_file_str"](
        "salt://monitoring/" + configFile)

    config = ConfigParser()
    config.read_string(baseContents)

    updatesJson = json.loads(updates)

    # Example data would be [inputs.cpu '[inputs.cpu' '[{"name": "percpu", "value": "true"}]'
    for update in updatesJson:
        config.set(section, update['name'], update['value'])

    with open("C:/Program Files/telegraf/telegraf.d/" + configFile, "w+") as configFile:
        configFile.read()
        config.write(configFile)

    return config


def getConfig(configFile):
    contents = None
    with open("C:/Program Files/telegraf/telegraf.d/" + configFile) as configFile:
        contents = configFile.read()

    config = ConfigParser()
    config.read_string(contents)

    return config
