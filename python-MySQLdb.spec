Summary:	An Python interface to MySQL
Summary(pl):	Interfejs Pythona do MySQL
Name:		python-MySQLdb
Version:	0.9.0
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://prdownloads.sourceforge.net/mysql-python/MySQL-python-%{version}.tar.gz
URL:		http://sourceforge.net/projects/mysql-python/
Requires:	mysql >= 3.22.32
Requires:	python >= 1.5.2
BuildRequires:	python-devel >= 1.5.2
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
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
%{_bindir}/python -- setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES
gzip -9nf README
tmpfile=INSTALLED_FILES.$$
grep -v 'py$' INSTALLED_FILES | sort > $tmpfile && mv $tmpfile INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(644,root,root,755)
%doc *.gz doc/*.html
