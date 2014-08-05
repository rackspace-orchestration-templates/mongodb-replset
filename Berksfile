source "https://api.berkshelf.com"

cookbook 'apt', '~> 2.4.0'
cookbook 'build-essential'
cookbook 'yum'
cookbook 'yum-epel'
cookbook 'firewall'
cookbook 'mongodb',
  git: 'https://github.com/edelight/chef-mongodb.git',
  ref: '8c593917a228752d877b76b3c2995b6d6b1ffbdb'
cookbook 'config_replset', path: './site-cookbooks/config_replset'
