Summary:	D1X - modified version of Descent 1
Summary(pl):	D1X - zmodyfikowana wersja Descenta 1
Name:		d1x
Version:	1.43
%define sver	%(echo %{version} | tr -d .)
Release:	2
License:	non-commercial
Group:		X11/Applications/Games
Source0:	ftp://pyropilots.org/pub/d1x/%{name}%{sver}sc.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-fix.patch
Patch3:		%{name}-paths.patch
URL:		http://d1x.warpcore.org/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1
BuildRequires:	kdelibs-devel
%ifarch %{ix86}
BuildRequires:	nasm
%endif
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
D1X is a modification of the Descent 1 source that was released by
Parallax. It's mostly compatible with the Descent 1 v1.5, both in
multiplayer and on the local machine.

%description -l pl
D1X to modyfikacja ¼róde³ Descenta 1 udostêpnionych przez Parallax.
Jest w wiêkszo¶ci kompatybilny z Descentem 1 w wersji 1.5, zarówno
w trybie dla wielu graczy, jak i bez sieci.

%package common
Summary:	D1X - modified version of Descent 1
Summary(pl):	D1X - zmodyfikowana wersja Descenta 1
Group:		X11/Applications/Games

%description common
D1X is a modification of the Descent 1 source that was released by
Parallax. It's mostly compatible with the Descent 1 v1.5, both in
multiplayer and on the local machine.

This package contains only common files for all versions of D1X. You
will need also one of game binaries (either SDL or GL version)
appropriate for your versions of game data (shareware or full) and
actual game data files.

%description common -l pl
D1X to modyfikacja ¼róde³ Descenta 1 udostêpnionych przez Parallax.
Jest w wiêkszo¶ci kompatybilny z Descentem 1 w wersji 1.5, zarówno
w trybie dla wielu graczy, jak i bez sieci.

Ten pakiet zawiera tylko wspólne pliki dla wszystkich wersji D1X.
Oprócz niego potrzebny jest który¶ z pakietów z binark± gry (w wersji
SDL lub GL) odpowiedni dla posiadanych danych gry (shareware lub
pe³nej wersji) oraz w³a¶ciwe pliki z danymi.

%package sdl-full
Summary:	D1X - SDL-based binary for full version of game
Summary(pl):	D1X - u¿ywaj±ca SDL binarka dla pe³nej wersji gry
Group:		X11/Applications/Games
Provides:	d1x-full
Requires:	%{name}-common = %{version}

%description sdl-full
This package contains D1X binary compiled with SDL support for full
version of game. You will need to place full (commercial) version of
game data files in /usr/X11R6/share/d1x.

%description sdl-full -l pl
Ten pakiet zawiera binarkê D1X skompilowan± z obs³ug± SDL dla pe³nej
wersji gry. Pliki z danymi z pe³nej (komercyjnej) wersji gry trzeba
umie¶ciæ w katalogu /usr/X11R6/share/d1x.

%package sdl-shareware
Summary:	D1X - SDL-based binary for shareware version of game
Summary(pl):	D1X - u¿ywaj±ca SDL binarka dla wersji shareware gry
Group:		X11/Applications/Games
Provides:	d1x-shareware
Requires:	%{name}-common = %{version}

%description sdl-shareware
This package contains D1X binary compiled with SDL support for full
version of game. You will need to install d1x-data-shareware package
or place shareware version of game data files in /usr/X11R6/share/d1x.

%description sdl-shareware -l pl
Ten pakiet zawiera binarkê D1X skompilowan± z obs³ug± SDL dla wersji
shareware gry. Trzeba do niego doinstalowaæ pakiet d1x-data-shareware
lub pliki z danymi z wersji shareware umie¶ciæ w /usr/X11R6/share/d1x.

%package gl-full
Summary:	D1X - GL-based binary for full version of game
Summary(pl):	D1X - u¿ywaj±ca GL binarka dla pe³nej wersji gry
Group:		X11/Applications/Games
Provides:	d1x-full
Requires:	%{name}-common = %{version}
Requires:	OpenGL

%description gl-full
This package contains D1X binary compiled with GL support for full
version of game. You will need to place full (commercial) version of
game data files in /usr/X11R6/share/d1x.

%description gl-full -l pl
Ten pakiet zawiera binarkê D1X skompilowan± z obs³ug± GL dla pe³nej
wersji gry. Pliki z danymi z pe³nej (komercyjnej) wersji gry trzeba
umie¶ciæ w katalogu /usr/X11R6/share/d1x.

%package gl-shareware
Summary:	D1X - GL-based binary for shareware version of game
Summary(pl):	D1X - u¿ywaj±ca GL binarka dla wersji shareware gry
Group:		X11/Applications/Games
Provides:	d1x-shareware
Requires:	%{name}-common = %{version}
Requires:	OpenGL

%description gl-shareware
This package contains D1X binary compiled with GL support for full
version of game. You will need to install d1x-data-shareware package
or place shareware version of game data files in /usr/X11R6/share/d1x.

%description gl-shareware -l pl
Ten pakiet zawiera binarkê D1X skompilowan± z obs³ug± GL dla wersji
shareware gry. Trzeba do niego doinstalowaæ pakiet d1x-data-shareware
lub pliki z danymi z wersji shareware umie¶ciæ w /usr/X11R6/share/d1x.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir lib
%ifnarch %{ix86}
echo "NO_ASM = 1" >> defines.in
%endif
%ifarch sparc sparc64
echo "BIGENDIAN = 1" >> defines.in
%endif

cp -f defines.in defines.mak
echo "SDL_IO = 1" >> defines.mak
%{__make} \
	OPTFLAGS="%{rpmcflags} -DD1XDATAPATH=\\\"%{_datadir}/d1x/\\\"" \
	SDLROOTDIR=/usr/X11R6
mv -f ?1x143 d1x-sdl-full

%{__make} clean
echo "SHAREWARE = 1" >> defines.mak
%{__make} \
	OPTFLAGS="%{rpmcflags} -DD1XDATAPATH=\\\"%{_datadir}/d1x/\\\"" \
	SDLROOTDIR=/usr/X11R6
mv -f ?1x143sh d1x-sdl-share

%{__make} clean
cp -f defines.in defines.mak
echo "SDLGL_IO = 1" >> defines.mak
%{__make} \
	OPTFLAGS="%{rpmcflags} -DD1XDATAPATH=\\\"%{_datadir}/d1x/\\\"" \
	SDLROOTDIR=/usr/X11R6
mv -f ?1x143_ogl d1x-gl-full

%{__make} clean
echo "SHAREWARE = 1" >> defines.mak
%{__make} \
	OPTFLAGS="%{rpmcflags} -DD1XDATAPATH=\\\"%{_datadir}/d1x/\\\"" \
	SDLROOTDIR=/usr/X11R6
mv -f ?1x143sh_ogl d1x-gl-share

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/d1x}

install d1x-*-* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%doc bugs.txt d1x.faq d1x.ini d1x.txt d1x140.txt license.txt readme.d1x readme.org todo.txt
%dir %{_datadir}/d1x

%files sdl-full
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d1x-sdl-full

%files sdl-shareware
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d1x-sdl-share

%files gl-full
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d1x-gl-full

%files gl-shareware
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/d1x-gl-share
