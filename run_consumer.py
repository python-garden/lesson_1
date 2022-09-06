from pprint import pprint

from app.settings import event_broker_settings, service_database_settings


if __name__ == "__main__":
    pprint(event_broker_settings.dict(), indent=4)
    pprint(service_database_settings.dict(), indent=4)
