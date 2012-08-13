%define	module	requests
%define name	python-%{module}
%define version 0.13.6
%define release 1

Summary:	Python HTTP for Humans
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://python-requests.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-certifi, python-urllib3

%description
Requests allow you to send HTTP/1.1 requests. You can add headers,
form data, multipart files, and parameters with simple Python
dictionaries, and access the response data in the same way. It's
powered by httplib and urllib3, but it does all the hard work and
crazy hacks for you.

%prep
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY.rst LICENSE README.rst
%py_sitedir/requests*
