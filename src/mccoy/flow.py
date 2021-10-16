import docker

class flow:

    test_mode: bool = False

    def __init__(self, container_name: String):
        self.client = docker.from_env()
        self._container_name = container_name
        self.container = self.client.get(container_name)

    @property
    def container_name(self)-> String:
        return self._container_name

    def rollback(self):
        ...

    def teardown(self):
        ...

    def backup(self):

        # Stop container

        # Backup volumes

        # Remove old (backup) containers

        # Rename container to backup

        ...

    def __call__(self):

        # Check for running container

        # Backup
        self.backup()

        # Spin up new container

        # Run tests
        if self.run_tests():
            # Roll back
            self.rollback()
            return

        # Cleanup
        if self.test_mode:
            self.teardown()

        


