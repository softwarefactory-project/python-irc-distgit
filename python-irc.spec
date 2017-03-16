%global sum     Full-featured Python IRC library for Python.

Name:           python-irc
Version:        15.0.6
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/jaraco/irc
Source0:        https://github.com/jaraco/irc/archive/%{version}.tar.gz

BuildArch:      noarch


%description
s library provides a low-level implementation of the IRC protocol for Python.
It provides an event-driven IRC client framework. It has a fairly thorough
support for the basic IRC protocol, CTCP, and DCC connections.

%package -n python2-irc
Summary:        %sum

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python2-setuptools_scm

Requires:       python-setuptools
Requires:       python-six
Requires:       python2-jaraco-collections
Requires:       python2-jaraco-text
Requires:       python2-jaraco-itertools
Requires:       python2-jaraco-logging
Requires:       python2-jaraco-functools
Requires:       python2-jaraco-stream
Requires:       python2-more-itertools
Requires:       python2-tempora
Requires:       pytz


%description -n python2-irc


%prep
%autosetup -n irc-%{version}

# Remove setuptools_scm min version requirements
sed -i "s|setuptools_scm>=.*|setuptools_scm',|" setup.py


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py build


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version} %{__python2} setup.py install --skip-build --root %{buildroot}


%files
%doc CHANGES.rst


%files -n python2-irc
%{python2_sitelib}/irc-%{version}-py*.egg-info
%{python2_sitelib}/irc


%changelog
* Thu Mar 16 2017 Tristan Cacqueray <tdecacqu@redhat.com> - 15.0.6-1
- Initial packaging
