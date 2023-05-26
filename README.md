# Helm-Compose

`helm-compose` is a CLI tool that brings the simplicity and elegance of Docker Compose to Helm. Manage your Helm charts like you would manage Docker services with Docker Compose.

## Features

- Define your Helm releases in a YAML or JSON file.
- Use simple commands to install, upgrade, rollback, delete Helm releases.
- Get status of Helm releases.
- Health checks for Kubernetes services.

## Installation

You can install `helm-compose` using pip:

```sh
pip install helm-compose
```

## Usage

You can define your Helm releases in a YAML or JSON file like this:

```yaml
services:
  web:
    kube_context: "my_kube_context"
    chart: "nginx"
    repo: "https://charts.bitnami.com/bitnami"
    version: "9.3.0"
    namespace: "default"
    values:
      service:
        type: ClusterIP
        port: 8080
```

Then you can manage your Helm releases with simple commands:

```sh
# Deploy Helm releases
helm-compose deploy config.yaml

# Upgrade Helm releases
helm-compose upgrade config.yaml

# Rollback Helm releases
helm-compose rollback config.yaml

# Delete Helm releases
helm-compose delete config.yaml

# Get status of Helm releases
helm-compose status config.yaml

# Check health of Kubernetes services
helm-compose health config.yaml
```

## Contributing

We welcome contributions! Please fork this repository and make your changes in a separate branch. When your changes are ready, raise a pull request.


## Development

You can start development by forking this repository. 
Here's what each command in the `Makefile` does:

- `make init`: Install the necessary Python libraries for creating and uploading the package.
- `make clean`: Clean up files and directories from previous builds.
- `make dist`: Create the package distribution.
- `make test`: Install the package locally for testing.
- `make install`: Install the package locally.
- `make upload`: Upload the package to PyPI.

You can run these commands by typing `make <command>` in your terminal. For example, `make init` or `make dist`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, please open an issue or send an email to `ashutoshdtu@gmail.com`.
