import datetime

import docker


class flow:

    test_mode: bool = False
    backup_folder: str = "/backup"
    volumes = None
    _backups_made = []

    def __init__(self, container_name: str):
        self.client = docker.from_env()
        self._container_name = container_name
        # self.container = self.client.get(container_name)

    @property
    def container_name(self) -> str:
        return self._container_name

    def rollback(self):
        ...

    def teardown(self):
        ...

    def backup(self):

        # Stop container

        # Backup volumes
        if not isinstance(self.volumes, list):
            self.volumes = [self.volumes]
        for volume in self.volumes:
            n = datetime.datetime.now()
            d = n.strftime("%Y_%m_%d_%0l_%M_%S")
            mounts = [f"{volume}:/from", f"{self.backup_folder}:/to"]
            self.client.containers.run(
                "alpine",
                f'ash -c "cd /from ; tar cvf /to/{volume}_{d}.tar ."',
                auto_remove=True,
                volumes=mounts,
            )
            self._backups_made.append(f"{volume}_{d}.tar")

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
