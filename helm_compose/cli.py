import fire
from helm_handler import HelmHandler
from config import load_config
from health_checker import HealthChecker
from tui import display_output


class CLI:
    def __init__(self):
        self.handler = HelmHandler()
        self.health_checker = HealthChecker()

    def deploy(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            status = self.handler.install_chart(service_config)
            display_output({service_name: status})

    def upgrade(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            status = self.handler.upgrade_chart(service_config)
            display_output({service_name: status})

    def rollback(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            status = self.handler.rollback_chart(service_config)
            display_output({service_name: status})

    def delete(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            status = self.handler.delete_chart(service_config)
            display_output({service_name: status})

    def status(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            status = self.handler.get_chart_status(service_config)
            display_output({service_name: status})

    def health(self, config_path: str):
        config = load_config(config_path)
        for service_name, service_config in config.get('services', {}).items():
            health = self.health_checker.check_service_health(service_name)
            display_output({service_name: health})


def main():
    fire.Fire(CLI)


if __name__ == '__main__':
    main()
