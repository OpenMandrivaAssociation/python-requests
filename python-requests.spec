%define	module	requests

Summary:	Python HTTP for Humans
Name:		python-%{module}
Version:	2.18.4
Release:	1
Source0:	https://github.com/requests/requests/archive/v%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://python-requests.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools
Requires:	python-certifi
Requires:	python-urllib3

%description
Requests allow you to send HTTP/1.1 requests. You can add headers,
form data, multipart files, and parameters with simple Python
dictionaries, and access the response data in the same way. It's
powered by httplib and urllib3, but it does all the hard work and
crazy hacks for you.


%package -n python2-%{module}
Summary:	Python HTTP for Human
Group:		Development/Python
Requires:	python2

%description -n python2-%{module}

%prep
%setup -q -n %{module}-%{version} -c

mv %{module}-%{version} python2
cp -r python2 python3

%build
pushd python2
%{__python2} setup.py build
popd

pushd python3
%{__python} setup.py build
popd

%install
pushd python2
PYTHONDONTWRITEBYTECODE= %__python2 setup.py install --root=%{buildroot}
popd

pushd python3
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
popd

%files
%{py_puresitedir}/requests*

%files -n python2-%{module}
%{py2_puresitedir}/requests*
