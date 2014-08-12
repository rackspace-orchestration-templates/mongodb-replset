from fabric.api import env, run, task
from envassert import detect, file, group, package, port, process, service, \
    user


@task
def check():
    env.platform_family = detect.detect()

    assert file.exists("/etc/mongod.conf"), "/etc/mongod.conf does not exist"
    assert port.is_listening(27017), "nothing is listening on port 27017"
    assert user.exists("mongodb"), "there is no mongodb user"
    assert group.is_exists("mongodb"), "there is no mongodb group"
    assert process.is_up("mongod"), "mongod is not running"
    assert service.is_enabled("mongod"), "service mongod is not enabled"
