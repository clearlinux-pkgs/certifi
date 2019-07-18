#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : certifi
Version  : 2019.6.16
Release  : 56
URL      : https://files.pythonhosted.org/packages/c5/67/5d0548226bcc34468e23a0333978f0e23d28d0b3f0c71a151aef9c3f7680/certifi-2019.6.16.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/67/5d0548226bcc34468e23a0333978f0e23d28d0b3f0c71a151aef9c3f7680/certifi-2019.6.16.tar.gz
Source99 : https://files.pythonhosted.org/packages/c5/67/5d0548226bcc34468e23a0333978f0e23d28d0b3f0c71a151aef9c3f7680/certifi-2019.6.16.tar.gz.asc
Summary  : Python package for providing Mozilla's CA Bundle.
Group    : Development/Tools
License  : MPL-2.0
Requires: certifi-license = %{version}-%{release}
Requires: certifi-python = %{version}-%{release}
Requires: certifi-python3 = %{version}-%{release}
Requires: ca-certs
BuildRequires : buildreq-distutils3
BuildRequires : ca-certs
Patch1: 0001-Use-unified-trust-store.patch

%description
================================
        
        `Certifi`_ is a carefully curated collection of Root Certificates for
        validating the trustworthiness of SSL certificates while verifying the identity
        of TLS hosts. It has been extracted from the `Requests`_ project.
        
        Installation
        ------------

%package license
Summary: license components for the certifi package.
Group: Default

%description license
license components for the certifi package.


%package python
Summary: python components for the certifi package.
Group: Default
Requires: certifi-python3 = %{version}-%{release}

%description python
python components for the certifi package.


%package python3
Summary: python3 components for the certifi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the certifi package.


%prep
%setup -q -n certifi-2019.6.16
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563470650
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/certifi
cp LICENSE %{buildroot}/usr/share/package-licenses/certifi/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/certifi/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
