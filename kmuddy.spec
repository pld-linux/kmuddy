Summary:	MUD (Multiple Users Dungeon) client for KDE
Summary(pl):	Klient MUD'a pod KDE
Name:		kmuddy
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.kmuddy.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	5e6d09abcf95862c4398a0d6d88e5a10
URL:		http://www.kmuddy.org/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMuddy is a MUD (Multiple Users Dungeon) client, that supports all the
features you'd expect from a MUD client - aliases, triggers,
variables, scripting(external) MCCP and MSP protocols and many more...

%description -l pl
KMuddy to klient MUD'a pod KDE, posiadaj±cy wszystkie cechy jakich by¶
oczekiwa³ od klienta MUD'a - aliasy, trigery, zmienne, skrypty MCCP i
MSP, oraz wiele innych...

%prep
%setup -q

%build

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}


# FIXME (desktop file name)
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Games/kmuddy.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

# FIXME (category)
echo "Categories=Qt;KDE;Game;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmuddy.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
