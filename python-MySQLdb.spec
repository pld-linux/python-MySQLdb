%include	/usr/lib/rpm/macros.python

Summary:	A Python interface to MySQL
Summary(pl):	Interfejs Pythona do MySQL
Name:		python-MySQLdb
Version:	1.1.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
# Source0-md5:	e961a6bca10dc3d502db74ad75423b0e
URL:		http://sourceforge.net/projects/mysql-python/
#Requires:	mysql >= 3.23.49
BuildRequires:	mysql-devel >= 4.0.10
BuildRequires:	python-devel >= 2.2.1
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
Ten pakiet zapewnia dostêp do baz danych MySQL z poziomu skryptów
jêzyka Python.

%prep
%setup -q -n MySQL-python-%{version}

%build
env CFLAGS="%{rpmcflags}" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-lib=%{py_sitescriptdir} \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG doc/*
%attr(755,root,root) %{py_sitescriptdir}/*.so
%{py_sitescriptdir}/*.py?

%dir %{py_sitescriptdir}/MySQLdb
%{py_sitescriptdir}/MySQLdb/*.py?

%dir %{py_sitescriptdir}/MySQLdb/constants
%{py_sitescriptdir}/MySQLdb/constants/*.py?
