Summary:	Ruby bindings for shadow password access
Name:		ruby-shadow
Version:	1.4.1
Release:	1
License:	Public Domain
Group:		Libraries
URL:		http://ttsky.net/
Source0:	http://ttsky.net/src/%{name}-%{version}.tar.gz
# Source0-md5:	425b742ac43bff359c1717360f761790
Patch0:		ruby-1.9-support.patch
Patch1:		cflags.patch
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby bindings for shadow password access.

%prep
%setup -q -n shadow-%{version}
%patch0 -p1
%patch1 -p1
iconv -f EUCJP -t utf8 -o README.ja README.euc

%build
%{__ruby} extconf.rb \
	--with-cflags="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make}  install \
	sitearchdir=$RPM_BUILD_ROOT%{ruby_archdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY README
%doc %lang(ja) README.ja
%attr(755,root,root) %{ruby_archdir}/shadow.so
