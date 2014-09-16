%global modname fedimg

Name:               python-fedimg
Version:            0.2.3
Release:            1%{?dist}
Summary:            Automatically upload Fedora Cloud images to cloud providers

Group:              Development/Libraries
License:            AGPLv3+
URL:                http://pypi.python.org/pypi/fedimg
Source0:            http://pypi.python.org/packages/source/f/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python2-devel
BuildRequires:      python-setuptools
BuildRequires:      python-nose

BuildRequires:      fedmsg
BuildRequires:      python-libcloud
BuildRequires:      python-paramiko

Requires:           fedmsg
Requires:           python-libcloud
Requires:           python-paramiko


%description
A service that listens to the Fedmsg bus and automatically uploads built Fedora
cloud images to internal and external cloud providers

%prep
%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%{__python} setup.py build

%install

%{__mkdir} -p %{buildroot}%{_sysconfdir}/fedmsg.d/
%{__cp} fedimg.cfg.example %{buildroot}%{_sysconfdir}/fedimg.cfg
%{__cp} fedmsg.d/fedimg.py %{buildroot}%{_sysconfdir}/fedmsg.d/.

%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

for file in $RPM_BUILD_ROOT%{python_sitelib}/fedimg/{services/*,uploader,messenger,util,consumers}.py; do
   chmod a+x $file
done

%check
%{__python} setup.py test

%files
%doc docs/ README.md LICENSE
%config(noreplace) %{_sysconfdir}/fedimg.cfg
%config(noreplace) %{_sysconfdir}/fedmsg.d/fedimg.py*

%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}*

%changelog
* Tue Sep 16 2014 David Gay <dgay@redhat.com> - 0.2.3-1
- initial package for Fedora
