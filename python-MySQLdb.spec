Summary:	A Python interface to MySQL
Summary(pl):	Interfejs Pythona do MySQL
Name:		python-MySQLdb
Version:	1.2.1_p2
Release:	6
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
# Source0-md5:	e6b9ea21fd91cb4a5663304da727bb70
Patch0:		%{name}-py2.5.patch
URL:		http://sourceforge.net/projects/mysql-python/
BuildRequires:	mysql-devel >= 4.0.10
# fix py2.5.patch ( http://www.python.org/dev/peps/pep-0353/ ) or 
BuildRequires:	python-devel >= 2.5
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
%setup  -q -n MySQL-python-%{version}
%patch0 -p1

%build
env CFLAGS="%{rpmcflags} -DHAVE_OPENSSL=1" %{_bindir}/python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm -f $RPM_BUILD_ROOT%{py_sitedir}/{MySQLdb/{constants/,},}*.py

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
%{py_sitedir}/*.egg-info
