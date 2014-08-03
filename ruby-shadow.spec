%define pkgname shadow
Summary:	Ruby bindings for shadow password access
Name:		ruby-%{pkgname}
Version:	1.4.1
Release:	3
License:	Public Domain
Group:		Development/Languages
Source0:	http://ttsky.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	425b742ac43bff359c1717360f761790
Patch0:		ruby-1.9-support.patch
Patch1:		cflags.patch
Patch2:		ruby-2.0.patch
URL:		http://ttsky.net/
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
%setup -q -n shadow-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
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
