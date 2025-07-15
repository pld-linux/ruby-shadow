%define pkgname shadow
Summary:	Ruby bindings for shadow password access
Name:		ruby-%{pkgname}
Version:	2.5.0
Release:	1
License:	Public Domain
Group:		Development/Languages
Source0:	https://github.com/apalmblad/ruby-shadow/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e9c35620f6c25233b7b54dcab8ee955e
Patch1:		cflags.patch
URL:		https://github.com/apalmblad/ruby-shadow
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-devel
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for shadow password access.

%prep
%setup -q
%patch -P1 -p1
iconv -f EUCJP -t utf8 -o README.ja README.euc

%build
%{__ruby} extconf.rb \
	--vendor \
	--with-cflags="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README
%doc %lang(ja) README.ja
%attr(755,root,root) %{ruby_vendorarchdir}/shadow.so
