import json
from fabric.api import env, run, hide, task
from envassert import detect, file, group, package, port, process, service, \
    user
from hot.utils.test import get_artifacts, http_check


def replset_is_ok():
    with hide('running', 'stdout'):
        mongo_cmd = "mongo --quiet --eval 'JSON.stringify(rs.status())'"
        rs_status = json.loads(run(mongo_cmd))
        return rs_status.get('ok', False)


@task
def check():
    env.platform_family = detect.detect()

    assert file.exists("/etc/mongod.conf"), "/etc/mongod.conf does not exist"
    assert port.is_listening(27017), "nothing is listening on port 27017"
    assert user.exists("mongodb"), "there is no mongodb user"
    assert group.is_exists("mongodb"), "there is no mongodb group"
    assert process.is_up("mongod"), "mongod is not running"
    assert service.is_enabled("mongod"), "service mongod is not enabled"
    assert replset_is_ok(), "replica set status was not ok"


@task
def artifacts():
    env.platform_family = detect.detect()
    get_artifacts()
