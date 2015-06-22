require 'json'

class Chef
  class Mongodb_Replset
    def self.configure(members, name)
      require 'rubygems'
      require 'mongo'

      connection = Mongo::Client.new([ 'localhost:27017' ], :socket_timeout => 30, :slave_ok => true)
      admin = connection.database
      cmd = BSON::Document.new

      rs_member_ips = []

      members.each_index do |n|
        rs_member_ips << { _id: n, host: "#{members[n]}:27017" }
      end

      cmd['replSetInitiate'] = {
           _id: name,
           members: rs_member_ips
      }

      result = admin.command(cmd, :check_response => false)
    end
  end
end
