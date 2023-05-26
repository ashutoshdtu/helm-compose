from kubernetes import client, config
from pydantic import BaseModel, ValidationError


class ServiceHealth(BaseModel):
    status: str
    message: str


class HealthChecker:
    def __init__(self, kube_context: str = None):
        config.load_kube_config(context=kube_context)
        self.api = client.CoreV1Api()

    def check_service_health(self, service_name: str, namespace: str) -> ServiceHealth:
        try:
            service = self.api.read_namespaced_service(
                name=service_name,
                namespace=namespace
            )
            
            status = service.status
            message = service.metadata.annotations.get('message', 'Service is running normally')
            
            return ServiceHealth(status=status, message=message)
        except client.ApiException as e:
            print(f"Exception when calling CoreV1Api->read_namespaced_service: {e}\n")
        except ValidationError as v_err:
            raise SystemExit(f"Validation error occurred: {v_err}") from v_err
        except Exception as err:
            raise SystemExit(f"An error occurred: {err}") from err
