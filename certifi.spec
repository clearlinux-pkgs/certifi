#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : certifi
Version  : 2016.9.26
Release  : 21
URL      : http://pypi.debian.net/certifi/certifi-2016.9.26.tar.gz
Source0  : http://pypi.debian.net/certifi/certifi-2016.9.26.tar.gz
Summary  : Python package for providing Mozilla's CA Bundle.
Group    : Development/Tools
License  : ISC MPL-2.0
Requires: certifi-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Certifi: Python SSL Certificates
================================
`Certifi`_ is a carefully curated collection of Root Certificates for
validating the trustworthiness of SSL certificates while verifying the identity
of TLS hosts. It has been extracted from the `Requests`_ project.

%package python
Summary: python components for the certifi package.
Group: Default

%description python
python components for the certifi package.


%prep
%setup -q -n certifi-2016.9.26

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
