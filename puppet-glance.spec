%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:           puppet-glance
Version:        XXX
Release:        XXX
Summary:        Puppet module for OpenStack Glance
License:        ASL 2.0

URL:            https://launchpad.net/puppet-glance

Source0:        https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-keystone
Requires:       puppet-openstacklib
Requires:       puppet-oslo
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for OpenStack Glance

%prep
%setup -q -n openstack-glance-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/glance/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/glance/



%files
%{_datadir}/openstack-puppet/modules/glance/


%changelog


