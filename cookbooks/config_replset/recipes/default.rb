chef_gem 'mongo'

ruby_block 'config replset' do
  block do
    Chef::Mongodb_Replset.configure(node['mongodb']['replicaset_members'], node['mongodb']['config']['replset'])
  end
end
