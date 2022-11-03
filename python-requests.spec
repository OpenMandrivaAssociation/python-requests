%define module requests

Summary:	Python HTTP for Humans
Name:		python-%{module}
Version:	2.28.1
Release:	2
# See also: https://github.com/psf/requests
Source0:	https://files.pythonhosted.org/packages/source/r/requests/requests-%{version}.tar.gz
Patch0:		https://github.com/psf/requests/commit/c57f1f0ca10e61771b459c857182c23626607312.patch
License:	MIT
Group:		Development/Python
Url:		http://python-requests.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python-pkg-resources
Requires:	python-certifi
Requires:	python-urllib3

%description
Requests allow you to send HTTP/1.1 requests. You can add headers,
form data, multipart files, and parameters with simple Python
dictionaries, and access the response data in the same way. It's
powered by httplib and urllib3, but it does all the hard work and
crazy hacks for you.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{py_puresitedir}/requests*
