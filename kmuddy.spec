Summary:	MUD (Multiple Users Dungeon) client for KDE
Summary(pl.UTF-8):	Klient MUD-a dla KDE
Name:		kmuddy
Version:	1.0.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.kmuddy.com/releases/stable/%{name}-%{version}.tar.gz
# Source0-md5:	b98a1753c728134c80fd253e454e41ce
Patch0:		%{name}-link.patch
URL:		http://www.kmuddy.com/
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
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
%patch0 -p1

# fix c++ syntax
%{__sed} -i 's,QColor::,,' plugins/mapper/filefilters/cmapfilefilterkmudone.cpp

# fix docbook thing
%{__sed} -i 's,dtd/kdex.dtd,%{_datadir}/apps/ksgmltools2/customization/dtd/kdex.dtd,' doc/kmuddy/index.docbook

%build
mkdir -p build
cd build
%cmake ..
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# FIXME (desktop file name)
#mv $RPM_BUILD_ROOT%{_datadir}/applnk/Games/kmuddy.desktop \
#	$RPM_BUILD_ROOT%{_desktopdir}/kde

# FIXME (category)
#echo "Categories=Qt;KDE;Game;" >> \
#	$RPM_BUILD_ROOT%{_desktopdir}/kde/kmuddy.desktop

# drop unnecessary files
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.so
%{__rm} $RPM_BUILD_ROOT%{_datadir}/apps/kmuddy/README

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG DESIGN README Scripting-HOWTO TODO
%attr(755,root,root) %{_bindir}/kmuddy
%attr(755,root,root) %{_libdir}/libkmuddycore.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmuddycore.so.1
%{_libdir}/kde4/*.so
%{_datadir}/apps/kmuddy
%{_datadir}/kde4/services/*.desktop
%{_datadir}/kde4/servicetypes/*.desktop
