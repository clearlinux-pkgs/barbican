#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC36CDCB4DF00C68C (infra-root@openstack.org)
#
Name     : barbican
Version  : 6.0.1
Release  : 1
URL      : https://tarballs.openstack.org/barbican/barbican-6.0.1.tar.gz
Source0  : https://tarballs.openstack.org/barbican/barbican-6.0.1.tar.gz
Source99 : https://tarballs.openstack.org/barbican/barbican-6.0.1.tar.gz.asc
Summary  : OpenStack Secure Key Management
Group    : Development/Tools
License  : Apache-2.0
Requires: barbican-bin
Requires: barbican-python3
Requires: barbican-license
Requires: barbican-python
Requires: Babel
Requires: Paste
Requires: PasteDeploy
Requires: SQLAlchemy
Requires: WebOb
Requires: alembic
Requires: cffi
Requires: cryptography
Requires: eventlet
Requires: jsonschema
Requires: keystonemiddleware
Requires: ldap3
Requires: oslo.config
Requires: oslo.context
Requires: oslo.db
Requires: oslo.i18n
Requires: oslo.log
Requires: oslo.messaging
Requires: oslo.middleware
Requires: oslo.policy
Requires: oslo.serialization
Requires: oslo.service
Requires: oslo.utils
Requires: pbr
Requires: pecan
Requires: pyOpenSSL
Requires: pycrypto
Requires: six
Requires: stevedore
BuildRequires : SQLAlchemy
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : ddt
BuildRequires : ldap3
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.log
BuildRequires : oslo.messaging
BuildRequires : oslo.policy
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : oslotest
BuildRequires : pbr
BuildRequires : pecan
BuildRequires : pep8
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Generic single-database configuration.

%package bin
Summary: bin components for the barbican package.
Group: Binaries
Requires: barbican-license

%description bin
bin components for the barbican package.


%package license
Summary: license components for the barbican package.
Group: Default

%description license
license components for the barbican package.


%package python
Summary: python components for the barbican package.
Group: Default
Requires: barbican-python3

%description python
python components for the barbican package.


%package python3
Summary: python3 components for the barbican package.
Group: Default
Requires: python3-core

%description python3
python3 components for the barbican package.


%prep
%setup -q -n barbican-6.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533875366
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/barbican
cp LICENSE %{buildroot}/usr/share/doc/barbican/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/barbican-db-manage
/usr/bin/barbican-keystone-listener
/usr/bin/barbican-manage
/usr/bin/barbican-retry
/usr/bin/barbican-worker
/usr/bin/barbican-wsgi-api
/usr/bin/pkcs11-kek-rewrap
/usr/bin/pkcs11-key-generation

%files license
%defattr(-,root,root,-)
/usr/share/doc/barbican/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
