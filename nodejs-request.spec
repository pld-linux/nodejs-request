%define		pkg	request
Summary:	Simplified HTTP request client
Name:		nodejs-%{pkg}
Version:	2.30.0
Release:	2
License:	Apache v2.0
Group:		Development/Libraries
URL:		https://github.com/mikeal/request
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	b71428776c83883d4a828c6991b2e037
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs >= 0.8.0
Requires:	nodejs-forever-agent < 0.6.0
Requires:	nodejs-forever-agent >= 0.5.0
Requires:	nodejs-json-stringify-safe < 5.1.0
Requires:	nodejs-json-stringify-safe >= 5.0.0
Requires:	nodejs-mime < 1.3.0
Requires:	nodejs-mime >= 1.2.9
Requires:	nodejs-qs < 0.7.0
Requires:	nodejs-qs >= 0.6.0
Requires:	nodejs-node-uuid < 1.5.0
Requires:	nodejs-node-uuid >= 1.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simplified HTTP request client.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr *.js lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
