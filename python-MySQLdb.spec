
%define module MySQLdb
%define python_sitepkgsdir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/site-packages/')"`)
%define python_config_dir %(echo `python -c "import sys; print (sys.prefix + '/lib/python' + sys.version[:3] + '/config/')"`)
%define python_compile python -c "import compileall; compileall.compile_dir('.')"
%define python_compile_opt python -O -c "import compileall; compileall.compile_dir('.')"

Summary:	Python interface to MySQL 
Summary(pl):	Interfejs pomiêdzy jêzykiem Python a baz± danych MySQL
Name:		python-%{module}
Version:	0.2.2
Release:	1
Copyright:	Distributable 
Group:		Development/Languages/Python
Group(de):	Entwicklung/Sprachen/Python
Group(pl):	Programowanie/Jêzyki/Python
Source0:	http://dustman.net/andy/python/MySQLdb/%{version}/%{module}-%{version}.tar.gz
Requires:	python >= 1.5.2
BuildRequires:	python-devel >= 1.5.2
BuildRequires:	mysql-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides access to MySQL data from Python.

%description -l pl
Ten pakiet zapewnia dostêp do baz danych MySQL z poziomu skryptów
jêzyka Python.

%prep
%setup -q -n %{module}-%{version}

%build
install %{python_config_dir}/Makefile.pre.in .
%{__make} -f Makefile.pre.in boot
%{__make} OPT="$RPM_OPT_FLAGS"

%python_compile
%python_compile_opt

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}
echo MySQLdb > $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}.pth
install _mysqlmodule.so %{module}.{py,pyc,pyo} $RPM_BUILD_ROOT%{python_sitepkgsdir}/%{module}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf examples/README

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf README license.py doc/*.sgml
install -d html
mv -f doc/*.html html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,license.py,doc/*.sgml}.gz html

%dir %{python_sitepkgsdir}/%{module}
%{python_sitepkgsdir}/%{module}.pth
%{python_sitepkgsdir}/%{module}/%{module}.py
%{python_sitepkgsdir}/%{module}/%{module}.pyc
%{python_sitepkgsdir}/%{module}/%{module}.pyo

%attr(755,root,root) %{python_sitepkgsdir}/%{module}/_mysqlmodule.so

%dir %{_examplesdir}/%{name}
%{_examplesdir}/%{name}/*
