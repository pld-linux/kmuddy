Summary:	MUD (Multiple Users Dungeon) client for KDE
Summary(pl.UTF-8):	Klient MUD-a dla KDE
Name:		kmuddy
Version:	0.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.kmuddy.net/files/%{name}-%{version}.tar.gz
# Source0-md5:	54146de43c0462b60c1328ab348c7789
URL:		http://www.kmuddy.net/
BuildRequires:	arts-qt-devel
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 9:3.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMuddy is a MUD (Multiple Users Dungeon) client, that supports all the
features you'd expect from a MUD client - aliases, triggers,
variables, scripting(external) MCCP and MSP protocols and many more...

%description -l pl.UTF-8
KMuddy to klient MUD-a dla KDE, posiadający wszystkie cechy jakich
można oczekiwać od klienta MUD-a - aliasy, trigery, zmienne, skrypty
MCCP i MSP, oraz wiele innych...

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

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

# FIXME (desktop file name)
mv $RPM_BUILD_ROOT%{_datadir}/applnk/Games/kmuddy.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

# FIXME (category)
echo "Categories=Qt;KDE;Game;" >> \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmuddy.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/kde/*
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/*
%{_datadir}/%{name}
