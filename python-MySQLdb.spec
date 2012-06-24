Summary:	A Python interface to MySQL
Summary(pl):	Interfejs Pythona do MySQL
Name:		python-MySQLdb
Version:	1.2.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
# Source0-md5:	b0eb974cc3c917276e015275e1ec996f
URL:		http://sourceforge.net/projects/mysql-python/
BuildRequires:	mysql-devel >= 4.0.10
BuildRequires:	python-devel >= 2.3.4
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

%description -l pl
Ten pakiet zapewnia dost�p do baz danych MySQL z poziomu skrypt�w
j�zyka Python.

%prep
%setup -q -n MySQL-python-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/*
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/*.py?
%dir %{py_sitedir}/MySQLdb
%{py_sitedir}/MySQLdb/*.py?
%dir %{py_sitedir}/MySQLdb/constants
%{py_sitedir}/MySQLdb/constants/*.py?
