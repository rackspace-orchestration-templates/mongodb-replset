chef_gem 'mongo' do
  version '1.12.0'
end

ruby_block 'config replset' do
  block do
    Chef::Mongodb_Replset.configure(node['mongodb']['replicaset_members'], node['mongodb']['config']['replset'])
  end
end
