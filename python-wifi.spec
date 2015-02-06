Summary:	Python binding for the wireless extensions
Name:		python-wifi
Version:	0.5.0
Release:	4
URL:		https://developer.berlios.de/projects/pythonwifi/
Source0:	http://download.berlios.de/pythonwifi/%{name}-%{version}.tar.bz2
#python-wifi is licensed under LGPLv2+, however, the examples
#(e.g. iwconfig.py and iwlist.py) are licensed under GPLv2+
License:	LGPLv2+ and GPLv2+
Group:		Development/Python
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
Python-Wifi is a Python library that provides access to information about a
W-LAN card's capabilities, like the wireless extensions written in C.

%prep
%setup -q
#Remove shebang
sed -i -e '/^#!\//, 1d' {tests/output_diff.sh,examples/*.py}
#Fix permissions
chmod -x {tests/output_diff.sh,examples/*.py}
# Convert to utf-8
for file in docs/AUTHORS; do
    mv $file timestamp
    iconv -f ISO-8859-1 -t UTF-8 -o $file timestamp
    touch -r timestamp $file
done

# fix permissions:
chmod 644 docs/* README tests/*
chmod 755 docs/logos tests

%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root="%{buildroot}"

#Delete the doc files, wrong location
rm -rf %{buildroot}/usr/{INSTALL,README}
rm -rf %{buildroot}/usr/docs

# move the examples
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}/usr/examples %{buildroot}%{_defaultdocdir}/%{name}/
rm -rf %{buildroot}/usr/examples
# copy tests
cp -pr tests %{buildroot}%{_defaultdocdir}/%{name}/

#Move the man pages
mkdir -p %{buildroot}%{_mandir}
mv %{buildroot}/usr/man/man8  %{buildroot}%{_mandir}
rm -fr %{buildroot}/usr/man

%files
%doc README docs/AUTHORS docs/BUGS docs/ChangeLog
%doc docs/LICENSE* docs/NEWS docs/ROADMAP docs/TODO docs/VERSION
%doc docs/*.txt
%{_mandir}/man8/iw*.*
%{python_sitelib}/pythonwifi
%{python_sitelib}/python_wifi-%{version}-py%{py_ver}.egg-info


%changelog
* Sat Oct 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 590520
- rebuild for python-2.7
- use %%pyver macro in the file list.

* Fri Mar 26 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.5.0-1mdv2010.1
+ Revision: 527883
- import python-wifi


