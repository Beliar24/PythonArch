from mobile.utils.read_property import get_property


def caps():
    return dict(
        platformName=get_property("platform.name"),
        deviceName=get_property("device.name"),
        platformVersion=get_property("platform.version"),
        automationName=get_property("automation.name"),
        appPackage=get_property("app.package"),
        appActivity=get_property("app.activity"),
        app=get_property("app"))
