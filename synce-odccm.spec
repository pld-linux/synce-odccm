Summary:	SynCE: Communication application
Name:		synce-odccm
Version:	0.10.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	977b8123a6d83dfb3194011b7c5b564c
URL:		http://synce.sourceforge.net/
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gnet-devel >= 2.0
BuildRequires:	gob2
BuildRequires:	hal-devel
BuildRequires:	synce-libsynce-devel = %{version}
Conflicts:	synce-kde < 0.9.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
odccm is part of the SynCE project

%prep
%setup -q -n odccm-%{version}

%build
%configure \
	--with-libsynce=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT
