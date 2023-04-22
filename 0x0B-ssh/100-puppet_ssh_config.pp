file { '/root/.ssh/config':
  ensure  => 'present',
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
  content => "Host server.example.com\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
