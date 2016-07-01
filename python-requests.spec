%define	module	requests

Summary:	Python HTTP for Humans
Name:		python-%{module}
Version:	2.10.0
Release:	1
Source0:	http://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://python-requests.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
Requires:	python-certifi
Requires:	python-urllib3

%description
Requests allow you to send HTTP/1.1 requests. You can add headers,
form data, multipart files, and parameters with simple Python
dictionaries, and access the response data in the same way. It's
powered by httplib and urllib3, but it does all the hard work and
crazy hacks for you.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc HISTORY.rst LICENSE README.rst
%{py_puresitedir}/requests*

