[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/mongodb-replset/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/mongodb-replset/tree/master)
Description
===========

This is a template to deploy [MongoDB](http://www.mongodb.org) to multiple
servers configured as a replica set.

This template uses [chef-solo](http://docs.opscode.com/chef_solo.html)
to configure the server.

Requirements
============
* A Heat provider that supports the following:
  * OS::Heat::ChefSolo
  * OS::Heat::RandomString
  * OS::Heat::ResourceGroup
  * Rackspace::Cloud::Server
  * OS::Nova::KeyPair
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
  <TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
  stack-create mymongodb -f mongodb-replset.yaml \
  -P peer_server_count=7
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `flavor`: Cloud Server size to use for database nodes. (Default:
  1GB Performance)
* `server_hostname`: Base hostname for database nodes. (Default: mongodb)
* `wp_web_server_flavor`: Cloud Server size to use on all of the additional web
  nodes. (Default: 2 GB Performance)
* `image`: Required: Server image used for all servers that are created as a
  part of this deployment. (Default: Ubuntu 12.04 LTS (Precise Pangolin))
* `child_template`: Location of the child template to use for the WordPress web
  servers (Default:
  https://raw.githubusercontent.com/rackspace-orchestration-templates/mongodb-replset/master/mongodb-replset-peer.yaml)
* `load_balancer_hostname`: Hostname for the Cloud Load Balancer (Default:
  WordPress-Load-Balancer)
* `chef_version`: Version of chef client to use (Default: 11.12.8)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: SSH private that can be used to login as root to the server.
* `server_public_ips`: Public IP addresses of the replica set members.

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
This template installs [MongoDB](http://www.mongodb.org/) v2.6 on multiple
servers configured as a replica set. Replica set members are configured
to coordinate via the private interface, and advertise those IPs, so clients
will need access to the private network to access multiple nodes automatically.
Direct access to a node will work from any internet address.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
