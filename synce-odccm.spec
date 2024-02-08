# NOTE: deprecated in favour of generic dccm support in synce-core.spec
Summary:	DCCM implementation for Windows Mobile 5 (and newer) devices
Summary(pl.UTF-8):	Implementacja DCCM dla urządzeń Windows Mobile 5 (i nowszych)
Name:		synce-odccm
Version:	0.13
Release:	0.1
License:	GPL v2+
Group:		Applications/Networking
Source0:	https://downloads.sourceforge.net/synce/odccm-%{version}.tar.gz
# Source0-md5:	8f12585398f1a79518887d5f94cf122d
Source1:	odccm.init
URL:		https://sourceforge.net/projects/synce/
BuildRequires:	dbus-devel >= 0.60
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 1:2.8
BuildRequires:	gnet-devel >= 2.0
BuildRequires:	hal-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.559
BuildRequires:	synce-libsynce-devel >= %{version}
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts >= 0.4.0.10
%requires_ge_to synce-libsynce synce-libsynce-devel
Conflicts:	synce-kde < 0.9.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
odccm maintains a connection to a WinCE device, responding to keep
alives and providing other members of the SynCE suite of tools with
details of the IP address and providing the ability to autorun scripts
upon connection.

%description -l pl.UTF-8
odccm utrzymuje połączenie z urządzeniem WinCE, odpowiadając na
zapytania "keep alive", udostępniając innym narzędziom z zestawu SynCE
szczegóły o adresie IP oraz zapewniając możliwość automatycznego
uruchamiania skryptów po połączeniu.

%prep
%setup -q -n odccm-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/rc.d/init.d
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/odccm

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add odccm
%service odccm restart

%preun
if [ "$1" = "0" ]; then
	%service -q odccm stop
	/sbin/chkconfig --del odccm
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_sbindir}/odccm
/etc/dbus-1/system.d/odccm.conf
%attr(754,root,root) /etc/rc.d/init.d/odccm
%{_mandir}/man1/odccm.1*
