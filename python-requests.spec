%define module requests

Name:		python-requests
Summary:	Python HTTP for Humans
Version:	2.33.1
Release:	1
License:	MIT
Group:		Development/Python
# See also: https://github.com/psf/requests
Url:		https://python-requests.org
Source0:	https://files.pythonhosted.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Requests allow you to send HTTP/1.1 requests. You can add headers,
form data, multipart files, and parameters with simple Python
dictionaries, and access the response data in the same way. It's
powered by httplib and urllib3, but it does all the hard work and
crazy hacks for you.

%files
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}.dist-info
