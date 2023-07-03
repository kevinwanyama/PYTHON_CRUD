import pypyodbc
import config


# returns the sql connection
def getConnection():
    connection = pypyodbc.connect(
        "Driver= {" + config.DATABASE_CONFIG["Driver"] + "} ;server=" + config.DATABASE_CONFIG[
            "Server"] + ";Database=" +
        config.DATABASE_CONFIG["Database"] + ";uid=" + config.DATABASE_CONFIG["UID"] + ";pwd=" + config.DATABASE_CONFIG[
            "Password"])
    return connection
