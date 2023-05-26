import helmpy
import time


class HelmHandler:
    def __init__(self, kube_context: str):
        self.helm = helmpy.Helm(kube_context)

    def install_chart(self, service_config: dict) -> dict:
        """
        Install a Helm chart, returns status.
        """
        try:
            chart = service_config.get('chart')
            repo = service_config.get('repo')
            version = service_config.get('version')
            values = service_config.get('values')
            namespace = service_config.get('namespace')

            release_name = f"{namespace}-{chart}"

            self.helm.add_repo(repo)
            self.helm.update_repos()
            self.helm.install_chart(release_name, chart, version, values, namespace)

            # Poll for status
            return self.poll_for_status(service_config)
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def upgrade_chart(self, service_config: dict) -> dict:
        """
        Upgrade a Helm chart, returns status.
        """
        try:
            chart = service_config.get('chart')
            repo = service_config.get('repo')
            version = service_config.get('version')
            values = service_config.get('values')
            namespace = service_config.get('namespace')

            release_name = f"{namespace}-{chart}"

            self.helm.add_repo(repo)
            self.helm.update_repos()
            self.helm.upgrade_chart(release_name, chart, version, values, namespace)

            # Poll for status
            return self.poll_for_status(service_config)
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def rollback_chart(self, service_config: dict) -> dict:
        """
        Rollback a Helm chart, returns status.
        """
        try:
            chart = service_config.get('chart')
            namespace = service_config.get('namespace')

            release_name = f"{namespace}-{chart}"

            self.helm.rollback_chart(release_name)

            # Poll for status
            return self.poll_for_status(service_config)
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def delete_chart(self, service_config: dict) -> dict:
        """
        Delete a Helm chart, returns status.
        """
        try:
            chart = service_config.get('chart')
            namespace = service_config.get('namespace')

            release_name = f"{namespace}-{chart}"

            self.helm.delete_chart(release_name)

            # Poll for status
            return self.poll_for_status(service_config)
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}

    def get_chart_status(self, service_config: dict) -> dict:
        """
        Get status of a Helm chart.
        """
        try:
            chart = service_config.get('chart')
            namespace = service_config.get('namespace')

            release_name = f"{namespace}-{chart}"

            return self.helm.get_status(release_name)
        except Exception as e:
            return {'status': 'failure', 'message': str(e)}
    
    def poll_for_status(self, service_config: dict) -> dict:
        """
        Poll for the status of the chart. 
        """
        max_retries = 10
        retries = 0
        while retries < max_retries:
            status = self.get_chart_status(service_config)
            if status.get('status') in ['deployed', 'uninstalled']:
                return status
            elif status.get('status') == 'failed':
                return {'status': 'failure', 'message': 'Helm operation failed'}
            else:
                time.sleep(10)
                retries += 1

        return {'status': 'failure', 'message': 'Max retries exceeded'}
