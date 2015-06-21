chef_gem 'mongo' do
  version '2.0.5'
end

ruby_block 'config replset' do
  block do
    Chef::Mongodb_Replset.configure(node['mongodb']['replicaset_members'], node['mongodb']['config']['replset'])
  end
end
