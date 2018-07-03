#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : certifi
Version  : 2018.4.16
Release  : 45
URL      : https://pypi.debian.net/certifi/certifi-2018.4.16.tar.gz
Source0  : https://pypi.debian.net/certifi/certifi-2018.4.16.tar.gz
Source99 : https://pypi.debian.net/certifi/certifi-2018.4.16.tar.gz.asc
Summary  : Python package for providing Mozilla's CA Bundle.
Group    : Development/Tools
License  : MPL-2.0
Requires: certifi-python3
Requires: certifi-license
Requires: certifi-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
================================
        
        `Certifi`_ is a carefully curated collection of Root Certificates for
        validating the trustworthiness of SSL certificates while verifying the identity
        of TLS hosts. It has been extracted from the `Requests`_ project.
        
        Installation
        ------------

%package legacypython
Summary: legacypython components for the certifi package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the certifi package.


%package license
Summary: license components for the certifi package.
Group: Default

%description license
license components for the certifi package.


%package python
Summary: python components for the certifi package.
Group: Default
Requires: certifi-python3

%description python
python components for the certifi package.


%package python3
Summary: python3 components for the certifi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the certifi package.


%prep
%setup -q -n certifi-2018.4.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530370356
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530370356
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/certifi
cp LICENSE %{buildroot}/usr/share/doc/certifi/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/certifi/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
