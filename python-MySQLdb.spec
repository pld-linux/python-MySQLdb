Summary:	A Python interface to MySQL
Summary(pl.UTF-8):	Interfejs Pythona do MySQL
Name:		python-MySQLdb
Version:	1.2.3
Release:	12
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
# Source0-md5:	215eddb6d853f6f4be5b4afc4154292f
URL:		http://sourceforge.net/projects/mysql-python/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	mysql-devel >= 4.0.10
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An interface to the popular MySQL database server for Python. The
design goals are:

- Compliance with Python database API version 2.0
- Thread-safety
- Thread-friendliness (threads will not block each other)

%description -l pl.UTF-8
Ten pakiet zapewnia dostęp do baz danych MySQL z poziomu skryptów
języka Python. Projekt jest tworzony z myślą o:
- zgodności z bazodanowym API Pythona w wersji 2.0
- przyjaznością dla wątków (wątki nie zablokują się nawzajem).

%prep
%setup  -q -n MySQL-python-%{version}

%build
CFLAGS="%{rpmcflags} -DHAVE_OPENSSL=1"
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py[co]
%dir %{py_sitedir}/MySQLdb
%{py_sitedir}/MySQLdb/*.py[co]
%dir %{py_sitedir}/MySQLdb/constants
%{py_sitedir}/MySQLdb/constants/*.py[co]
%{py_sitedir}/*.egg-info
